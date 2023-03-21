from selenium.webdriver.common.by import By


class TenPearlsUniversityPage:

    def __init__(self, driver):
        self.driver = driver

    userName = (By.ID, "inputUsername")
    password = (By.ID, "inputPassword")
    login_btn = (By.XPATH, "//button[@type='submit']")
    explore = (By.XPATH, "(//*[contains(text(),'Explore')])[2]")

    def getName(self):
        return self.driver.find_element(*TenPearlsUniversityPage.userName)

    def getPassword(self):
        return self.driver.find_element(*TenPearlsUniversityPage.password)

    def getLoginBtn(self):
        return self.driver.find_element(*TenPearlsUniversityPage.login_btn)

    def getExploreOption(self):
        return self.driver.find_element(*TenPearlsUniversityPage.explore)
