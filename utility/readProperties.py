# import os
# from configparser import ConfigParser
#
# cwd = os.path.abspath(os.path.join(os.getcwd(), os.pardir))  # Go one level up from 'utility'
# config = ConfigParser()
# config_path = os.path.join(cwd, 'configuration', 'config.ini')
#
# if not os.path.exists(config_path):
#     print(f"Config file not found at: {config_path}")
# else:
#     print(f"Config file found at: {config_path}")
#
# config.read(config_path)
# print(f"Sections found: {config.sections()}")
#
# class ReadConfig:
#     @staticmethod
#     def getApplicationURL():
#         return config.get('commonInfo', 'URL')
#
#     @staticmethod
#     def getUsername():
#         return config.get('commonInfo', 'USERNAME')
#
#     @staticmethod
#     def getPassword():
#         return config.get('commonInfo','PASSWORD')
#
# # ob = ReadConfig()
# # print(ob.getApplicationURL())
# # print(ob.getUsername())
# # print(ob.getPassword())




import os
from configparser import ConfigParser

# Get the directory of this file (utility folder)
utility_dir = os.path.dirname(os.path.abspath(__file__))
# Go one level up to the project root
project_root = os.path.abspath(os.path.join(utility_dir, os.pardir))
# Build the correct path to the config file
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
