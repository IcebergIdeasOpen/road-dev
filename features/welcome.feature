Feature: Welcome page

  As a user
  I want to be welcomed to the page
  So that I feel like a VIP

  Scenario: Correct welcome message
    Given I am on the welcome page
    Then I expect to see the correct welcome message

  Scenario: Looking for book recommendation
    Given Monique is on the welcome page
    When She selects the book recommendation button
    Then Monique see the book Extreme Programming Installed