import time
from selenium.webdriver.common.by import By
from Utils.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, browser):
        self.browser = browser

    userName = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    explore = (By.XPATH, "(//*[contains(text(),'Explore')])[2]")
    product = (By.XPATH, "//span[contains(text(),'Products')]")
    page_title = (By.XPATH, "//div[contains(text(),'Swag Labs')]")
    errorMsg = (By.XPATH, '//div[@class="error-message-container error"]//h3')

    def getUrl(self):
        return self.browser.get("https://www.saucedemo.com/")

    def getUsername(self):
        return self.browser.find_element(*LoginPage.userName)

    def getPassword(self):
        return self.browser.find_element(*LoginPage.password)

    def getLoginBtn(self):
        return self.browser.find_element(*LoginPage.login_btn)

    def get_page_title_text(self):
        return self.browser.find_element(*self.page_title).text

    def get_error_text(self):
        time.sleep(2)
        return self.browser.find_element(*self.errorMsg).text
