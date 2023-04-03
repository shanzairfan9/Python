import json
import pytest
import selenium
import selenium.webdriver
import selenium.webdriver
from pytest_bdd import given
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None
swagUrl = 'https://www.saucedemo.com/'


@pytest.fixture(scope='session')
def config(scope='session'):
    # Read the file
    with open('D:\pythonProjectTAU\config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture(scope='session')
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = webdriver.Chrome(executable_path='../chromeDriver/chromedriver.exe')
        b.maximize_window()

    elif config['browser'] == 'Headless Chrome':
        options = Options()
        options.headless = True
        b = webdriver.Chrome('../chromeDriver/chromedriver.exe', options=options)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the cleanup
    b.quit()


@given("user on the Login Page")
def getUrl(browser):
    browser.get(swagUrl)
