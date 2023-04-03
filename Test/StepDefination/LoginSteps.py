import pytest_bdd
from pytest_bdd import given, parsers, when
from pages.LoginPage import LoginPage

pytest_bdd.scenarios('C:\\Users\\shanza.irfan\\PycharmProjects\\pythonProject\\Test\\Features\\Login.Feature')


@pytest_bdd.when(pytest_bdd.parsers.parse('user enters username with "{username}"'))
def username(browser, username):
    LoginPage(browser).getUsername().send_keys(username)


@pytest_bdd.when(pytest_bdd.parsers.parse('user enters password with "{password}"'))
def password(browser, password):
    LoginPage(browser).getPassword().send_keys(password)


@when('user clicks on login button')
def loginButton(browser):
    LoginPage(browser).getLoginBtn().click()


@pytest_bdd.then(pytest_bdd.parsers.parse('user should Land on homepage and Homepage title should be "{pageTitle}"'))
def assertPageTitle_impl(browser, pageTitle):
    assert pageTitle == LoginPage(browser).get_page_title_text()


@pytest_bdd.then(pytest_bdd.parsers.parse('user should get an error msg "{errorMsg}"'))
def assertInvalidLogin(browser, errorMsg):
    assert errorMsg == LoginPage(browser).get_error_text()


