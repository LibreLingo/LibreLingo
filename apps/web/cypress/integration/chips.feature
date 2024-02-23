Feature: Chips challenge

  A challenge type where the user has to reorder chips to form a correct sentence

  Scenario: Getting a chips challenge
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=5000997897bb"
    Then I read "Translate"
    And I read "How"
    And I read "are"
    And I read "you"
    And I read "today?"
    And I see a panel with a Skip, Cancel and disabled "Submit" button
    And I see the correct chips
    And chips challenge looks correct
    And I see a "Feedback" link in the navbar

  Scenario: Using the mini-dictionary
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=c3f7fcb9c86c"
    Then words with definitions have tooltips
    
  Scenario: Submitting an incorrect solution
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=5000997897bb"
    And I click "estás"
    And I click "hoy"
    And I click "Como"
    Given I click "Submit"
    Then I read "Incorrect solution"
    And I read "Correct answer: ¿Como, estás hoy?"
    And I see a "Continue" button
    Given I click "Continue"
    Then I see a panel with a Skip, Cancel and a disabled "Submit" button

  Scenario: Submitting a correct solution
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=5000997897bb"
    And I click "Como"
    And I click "estás"
    And I click "hoy"
    Then I have unused chips
    Given I click "Submit"
    Then I see the challenge panel with no Skip and no "Submit" button
    And I read "Correct solution"
    And I see a "Continue" button
    Given I click "Continue"
    Then I see a panel with only a Skip, Cancel and a disabled "Submit" button

  Scenario: Submitting an alternative correct solution
    Given I open "/course/test-1/skill/chips-test-0?testChallenge=5000997897bb"
    And I click "Hoy"
    And I click "como"
    And I click "estás"
    Given I click "Submit"
    Then I see the challenge panel with no Skip and no "Submit" button
    And I read "Correct solution"
    And I see a "Continue" button
    Given I click "Continue"
    Then I see a panel with only a Skip and a Cancel button

    Scenario: Submitting an alternative correct solution with uncapitalized chips
      Given I open "/course/test-1/skill/chips-test-0?testChallenge=59cd9b603be9"
      And I click "como"
      And I click "estás"
      And I click "hoy"
      Given I click "Submit"
      Then I see the challenge panel with no Skip and no "Submit" button
      And I read "Correct solution"
      And I see a "Continue" button
      Given I click "Continue"
      Then I see a panel with only a Skip, Cancel and a disabled "Submit" button