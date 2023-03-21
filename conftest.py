import pytest
from pytest import fixture
from selenium import webdriver


@fixture(scope='class')
def chrome_browser():
    driver = webdriver.Chrome(executable_path='../chromeDriver/chromedriver.exe')
    yield driver
    driver.quit()


@fixture(scope='module')
def browser():
    driver = webdriver.Chrome(executable_path='../chromeDriver/chromedriver.exe')
    yield driver
    driver.quit()
