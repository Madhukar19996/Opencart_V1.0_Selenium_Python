import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser=='edge':
     driver = webdriver.Edge()
     print("Lauching Edge Browser")

    elif browser=="firefox":
        driver=webdriver.Firefox()
        print("Launching the Firefox Browser")

    else:
        driver = webdriver.Chrome()
        print("Launching the Chrome Browser")



    return driver




def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Madhukar Pandey'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
