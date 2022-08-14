import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

class recruitment():
    def recclick(self):
        recruitmenttab = driver.find_element(By.CSS_SELECTOR,"a[id='menu_recruitment_viewRecruitmentModule'] b")
        recruitmenttab.click()
        time.sleep(3)
    def candidate(self):
        candidatetab = driver.find_element(By.ID,"menu_recruitment_viewCandidates")
        candidatetab.click()
        print("Candidate list")

log = loginfuncheck()
log.loginbox()
log.passwordbox()
log.loginbutton()
log.loginverity()
log.title()

rec = recruitment()
rec.recclick()
rec.candidate()

driver.close()