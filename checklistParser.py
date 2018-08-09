from docx import Document
import xml.etree.ElementTree as ET
from xmlObject import XMLObject
from resources import Resources

def readVersion(checklistDocument):
    version = checklistDocument.tables[0].table.cell(1,0).text[2:]
    print(version)
    return version

def parseTable(xmlElement, checklistDocument):
    pos = int(xmlElement.attrib.get("tabelle"))
    table = checklistDocument.tables[pos-1]
    tableObject = {}
    
    for child in xmlElement:
        zeile = int(child.attrib.get("zeile"))-1
        spalte = int(child.attrib.get("spalte"))-1
        print (str(zeile) + " " + str(spalte))

        if child.attrib.get("wordType") == "table":
            tableObject[child.tag] = parseTable(child, table.cell(zeile,spalte))
        else:
            tableObject[child.tag] = table.cell(zeile,spalte).text
            print (child.tag, child.attrib) 
            print (table.cell(zeile,spalte).text)
    
    return tableObject

def parseChecklist(checklistFile):
    checklistDocument = Document(checklistFile)
    version = readVersion(checklistDocument)
    res = Resources()
    checklistTemplate = res.getChecklisteTemplate(version)
    tree = ET.parse(checklistTemplate) """ TODO: Exception Handling """
    root = tree.getroot()
    checklistObject = XMLObject()
    checklistObject.xmlVersion = root.attrib.get("version")

    for elem in root:
        print(elem.attrib.get("wordType"))
        if elem.attrib.get("wordType") == "table":
            checklistObject.addElement(elem.tag, parseTable(elem, checklistDocument))

    """ setting instance variables """    
    if "titel" in checklistObject.elementList:
        checklistObject.wordVersion = checklistObject.elementList["titel"]["version"]
    return checklistObject