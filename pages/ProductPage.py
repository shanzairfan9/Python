import time
from selenium.webdriver.common.by import By
from Utils.BaseClass import BaseClass


class ProductPage(BaseClass):

    def __init__(self, browser):
        self.browser = browser

    product = (By.XPATH, "//div[contains(text(),'Sauce Labs Backpack')]")
    getProduct = (By.XPATH, "//*[@id='item_4_title_link']/div")
    addToCartBtn = (By.XPATH, "//Button[contains(text(),'Add to cart')]")
    productPrice = (By.XPATH, "//div[@class='inventory_details_price']")
    viewCartBtn = (By.XPATH, '//div[@Id="shopping_cart_container"]')
    removeBtn = (By.XPATH, "//Button[contains(text(),'Remove')]")

    def getProductIsDisplayed(self, product):
        return self.browser.find_element(By.XPATH, "//div[contains(text(),'" + product + "')]").is_displayed()

    def selectProduct(self):
        return self.browser.find_element(*self.getProduct)

    def selectProduct(self):
        return self.browser.find_element(*self.getProduct)

    def assertDetailPage(self):
        return self.browser.find_element(*self.product).text

    def addToCart(self):
        return self.browser.find_element(*self.addToCartBtn)

    def ValidateProductPrice(self):
        return self.browser.find_element(*self.productPrice).text

    def viewCart(self):
        return self.browser.find_element(*self.viewCartBtn)

    def removeFromCart(self):
        return self.browser.find_element(*self.removeBtn)
