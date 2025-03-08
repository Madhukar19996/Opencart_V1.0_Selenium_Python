import time

import allure
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import logclass
import os


@allure.title("Verify that Opencart Login Account Testing")
@allure.description("TC_005  TestCase- Login  with Valid data and Invalid data verify whether user log-in successfully ")
@allure.feature("Opencart Login with Valid and Invalid Credentials")
@pytest.mark.DataDrivenTesting
class Test_Login_DDT(logclass):



    path = os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"

    def test_login_ddt(self,setup):
        log = self.getthelogs()
        log.info("**** Starting test_005_login_Datadriven *******")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(os.getenv("BASE_URL"))
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)  # HomePage Page Object Class
        self.lp = LoginPage(self.driver)  # LoginPage Page Object Class
        self.ma = MyAccountPage(self.driver)  # MyAccount Page Object class

        for r in range(2,self.rows+1):
            time.sleep(2)
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExists()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    time.sleep(1)
                    self.ma.clickLogout()
                    time.sleep(1)
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        log.info("******* End of test_005_login_Datadriven **********")
