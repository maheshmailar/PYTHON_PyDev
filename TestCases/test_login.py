import pytest
from selenium import webdriver   
from PageObjects.LoginPage import LoginPage
from Util.readProperties import ReadConfig
from Util.customLogger import LogGen

class Test_Login:
    baseURL=ReadConfig.gettAppUrl()
    username=ReadConfig.gettUserName()
    password=ReadConfig.gettPassword()
    logger = LogGen.loggen()
     
    @pytest.mark.regression   
    def test_homePageTitle(self,setup):
        self.logger.info("*********** Test_Login test execution started****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title      
        if act_title=="Login123":
            assert True        
            self.driver.close()
            self.logger.info("*********** Test_Login execution Passed ****************************")    
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********** Test_Login execution Failed ****************************")   
            assert False
        self.logger.info("*********** Test_Login execution Ended ****************************")   
        
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_UserManagement(self,setup):
        self.logger.info("*********** Test_UserManagement test execution started****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        act_title=self.driver.title
       
        if act_title=="Operations Management":
            assert True
            self.driver.close()
            self.logger.info("*********** Test_UserManagement execution Passed ****************************") 
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_UserManagement.png")
            self.driver.close()
            self.logger.error("*********** Test_UserManagement execution Failed ****************************") 
            assert False
        self.logger.info("*********** Test_UserManagement execution Ended ****************************")