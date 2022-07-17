from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import pytest

# Arrange
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        print("***************Launching Chrome Browser*************************") 
        desired_capabilities = DesiredCapabilities().CHROME.copy()
        desired_capabilities['acceptInsecureCerts']=True
        driver = webdriver.Chrome(executable_path="C:\Mahesh\Sources\PythonPractice\Drivers\chromedriver.exe",desired_capabilities=desired_capabilities)
        driver.implicitly_wait(1000)
        driver.maximize_window()
        return driver
    elif browser=='Firefox':
        print("***************Launching FireFox Browser*************************")
        desired_capabilities = DesiredCapabilities().FIREFOX.copy()
        desired_capabilities['acceptInsecureCerts']=True 
        driver = webdriver.Firefox(executable_path="C:\Mahesh\Sources\PythonPractice\Drivers\geckodriver.exe",desired_capabilities=desired_capabilities)
        driver.implicitly_wait(1000)
        driver.maximize_window()
        return driver
#This will get the value from CLI /hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

#This will return the browser value to setup method
@pytest.fixture()    
def browser(request):
    return request.config.getoption("--browser") 

########## Pytest HTML Report#########
# Hook to adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='CargoVision'
    config._metadata['Module Name']='Open Cases'
    config._metadata['Tested By']='Mahesh'
    
#Hook to Modify/Delete environment info to HTML Report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
    