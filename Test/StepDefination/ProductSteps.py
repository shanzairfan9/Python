import time

import pytest_bdd
from pytest_bdd import given, parsers, when
from pages.LoginPage import LoginPage
from pages.ProductPage import ProductPage

pytest_bdd.scenarios('C:\\Users\\shanza.irfan\\PycharmProjects\\pythonProject\\Test\\Features\\Product.Feature')


@pytest_bdd.when(pytest_bdd.parsers.parse('user enters username with "{username}"'))
def username(browser, username):
    LoginPage(browser).getUsername().send_keys(username)


@pytest_bdd.when(pytest_bdd.parsers.parse('user enters password with "{password}"'))
def password(browser, password):
    LoginPage(browser).getPassword().send_keys(password)


@when('user clicks on login button')
def loginButton(browser):
    LoginPage(browser).getLoginBtn().click()


@pytest_bdd.when(pytest_bdd.parsers.parse('user can Find the product with name "{product}"'))
def getProduct(browser, product):
    ProductPage(browser).getProductIsDisplayed(product)


@pytest_bdd.when(pytest_bdd.parsers.parse('user is able to select the product'))
def selectProduct(browser):
    ProductPage(browser).selectProduct().click()


@pytest_bdd.then(pytest_bdd.parsers.parse('Product detail page should appear with product "{product}"'))
def detailPage(browser, product):
    assert product == ProductPage(browser).assertDetailPage()


@pytest_bdd.then(pytest_bdd.parsers.parse('User is able to Click on Add cart Button'))
def addToCart(browser):
    ProductPage(browser).addToCart().click()


@pytest_bdd.then(pytest_bdd.parsers.parse('Validate the price of product is "{price}"'))
def validatePrice(browser, price):
    assert price == ProductPage(browser).ValidateProductPrice()


@pytest_bdd.then(pytest_bdd.parsers.parse('User can View cart'))
def viewCart(browser):
    ProductPage(browser).viewCart().click()


@pytest_bdd.then(pytest_bdd.parsers.parse('Remove the item from cart'))
def viewCart(browser):
    ProductPage(browser).removeFromCart().click()
