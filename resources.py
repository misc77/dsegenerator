from pkg_resources import resource_filename

class Resources:
    templatePath = "/input"
    outputPath = "/output"
    configPath = "/config"
    logPath = "/log"
    configFile = "config.ini"
    dseTemplate = "dse_template_v.xml"
    checklistTemplate = "checkliste_template_v.xml"
    logFile = "DSEGenerator.log"

    @staticmethod
    def getDSETemplate(version = "1.0"):
        relativePath = Resources.templatePath + "/" + Resources.getVersion(Resources.dseTemplate, version)
        filename = resource_filename(__name__, relativePath)
        return filename

    @staticmethod
    def getChecklisteTemplate(version = "1.0"):
        relativePath = Resources.templatePath + "/" + Resources.getVersion(Resources.checklistTemplate, version)
        filename = resource_filename(__name__, relativePath)
        return filename

    @staticmethod
    def getVersion(filename, version):
        return filename.split(".")[0] + version + "." + filename.split(".")[1]

    @staticmethod
    def getOutputPath():
        relativPath = Resources.outputPath
        filename = resource_filename(__name__, relativPath)
        return filename

    @staticmethod
    def getConfigFile():
        filename = resource_filename(__name__, Resources.configPath + "/" + Resources.configFile)
        return filename

    @staticmethod
    def getLogFile():
        filename = resource_filename(__name__, Resources.logPath + "/" + Resources.logFile)
        return filename

    @staticmethod
    def validVersions(versionA="1.0", versionB="1.0"):
        if versionA == versionB:
            return True
        else:
            return False
