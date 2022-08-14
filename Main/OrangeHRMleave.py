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

class leave():
    def leavetabclick(self):
        leavetab = driver.find_element(By.XPATH,"//b[normalize-space()='Leave']")
        leavetab.click()
        time.sleep(3)
    def leavereportclick(self):
        leavereport = driver.find_element(By.ID,"menu_leave_Reports")
        leavereport.click()
        time.sleep(3)
    def generatereport(self):
        genreport = driver.find_element(By.ID,"menu_leave_viewLeaveBalanceReport")
        genreport.click()
        time.sleep(2)
    def generatereportdropdown(self):
        dropdown = driver.find_element(By.NAME,"leave_balance[report_type]")
        gendropdown = Select(dropdown)
        gendropdown.select_by_visible_text("Leave Type")
        time.sleep(2)
    def viewbtn(self):
        btn = driver.find_element(By.ID,"viewBtn")
        btn.click()
        print("report list displayed")

log = loginfuncheck()
log.loginbox()
log.passwordbox()
log.loginbutton()
log.loginverity()
log.title()

l = leave()
l.leavetabclick()
l.leavereportclick()
l.generatereport()
l.generatereportdropdown()
l.viewbtn()

driver.close()