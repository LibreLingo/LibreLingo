Feature: Short text input challange

  A challange type where the user has to translate a short phrase

  Scenario: Getting a short text input challenge
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    Then short text input challenge looks correct
    And I read "Type"
    And I read "dog"
    And I read "in Test Language!"
    Given I open "/course/test-1/skill/short-input-test-1?testChallenge=fc0a3426d589"
    Then I see a tooltip that says "foo"
    And I see a panel with only a Skip, Cancel and a disabled "Submit" button
    And I'm not able to submit
    And I see a card with an image
    And I see an input field
    And the input field is focused
    And the input field has a "Type your answer…" placeholder
    
  Scenario: Virtual keyboard for special characters
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    Then I see a virtual keyboard with 16 keys
    And the keys on the virtual keyboard have proper labels
    And clicking on a key types into the input field
    Given I submit solution
    Then I don't see a virtual keyboard anymore

  Scenario: Typing into the input field
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "el perro"
    Then I see the challenge panel
    And I see a "Skip" button
    And I see an enabled "Submit" button
    
  Scenario: Submitting incorrect answer
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "asdfg"
    And I click "Submit"
    Then I read "Incorrect solution"
    And I read "Correct answer: perro"
    And I see a "Continue" button
    
  Scenario: Submitting correct answer
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "perro"
    And I click "Submit"
    Then I read "Correct solution"
    And I see a "Continue" button

  Scenario: Submitting alternative correct answer
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "can"
    And I click "Submit"
    Then I read "Correct solution"
    And I see a "Continue" button

  Scenario: Submitting alternative correct answer
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "el perro"
    And I click "Submit"
    Then I read "Correct solution"

  Scenario: Submitting correct answer with a small typo
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "      el      pierro      "
    And I click "Submit"
    Then I read "You have a typo!"
    And I read "Correct spelling: el perro"

  Scenario: Submitting correct answer with a small casing error
    Given I open "/course/test-1/skill/short-input-test-0?testChallenge=14fc2ae4fb35"
    And I type "PerRo"
    And I click "Submit"
    Then I read "Correct solution!"
    And I don't read "Correct spelling: perro"

  Scenario: Going to the next challenge
    Given I open "/course/test-1/skill/short-input-test-2?testChallenge=aa171956aefe"
    And I type "agua"
    And I click "Submit"
    And I click "Continue"
    Then I see a panel with only a Skip and a Cancel button

  Scenario: Going to the next challenge with keyboard only
    Given I open "/course/test-1/skill/short-input-test-2?testChallenge=aa171956aefe"
    And I type "agua"
    And I hit the enter key
    And I hit the enter key
    Then I see a panel with only a Skip and a Cancel button

  Scenario: using the hover-over dictionary
    Given I open "/course/test-1/skill/short-input-test-3?testChallenge=86665e4f61fa"
    Then I see a tooltip that says "tu"