from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@given(u':   Browser launch')
def launch_Firefox_Browser(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()


@when(u':   Go to homepage of OrangeHRM')
def Openurl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    context.driver.implicitly_wait(5)


@when(u':   Enter valid username "Admin" and password "admin123"')
def login_Credentials(context):
    loginbox = context.driver.find_element(By.ID, 'txtUsername')
    loginbox.send_keys("Admin")
    passbox = context.driver.find_element(By.ID, 'txtPassword')
    passbox.send_keys("admin123")


@when(u':   login')
def login(context):
    loginbtn = context.driver.find_element(By.ID, 'btnLogin')
    loginbtn.click()


@when(u':   login validation')
def login_Check(context):
    logincheck = context.driver.find_element(By.CLASS_NAME, 'panelTrigger')
    logincheck.is_displayed()
    print("log in successfully")


@when(u': Click on my info tab')
def myinfo_tab(context):
    myinfotab = context.driver.find_element(By.CSS_SELECTOR, "a[id='menu_pim_viewMyDetails'] b")
    myinfotab.click()
    time.sleep(3)


@when(u': Get name of employee')
def emp_name(context):
    text = context.driver.find_element(By.XPATH, "//h1[normalize-space()='Manoj c']")
    text.text
    print(text)


@when(u': Click on leave tab')
def leave_Tab(context):
    leavetab = context.driver.find_element(By.XPATH, "//b[normalize-space()='Leave']")
    leavetab.click()
    time.sleep(3)


@when(u': Click on leave report')
def leave_report(context):
    leavereport = context.driver.find_element(By.ID, "menu_leave_Reports")
    leavereport.click()
    time.sleep(3)


@when(u': Click on generate leave report')
def generate_report(context):
    genreport = context.driver.find_element(By.ID, "menu_leave_viewLeaveBalanceReport")
    genreport.click()
    time.sleep(2)


@when(u': Click on generate report dropdown')
def report_dropdown(context):
    dropdown = context.driver.find_element(By.NAME, "leave_balance[report_type]")
    gendropdown = Select(dropdown)
    gendropdown.select_by_visible_text("Leave Type")
    time.sleep(2)


@when(u': Click on view button')
def view_btn(context):
    btn = context.driver.find_element(By.ID, "viewBtn")
    btn.click()
    print("report list displayed")


@when(u': Click on recruitment tab')
def recruitment_tab(context):
    recruitmenttab = context.driver.find_element(By.CSS_SELECTOR, "a[id='menu_recruitment_viewRecruitmentModule'] b")
    recruitmenttab.click()
    time.sleep(3)


@when(u': Click on Candidate tab')
def candidate_tab(context):
    candidatetab = context.driver.find_element(By.ID, "menu_recruitment_viewCandidates")
    candidatetab.click()
    print("Candidate list")


@then(u': Browser close')
def browseroff(context):
    context.driver.close()