from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time

user_name = "AdminSmiths"
password = "HighEnergy2020*"
desired_capabilities = DesiredCapabilities().CHROME.copy()
desired_capabilities['acceptInsecureCerts']=True
driver = webdriver.Chrome(executable_path="C:\Mahesh\Sources\PythonPractice\Drivers\chromedriver.exe",desired_capabilities=desired_capabilities)
driver.implicitly_wait(1000)
driver.maximize_window()
driver.get("https://cv.smithsdetection.com/")
element = driver.find_element("name","username")
element.send_keys(user_name)
element = driver.find_element("name","password")
element.send_keys(password)
driver.find_element("name","login").click()
time.sleep(20)
driver.find_element("xpath","//div[@class='info-container']").click()
driver.find_element("xpath","//span[text()='Log out']").click()
driver.find_element("xpath","//button[text()='OK']").click()
#driver.close()