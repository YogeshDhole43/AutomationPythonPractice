import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)
class loginfuncheck():
    def loginbox(self):
        loginbox = driver.find_element(By.ID,'txtUsername')
        loginbox.send_keys("Admin")
    def passwordbox(self):
        passbox = driver.find_element(By.ID,'txtPassword')
        passbox.send_keys("admin123")
    def loginbutton(self):
        loginbtn= driver.find_element(By.ID,'btnLogin')
        loginbtn.click()
    def loginverity(self):
        logincheck = driver.find_element(By.CLASS_NAME,'panelTrigger')
        welcomemsg = logincheck.is_displayed()
        print("log in successfully")
    def title(self):
        act_title = driver.title
        exp_title = "OrangeHRM"
        if (act_title == exp_title):
            print("Title mached")
        time.sleep(3)
class myinfo():
    def myinfoclick(self):
        myinfotab = driver.find_element(By.CSS_SELECTOR,"a[id='menu_pim_viewMyDetails'] b")
        myinfotab.click()
        time.sleep(3)
    def gettext(self):
        text = driver.find_element(By.XPATH,"//h1[normalize-space()='Manoj c']")
        text.text
        print(text)

log = loginfuncheck()
log.loginbox()
log.passwordbox()
log.loginbutton()
log.loginverity()
log.title()

info = myinfo()
info.myinfoclick()
info.gettext()

driver.close()