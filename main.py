from checklistParser import parseChecklist
from docGenerator import DocGenerator
from resources import Resources
import logger

log = logger.getLogger()
checklistObject = parseChecklist( "C:/Users/misc2/Documents/PyProjects/DSEGenerator/test/data/checkliste.docx" )
if checklistObject is not None:
    docGenerator = DocGenerator(checklistObject)
    retval = docGenerator.saveDocument()
    if retval == True:
        log.info("Document processed successfully!")
    else:
        log.error("Document hasn't been created! Error occured during processing!")
else:
    log.error("Checklist Document hasn't been processed!")

