import logging
import configparser
from resources import Resources


def getLogger():
    config = configparser.ConfigParser()
    try:
        config.read(Resources.getConfigFile())
    except(FileNotFoundError):
        print("ERROR: File '" + Resources.getConfigFile() + "' NOT found! " + FileNotFoundError.strerror)
        config = None

    if config is not None and 'Logging' in config:
        logLevel = config['Logging'].getint("APPLICATION_LOG_LEVEL")
    else:
        logLevel = logging.DEBUG  
       
    logger = logging.getLogger("DSEGenerator")
    logger.setLevel(logLevel)

    fileHandler = logging.FileHandler(Resources.getLogFile())
    fileHandler.setLevel(logLevel)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logLevel)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fileHandler.setFormatter(formatter)
    consoleHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)
    return logger