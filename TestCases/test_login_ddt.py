import pytest
from selenium import webdriver   
from PageObjects.LoginPage import LoginPage
from Util.readProperties import ReadConfig
from Util.customLogger import LogGen
from Util import XLUtil
import time
from selenium.webdriver import DesiredCapabilities

class Test_ddt_Login:
    baseURL=ReadConfig.gettAppUrl()
    path=".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()
    
    @pytest.mark.regression
    def test_UserManagement(self,setup):
        self.logger.info("*********** Test_ddt_Login test execution started***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtil.getRowCount(self.path, 'Sheet1')
        print("Print No of rows in excel:",self.rows)
        lst_status=[]#Empty list variables
        
        for r in range(2,self.rows+1):
            self.user=XLUtil.readData(self.path, 'Sheet1', r, 1)
            self.password=XLUtil.readData(self.path, 'Sheet1', r, 2)
            self.exp=XLUtil.readData(self.path, 'Sheet1', r, 3)
            
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickSignIn()
            time.sleep(5)
            act_title=self.driver.title
       
            if act_title=="Operations Management":
                if self.exp=="Pass":
                    self.logger.info("***Passed")
                    self.lp.clickSignout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.error("***Failed")
                    self.lp.clickSignout()
                    lst_status.append("Fail")
            elif act_title!="Operations Management":
                if self.exp=="Pass":
                    self.logger.error("***Failed")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("***Passed")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("****Login DDT test passed***")
            self.driver.close()
            assert True
        else:
            self.logger.info("****Login DDT test failed***")
            self.driver.close()
            assert False
            
        self.logger.info("****End OF DDT TEST***")
        self.logger.info("Completed Login test")