from selenium import webdriver
import threading
import time
from selenium.webdriver import DesiredCapabilities
desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts']=True

class Test_Login:
    baseURL="https://cv.smithsdetection.com/"
    username="AdminSmiths"
    password="HighEnergy2020*"
    
    def test_homePageTitle(self):
      self.driver = webdriver.Chrome(executable_path="C:\Mahesh\Sources\PythonPractice\Drivers\chromedriver.exe",desired_capabilities=desired_capabilities)
      self.driver.implicitly_wait(1000)
      self.driver.get(self.baseURL)
      self.driver.maximize_window()

      element = self.driver.find_element("name","username")
      element.send_keys(self.username)
      element = self.driver.find_element("name","password")
      element.send_keys(self.password)
      element = self.driver.find_element("name","login")
      element.click()
#driver.get("https://cv.smithsdetection.com/")
#driver.maximize_window()
#driver.fi
#print(driver.title)

#driver.close()

#FROM FIREFOX DRIVER
#driver = webdriver.Firefox(GeckoDriverManager().install(),options=options)
#driver.get("https://cv.smithsdetection.com/")
#driver.maximize_window()
#time.sleep(5)
#print(driver.title)
#driver.close()#