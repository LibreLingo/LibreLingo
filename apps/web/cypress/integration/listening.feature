Feature: Listening exercise
  
  A challenge type where the user has to type the phrase they hear on an audio recording

  Scenario: Getting a listening challenge
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    Then listening challenge looks correct
    And I read "Type what you hear"
    And I see a panel with only a Skip, a Cancel, Can't listen now, and a disabled "Submit" button
    And I'm not able to submit
    And I see an input field
    And the input field is focused
    And the input field has a "Type your answer…" placeholder

  Scenario: Virtual keyboard for special characters
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    Then I see a virtual keyboard with 16 keys

  Scenario: Typing into the input field
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "asdfg"
    Then I see the challenge panel
    And I see a "Skip" button
    And I see an enabled "Submit" button
    And I see a "Can't listen now" button

  Scenario: Submitting incorrect answer
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "asdfg"
    And I click "Submit"
    Then I read "Incorrect solution"
    And I read "Correct answer: perro"
    And I see a "Continue" button
    
  Scenario: Submitting correct answer
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "perro"
    And I click "Submit"
    Then I read "Correct solution"
    And I see a "Continue" button

  Scenario: Submitting correct answer with a small typo
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "          pierro      "
    And I click "Submit"
    Then I read "You have a typo!"
    And I read "Correct spelling: perro"

  Scenario: Submitting correct answer with a small casing error
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "PerRo"
    And I click "Submit"
    Then I read "Correct solution!"
    And I don't read "Correct spelling: perro"

  Scenario: Going to the next challenge
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "perro"
    And I click "Submit"
    Then I don't see a "Skip" button
    And I click "Continue"
    Then I see a panel with only a Skip, Cancel, and a disabled "Submit" button

  Scenario: Going to the next challenge with keyboard only
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I type "perro"
    And I hit the enter key
    And I hit the enter key
    Then I see a panel with only a Skip, Cancel, and a disabled "Submit" button

  Scenario: Skipping all listening excercises
    Given I open "/course/test-1/skill/listening-test-0?testChallenge=cd183d15d4d1"
    And I see a "Skip" button
    And I see a "Can't listen now" button
    And I click "Can't listen now"
    Then I don't see a "Can't listen now" button
