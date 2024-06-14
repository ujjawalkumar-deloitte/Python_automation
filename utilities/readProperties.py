import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common_info','baseURL')
        return url

    @staticmethod
    def getfirstName():
        firstName=config.get('common_info','firstName')
        return firstName

    @staticmethod
    def getlastName():
        lastName=config.get('common_info','lastName')
        return lastName
    
    @staticmethod
    def getEmail():
        email=config.get('common_info','email')
        return email
    
    @staticmethod
    def gettelephone():
        telephone=config.get('common_info','telephone')
        return telephone
    
    @staticmethod
    def getPassword():
        password=config.get('common_info','password')
        return password
    
    @staticmethod
    def getConfirmPassword():
        password=config.get('common_info','confirmPassword')
        return password
