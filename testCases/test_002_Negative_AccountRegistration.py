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
    @allure.description("TC2 - Negative TestCase - Fill the registration form with Inalid data and verify whether account created or Not")
    @allure.feature("Opencart Registration with Inalid Credentials")
    @pytest.mark.Negative
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
        # self.email =random_string_generator() + 'pandey@gmail.com'

        self.regpage.setEmail("madhukar1232")
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
        time.sleep(2)



        self.confmsg = self.regpage.getconfirmationmsg()
        time.sleep(2)


        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg_with_invalid_data.png")
        take_screen_shot(driver=driver, name="OpencartRegistractionFailed")
        self.driver.close()




        if self.confmsg == "Account Has Been Created!":
            take_screen_shot(driver=driver, name="OpencartRegistractionFailed")
            assert True
        else:

            assert False
            take_screen_shot(driver=driver, name="OpencartRegistractionFailed")

