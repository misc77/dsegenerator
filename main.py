from docx import Document
import xml.etree.ElementTree as ET
from checklist import Checklist

""" 
    readTable

    reads the content of a word table
    and puts the content into an instance of checklist class.
    This instance will be persisted into an Sqlite table
"""
def readTable(table):
    r = c = 0
    print("columns: " + str(len(table.columns)) + " rows: " + str(len(table.rows)))

    for row in table.rows:
        r=r+1
        print("---- row " + str(r) + "---")
        c=0
        for col in table.columns:
            c=c+1
            cell = table.cell(r-1, c-1)
            print(str(r) +"," + str(c))
            print(cell.text)
            if len(cell.tables) > 0:
                for t in cell.tables:
                    readTable(t)

"""
    readChecklist

    reads the input document that is basis for
    generation of the dse-document
"""
def readChecklist(file):
    document = Document(file)
    i = 0

    for t in document.tables:
        i=i+1
        print("####### START (" + str(i) + ") #######")
        readTable(t)
        print("####### END (" + str(i) + ") #######")
        print("")
        if i>=5:
            break

    print("document finished - contained " + str(i) + " tables")


"""readChecklist("C:/Users/misc2/Documents/PyProjects/DSEGenerator/test/data/checkliste.docx")"""

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

def parseChecklist(xmlFile, checklistFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    checklistDocument = Document(checklistFile)
    checklistObject = Checklist()
    checklistObject.xmlVersion = root.attrib.get("version")

    for elem in root:
        print(elem.attrib.get("wordType"))
        if elem.attrib.get("wordType") == "table":
            checklistObject.addCategory(elem.tag, parseTable(elem, checklistDocument))

    """ setting instance variables """
    checklistObject.setInstanceVariables()
    print("checklistobject...")
    print(checklistObject.getCategoryList()) 
    print(checklistObject.wordVersion + " " + checklistObject.xmlVersion)


parseChecklist(     "C:/Users/misc2/Documents/PyProjects/DSEGenerator/test/data/checkliste.xml"
                ,   "C:/Users/misc2/Documents/PyProjects/DSEGenerator/test/data/checkliste.docx" )
