# from selenium.webdriver.common.by import By
#
#
# class MyAccountPage():
#
#     MyAccount_xpath = "//span[normalize-space()='My Account']"
#     logout_xpath="//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Logout']"
#     account_logout_continue_xpath="//a[normalize-space()='Continue']"
#
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def clickMyAccount(self):
#         self.driver.find_element(By.XPATH,self.MyAccount_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element(By.XPATH,self.logout_xpath).click()
#     def clickAccountLogoutContinue(self):
#         self.driver.find_element(By.XPATH, self.account_logout_continue_xpath).click()
from selenium.webdriver.common.by import By


class MyAccountPage():

    lnk_logout_xpath = "//aside[@id='column-right']//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()
