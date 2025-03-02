from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.HomePage import HomePage
from utilities.randomString import random_string_generator
import time
import allure
import pytest
from dotenv import load_dotenv
import os
from utilities.screenshots import take_screen_shot

class Test_001_AccountReg:
    load_dotenv()

    @allure.title("Verify that Opencart Registration Account Testing")
    @allure.description("TC_001 - Positive TestCase - Fill the registration form with Valid data and verify whether account created ")
    @allure.feature("Opencart Registration with Valid Credentials")
    @pytest.mark.Positive
    def test_account_reg(self, setup):
        self.driver = setup
        driver=self.driver
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
        self.email =random_string_generator() + 'pandey@gmail.com'

        self.regpage.setEmail(self.email)
        take_screen_shot(driver=driver, name="Random E-mail is Generated")


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
        time.sleep(2)


        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg.png")
        take_screen_shot(driver=driver, name="OpencartRegistractionPassed")
        self.driver.close()




        if self.confmsg == "Your Account Has Been Created!":
            assert True
        else:

            assert False

