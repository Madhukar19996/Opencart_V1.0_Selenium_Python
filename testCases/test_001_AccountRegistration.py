from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities.randomString import random_string_generator
import time
import allure
import pytest
from dotenv import load_dotenv
import os


class Test_001_AccountReg:
    load_dotenv()

    @allure.title("Verify that Opencart Registration Account Testing")
    @allure.description("TC1 - Positive TestCase - Fill the registration form with Valid data and verify whether account created ")
    @pytest.mark.Positive
    def test_account_reg(self, setup):
        self.driver = setup
        self.driver.get(os.getenv("BASE_URL"))

        self.driver.maximize_window()
        time.sleep(2)

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        self.regpage = AccountRegistrationPage(self.driver)

        # self.driver.execute_script("document.body.style.zoom='90%'")



        self.regpage.setFirstName(os.getenv("NAME_001_OC"))
        time.sleep(1)
        self.regpage.setLastName(os.getenv("LAST_NAME_001_OC"))
        time.sleep(1)
        self.email =random_string_generator() + '@gmail.com'

        self.regpage.setEmail(self.email)
        time.sleep(1)
        self.regpage.setTelephone(os.getenv("TELEPHONE_001_OC"))
        time.sleep(1)
        self.regpage.setPassword(os.getenv("PASSWORD_001_OC"))
        time.sleep(1)
        self.regpage.setConfirmPassword(os.getenv("CONFIRM_PASSWORD_001_OC"))
        time.sleep(1)
        self.regpage.setPrivacyPolicy()
        time.sleep(1)
        self.regpage.clickContinue()
        time.sleep(1)
        self.confmsg = self.regpage.getconfirmationmsg()
        time.sleep(1)

        self.driver.close()

        if self.confmsg == "Your Account Has Been Created!":
            assert True
        else:
            assert False
