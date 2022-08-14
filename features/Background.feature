Feature: Check details present on OrangeHRM

  Background: common methods
    Given :   Browser launch
    When  :   Go to homepage of OrangeHRM
    And   :   Get title
    And   :   Enter valid username "Admin" and password "admin123"
    And   :   login
    And   :   login validation

  Scenario: My Information Check
    When : Click on my info tab
    And  : Get name of employee
    Then : Browser close

  Scenario: My Leave Check
    When : Click on leave tab
    And  : Click on leave report
    And  : Click on generate leave report
    And  : Click on generate report dropdown
    And  : Click on view button
    Then : Browser close

  Scenario: Recruitment Details Check
    When : Click on recruitment tab
    And  : Click on Candidate tab
    Then : Browser close