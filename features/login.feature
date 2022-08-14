Feature: Logintest
  Background: common methods

  Scenario: To check the login functionality
    Given :   Launch Firefox Browser
    When  :   Open OrangeHRM Homepage
    And   :   Get title
    And   :   Enter username "Admin" and password "admin123"
    And   :   Click on login button
    And   :   Verify login
    Then  :   Close the browser

  Scenario Outline: To check the login functionality with multiple data
    Given :   Launch Firefox Browser
    When  :   Open OrangeHRM Homepage
    And   :   Get title
    And   :   Enter username "<Username>" and password "<Password>"
    And   :   Click on login button
    And   :   Verify login
    Then  :   Close the browser

    Examples:

        | Username  | Password  |
        | Admin     | admin123  |
        | Admin     | adm3      |
        | Ad        | admin123  |

  Scenario: Dropdown Functionality Check
    Given :   Launch Firefox Browser
    When  :   Open OrangeHRM Homepage
    And   :   Enter username "Admin" and password "admin123"
    And   :   Click on login button
    And   :   Verify login
    And   :   Click on Admin tab
    And   :   Dropdown Selection
    Then  :   Close the browser
