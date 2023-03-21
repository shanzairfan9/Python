import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.TenPearlsUniversityPage import TenPearlsUniversityPage


class TestCases:
    def test_assertPageTitle(self, chrome_browser):
        chrome_browser.get("https://pulse.10pearls.com/#/login")
        page_title = chrome_browser.title
        print(page_title)
        assert "Pulse - 10Pearls" in page_title

    def test_ClickOnSignIn(self, chrome_browser):
        chrome_browser.get("https://pulse.10pearls.com/#/login")
        chrome_browser.find_element(By.ID, "inputUsername").send_keys("I am able to automate")
        chrome_browser.find_element(By.ID, "inputPassword").send_keys("password")
        chrome_browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    def test_moduleLevelFixture1(self, browser):
        browser.get("https://www.udemy.com/")

    def test_moduleLevelFixture2(self, browser):
        browser.get("https://www.office.com/")

    def test_moduleLevelFixture3(self, browser):
        browser.get("https://www.youtube.com/")
