Feature:  Product

  Background:
    Given user on the Login Page

  Scenario: User is should be able to Find product and Add to Cart
    When user enters username with "standard_user"
    And user enters password with "secret_sauce"
    And user clicks on login button
    And user can Find the product with name "Sauce Labs Backpack"
    And user is able to select the product
    Then Product detail page should appear with product "Sauce Labs Backpack"
    And User is able to Click on Add cart Button
    And Validate the price of product is "$29.99"

  Scenario: User is should be able to Remove From Cart
    When user enters username with "standard_user"
    And user enters password with "secret_sauce"
    And user clicks on login button
    And user can Find the product with name "Sauce Labs Backpack"
    And user is able to select the product
    Then Product detail page should appear with product "Sauce Labs Backpack"
    And User is able to Click on Add cart Button
    And Validate the price of product is "$29.99"
    And User can View cart
    And Remove the item from cart
