from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service
# -- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import Rating


def browser():
    driver = webdriver.Chrome(executable_path='../chromeDriver/chromedriver.exe')
    driver.get("https://pulse.10pearls.com/#/login")
    page_title = driver.title
    print(page_title)
    assert "Pulse - 10Pearls" in page_title
    driver.quit()


if __name__ == '__main__':
    browser()
