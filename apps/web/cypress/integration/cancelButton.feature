Feature: Cancel button in a practice session

  Scenario: Getting a short text input challenge
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I click "Cancel"
    Then I should be on "/course/test-1"
    # Test that the progress has been recorded
    # Later add a window to confirm the user wants to cancel and if s/he wants to save the progress or not.

  Scenario: I am redirected back to the matching course page
    Given I open "/course/test-2/skill/animals"
    And I click "Cancel"
    Then I should be on "/course/test-2"
