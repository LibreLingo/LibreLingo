Feature: Cancel button in a practice session

  Scenario: Getting a short text input challenge
    Given I open "/course/test/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I click the "Cancel" button
    Then I should be on "/course/test"
    # Test that the progress has been recorded
    # Later add a window to confirm the user wants to cancel and if s/he wants to save the progress or not.
