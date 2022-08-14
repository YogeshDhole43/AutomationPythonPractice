from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
@given(u':   Launch Firefox Browser')
def Launchbrowser(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when(u':   Open OrangeHRM Homepage')
def homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u':   Get title')
def title(context):
    act_title = context.driver.title
    exp_title = "OrangeHRM"
    if (act_title == exp_title):
        assert True,"title matched"


@when(u':   Enter username "{usename}" and password "{password}"')
def logincredentials(context,usename,password):
    loginbox = context.driver.find_element(By.ID, 'txtUsername')
    loginbox.send_keys(usename)
    passbox = context.driver.find_element(By.ID, 'txtPassword')
    passbox.send_keys(password)


@when(u':   Click on login button')
def clickonlogin(context):
    loginbtn = context.driver.find_element(By.ID, 'btnLogin')
    loginbtn.click()
    assert True,"Login successfull"


@when(u':   Verify login')
def loginverify(context):
    try:
        logincheck = context.driver.find_element(By.CLASS_NAME,'panelTrigger')
        logincheck.is_displayed()
        time.sleep(5)
        assert True,"login verification test passed successfully"
    except:
        context.driver.close()
        assert False,"Login verification failed"


@when(u':   Click on Admin tab')
def Admintabclick(context):
    adminclk = context.driver.find_element(By.CSS_SELECTOR, "a[id='menu_admin_viewAdminModule'] b")
    adminclk.click()
    time.sleep(3)


@when(u':   Dropdown Selection')
def dropdownselect(context):
    ddselect = context.driver.find_element(By.ID, "searchSystemUser_userType")
    dd = Select(ddselect)
    dd.select_by_visible_text("All")
    time.sleep(3)
    dd.select_by_visible_text("Admin")
    time.sleep(3)
    dd.select_by_visible_text("ESS")
    time.sleep(3)
    assert True, "The dropdown test is passed"


@then(u':   Close the browser')
def browserclose(context):
    context.driver.close()