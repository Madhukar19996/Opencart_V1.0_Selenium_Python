import utilities.currentDatetime
from utilities.randomString import random_string_generator
from utilities.currentDatetime import take_current_time
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import logclass
import time
import allure
import pytest
from utilities.screenshots import take_screen_shot
from dotenv import load_dotenv
import os




class Test_Login(logclass):
    load_dotenv()

    @allure.title("Verify that Opencart Login Account Testing")
    @allure.description("TC_003 Positive TestCase- Login  with Valid data and verify whether user log-in successfully ")
    @allure.feature("Opencart Login with Valid Credentials")
    @pytest.mark.login


    def test_login(self, setup):
        log = self.getthelogs()
        log.info("******* Starting test_002_login **********")
        self.driver = setup
        self.driver.get(os.getenv("BASE_URL"))
        self.driver.maximize_window()
        time.sleep(2)

        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()


        self.lp = LoginPage(self.driver)
        self.lp.setEmail(os.getenv("EMAIL_001_OC"))
        self.lp.setPassword(os.getenv("PASSWORD_001_OC"))
        self.lp.clickLogin()

        self.target_page=self.lp.isMyAccountPageExists()

        if self.target_page:
            time.sleep(2)
            # take_screen_shot(driver=driver, name="My Account is created")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login_successfully" +utilities.currentDatetime.take_current_time()+".png")
            take_screen_shot(driver=self.driver, name="test_login_successfully.png")



            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login_error"+utilities.currentDatetime.take_current_time()+".png")
            take_screen_shot(driver=self.driver, name="test_login_error.png")

            assert False


        log.info("******* End of test_003_login **********")
        self.driver.close()
