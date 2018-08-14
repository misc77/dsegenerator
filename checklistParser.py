from docx import Document
from xmlObject import XMLObject
from resources import Resources
import xml.etree.ElementTree as ET
import const
import logging

def isWordTypeTable(child):
    if child.attrib.get(const.CHECKLIST_ATTRIB_WORDTYPE) == const.CHECKLIST_ATTRIB_WORDTYPE_TABLE:
        return True
    else:
        return False


def readVersion(checklistDocument):
    version = checklistDocument.tables[0].table.cell(1,0).text[2:]
    if version is None:
        version = "v1.0"
    return version


def parseTable(xmlElement, checklistDocument):
    pos = int(xmlElement.attrib.get(const.CHECKLIST_ATTRIB_TAB))
    table = checklistDocument.tables[pos-1]
    tableObject = {}    
    for child in xmlElement:
        zeile = int(child.attrib.get(const.CHECKLIST_ATTRIB_ROW))-1
        spalte = int(child.attrib.get(const.CHECKLIST_ATTRIB_COL))-1       
        if isWordTypeTable(child):
            tableObject[child.tag] = parseTable(child, table.cell(zeile,spalte))
        else:
            tableObject[child.tag] = table.cell(zeile,spalte).text      

    return tableObject


def parseChecklist(checklistFile):
    log = logging.getLogger("DSEGenerator.checklistParser")
    try:
        checklistDocument = Document(checklistFile)
    except (FileNotFoundError):
        log.error("File '" + checklistFile + "' not Found! " + FileNotFoundError.strerror)
        checklistDocument = None

    if checklistDocument is not None:
        version = readVersion(checklistDocument)
        checklistTemplate = Resources.getChecklisteTemplate(version)

        try:
            tree = ET.parse(checklistTemplate) 
        except (ET.ParseError):
            log.error("Checklist Template '" + checklistTemplate + "' could not be read!")
            tree = None
            checklistObject = None

        if tree != None:
            root = tree.getroot()
            checklistObject = XMLObject()
            checklistObject.xmlVersion = root.attrib.get(const.DSEDOC_ATTRIB_VERSION)
            if Resources.validVersions(version, checklistObject.xmlVersion):
                for elem in root:
                    if isWordTypeTable(elem):
                        checklistObject.addElement(elem.tag, parseTable(elem, checklistDocument))

                if const.CHECKLIST_ATTRIB_TITLE in checklistObject.elementList:
                    checklistObject.wordVersion = checklistObject.elementList[const.CHECKLIST_ATTRIB_TITLE][const.CHECKLIST_ATTRIB_VERSION]
            else:
                log.warn("No valid versions! Processing skipped!")
    else:
        log.error("Processing of Template skipped! Please check Error log!")
        checklistObject = None

    return checklistObject