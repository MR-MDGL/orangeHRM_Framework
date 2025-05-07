



import os
from configparser import ConfigParser

utility_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(utility_dir, os.pardir))
config_path = os.path.join(project_root, 'configuration', 'config.ini')

config = ConfigParser()
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        return config.get('commonInfo', 'URL')

    @staticmethod
    def getUsername():
        return config.get('commonInfo', 'USERNAME')

    @staticmethod
    def getPassword():
        return config.get('commonInfo', 'PASSWORD')
