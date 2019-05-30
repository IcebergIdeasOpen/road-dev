Feature: Lost and Found Pets

  Scenario: Report a lost pet
    Given I have a pet
    When my pet is lost
    Then I should be able to report that my pet is lost

  Scenario: Upload Photo And Display Text
    Given Report a lost pet page
    When I upload a photo and enter "My Dog Fido"
      Then A photo appears on the page
    And the text should read "My Dog Fido is missing"

  Scenario:
    Given Luis dog is not at home
    And it has been a day since Luis has seen him
    When Luis upload a photo of my dog
    Then Luis should see his dog on the missing dog list

  Scenario: Reporting a lost dog
    Given Anna has lost her dog
    When she visits the lost pet submission page
    And she submits a photo
    And she enters the last known location of her dog
    Then Anna can see her dogs photo
    And marked on a map at it's last known location

  Scenario: Report a found pet

#  Scenario: Pet matches pet in found listing




