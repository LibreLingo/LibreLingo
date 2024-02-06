Feature: Skipping a challenge

  Each challenge should come with a skip button. Pressing the skip button postpones the challenge for later.

  Scenario: Skip button is visible
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=5000997897bb"
    Then I should not have progressed
    Then I see a "Skip" button

  Scenario: Skipping a challenge
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=5000997897bb"
    When I click "Skip"
    Then I should have progressed
