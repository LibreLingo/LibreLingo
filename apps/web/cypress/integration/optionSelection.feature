Feature: Option selection challenge

  A challenge type where the user has to choose from multiple possible answers

  Scenario: Getting an option selection challenge
    Given I open "course/test-1/skill/options-test-0?testChallenge=5075bbb5a7df"
    Then I read "Which of these is"
    And I see 3 options
    And every option is inactive
    And I see a panel with only a Skip, Cancel and a disabled "Submit" button
    And option selection challenge looks correct

  Scenario: clicking an option
    Given I open "course/test-1/skill/options-test-0?testChallenge=5075bbb5a7df"
    And I select an option
    Then I see 2 inactive options
    And I see 1 active option
    And option selection challenge with first option selected looks correct

  Scenario: Submitting correct answer
    Given I open "course/test-1/skill/options-test-0?testChallenge=5075bbb5a7df"
    And I select the correct option
    And I click "Submit"
    Then I read "Correct solution"
    And I see a "Continue" button

  Scenario: Submitting incorrect answer
    Given I open "course/test-1/skill/options-test-0?testChallenge=5075bbb5a7df"
    And I select an incorrect option
    And I click "Submit"
    Then I read "Incorrect solution"
    And I read "Correct answer: perro"
    And I see a "Continue" button