from pkg_resources import resource_filename

class Resources:
    templatePath = "/input"
    dseTemplate = "dse_template_v.xml"
    checklistTemplate = "checkliste_template_v.xml"

    def getDSETemplate(self, version = "1.0"):
        relativePath = Resources.templatePath + "/" + self.getVersion(Resources.dseTemplate, version)
        filename = resource_filename(__name__, relativePath)
        return filename

    def getChecklisteTemplate(self, version = "1.0"):
        relativePath = Resources.templatePath + "/" + self.getVersion(Resources.checklistTemplate, version)
        filename = resource_filename(__name__, relativePath)
        return filename

    def getVersion(self, filename, version):
        return filename.split(".")[0] + version + "." + filename.split(".")[1]