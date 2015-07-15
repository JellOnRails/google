Feature: Search
  In order get some information
  As a User
  I want to find particular info

  Scenario: Search for artist
    Given I am on search page
    When Search for Red Hot Chili Peppers text
    Then Search result should contain Red Hot Chili Peppers link on 3 position
    When Search for Nick Cave text
    Then Search result should contain Nick Cave link on 4 position
    And Search result should not contain Red Hot Chili Peppers link on 5 position