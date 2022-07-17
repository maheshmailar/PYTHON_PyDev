import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\Config.ini")

class ReadConfig:
    @staticmethod
    def gettAppUrl():
        url=config.get('login','baseURL')    
        return url  
  
    @staticmethod
    def gettUserName():
        username=config.get('login','username')
        return username
    
    @staticmethod
    def gettPassword():
        password=config.get('login','password')
        return password   