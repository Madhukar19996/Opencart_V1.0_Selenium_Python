import logging
import os
from stat import filemode


# class LogGen():
#     @staticmethod
#     def loggen():
#         path = os.path.abspath(os.curdir) + '\\logs\\automation.log'
#         logging.basicConfig(filename="app.log", filemode="w",
#                             format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.DEBUG)
#         return logger

class logclass:
    def getthelogs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("logs\\automation.log",mode="w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

