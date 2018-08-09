import os
import xml.etree.ElementTree as ET

from xmlObject import XMLObject
from docx import Document
from resources import Resources


class DocGenerator:
   
    
    def __init__(self):
        self.checklistObject = {}
        self.dseTemplate = {}
        self.dseDocument = ""

    def parseTemplate(self, version = "1.0"):
        res = Resources()
        filename = res.getDSETemplate(version)
        """ TODO: Exception Handling """
        tree = ET.parse(filename)   
        root = tree.getroot()
        templateObject = XMLObject()
        templateObject.xmlVersion = root.attrib.get("version")

        """ TODO: Implement version check """

        for elem in root:
            print(elem.tag)