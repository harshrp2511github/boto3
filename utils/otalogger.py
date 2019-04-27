#IoTium OTAccess LOGGER
#title           :otalogger.py
#description     :This is the library that provides Logger Object which helps to log locally.
#author          :Sandeep Machiraju
#maintainer      :IoTium
#date            :2018-09-11
#version         :1.0
#usage           :
#==============================================================================

#imports
import logging.handlers
import logging.config
import datetime
import logging
import os

class OtaLogger:
    def _prepareLogger(self,logPath,loggerName):
        otaLogger = logging.getLogger(loggerName)
        otaLogger.setLevel(logging.DEBUG)
        if(not otaLogger.hasHandlers()):
            handler = logging.handlers.RotatingFileHandler(logPath,maxBytes=50000,backupCount=10)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            otaLogger.addHandler(handler)
        return otaLogger
    def getLogger(self):
        logPath = os.environ.get("PYTHONPATH")+"/logs/ota.log"
        logger = self._prepareLogger(logPath,'OTALogger')
        return logger
    def getOutputLogger(self,logPath,loggerName):
        if(len(logPath) == 0):
            logPath = os.environ.get("PYTHONPATH")+"/output/ota.log"
        if(len(loggerName) == 0):
            loggerName = 'OTALogger'
        logger = self._prepareLogger(logPath,loggerName)
        return logger