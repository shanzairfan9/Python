Feature:  Login


  Background:
    Given user on the Login Page

  Scenario: Verification of Login with valid Credentials
    When user enters username with "standard_user"
    And user enters password with "secret_sauce"
    And user clicks on login button
    Then user should Land on homepage and Homepage title should be "Swag Labs"


  Scenario: Verification of Login with Invalid username
    When user enters username with "standard_usersss"
    And user enters password with "secret_sauce"
    And user clicks on login button
    Then user should get an error msg "Epic sadface: Username and password do not match any user in this service"



  Scenario: Verification of Login with Invalid password
    When user enters username with "standard_user"
    And user enters password with "secret_sauceswww"
    And user clicks on login button
    Then user should get an error msg "Epic sadface: Username and password do not match any user in this service"


  Scenario Outline: Verification of Login multiple accounts
    When user enters username with <username>
    And user enters password with <password>
    And user clicks on login button
    Then user should Land on homepage and Homepage title should be "Swag Labs"
      Examples:
    | username        | password     |
    | standard_user   | secret_sauce |
    | locked_out_user | secret_sauce |
    | problem_user    | secret_sauce |