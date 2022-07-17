import time
class LoginPage:
    textbox_username="username"
    textbox_password="password"
    button_signin="login"
    button_accountname="//div[@class='info-container']"
    button_logout="//span[text()='Log out']"
    button_closeDialogueOKBtn="//button[text()='OK']"
    
    def __init__(self,driver):
        self.driver=driver
    
    def setUserName(self,username):
        UserName=self.driver.find_element("name",self.textbox_username)
        UserName.clear()
        UserName.send_keys(username)
        
    def setPassword(self,password):
        PassWord=self.driver.find_element("name",self.textbox_password)
        PassWord.clear()
        PassWord.send_keys(password)
        
    def clickSignIn(self):
        SignIn=self.driver.find_element("name",self.button_signin)
        SignIn.click()
        
    def clickSignout(self):
        accountName=self.driver.find_element("xpath",self.button_accountname)
        accountName.click()
        logOut=self.driver.find_element("xpath",self.button_logout)
        logOut.click()
        time.sleep(5)
        okButton=self.driver.find_element("xpath",self.button_closeDialogueOKBtn)
        okButton.click()