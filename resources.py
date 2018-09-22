from pkg_resources import resource_filename
import wx

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
       return Resources.get_filename(Resources.templatePath + "/" + Resources.getVersion(Resources.dseTemplate, version))

    @staticmethod
    def getChecklisteTemplate(version = "1.0"):
        return Resources.get_filename(Resources.templatePath + "/" + Resources.getVersion(Resources.checklistTemplate, version))

    @staticmethod
    def get_filename(path):
        try:
            filename = resource_filename(__name__, path)
            return filename
        except(FileNotFoundError):
            wx.MessageBox("Error occured by determining resource! " + FileNotFoundError.strerror(), caption="Error occured!")

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
