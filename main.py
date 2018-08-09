from checklistParser import parseChecklist
from docGenerator import DocGenerator

"""checklistObject = parseChecklist(     "C:/Users/misc2/Documents/PyProjects/DSEGenerator/test/data/checkliste.docx" )
print("checklistobject...")
print(checklistObject.getElementList()) 
print(checklistObject.wordVersion + " " + checklistObject.xmlVersion)"""

docGenerator = DocGenerator()
docGenerator.parseTemplate("1.0")

