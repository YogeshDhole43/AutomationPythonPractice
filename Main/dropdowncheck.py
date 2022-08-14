import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#driver = webdriver.Firefox(executable_path="C:\\Users\\YOGESH\\Downloads\\drivers\\gecko 0.30\\geckodriver.exe")
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
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

log = loginfuncheck()
log.loginbox()
log.passwordbox()
log.loginbutton()
log.loginverity()
log.title()
time.sleep(5)

class dropdown():
    def Admin(self):
        adminclk = driver.find_element(By.CSS_SELECTOR,"a[id='menu_admin_viewAdminModule'] b")
        adminclk.click()
        time.sleep(3)
    def ddselection(self):
        ddselect = driver.find_element(By.ID,"searchSystemUser_userType")
        dd = Select(ddselect)
        dd.select_by_visible_text("All")
        time.sleep(3)
        dd.select_by_visible_text("Admin")
        time.sleep(3)
        dd.select_by_visible_text("ESS")
        time.sleep(3)
        print("The dropdown test is passed")

drop = dropdown()
drop.Admin()
drop.ddselection()
driver.close()