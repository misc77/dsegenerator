from datetime import date

class Checklist:
        
    def __init__ (self):
        self.categoryList = {}
        self.client = ""
        self.wordVersion = ""
        self.xmlVersion = ""
        self.created = date.today()

    def setCategoryList(self, categoryList):
        self.categoryList = categoryList

    def addCategory(self, categoryName, category):
        self.categoryList[categoryName] = category

    def addCategoryEntry(self, categoryName, key, value):
        self.categoryList[categoryName][key] = value 
      
    def getCategory(self, categoryName):
        return self.categoryList[categoryName]

    def getCategoryList(self):
        return self.categoryList

    def getValue(self, categoryName, key):
        return self.categoryList[categoryName][key]

    def getValueByPos(self, position):
        return self.categoryList[position]

    def setInstanceVariables(self):
        if "titel" in self.categoryList:
            self.wordVersion = self.categoryList["titel"]["version"]
        if "verantwortlicher" in self.categoryList:
            self.client = self.categoryList["verantwortlicher"]["adressTabelle"]["adresse"].split("\n")[0]
        