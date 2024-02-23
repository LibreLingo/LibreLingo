Feature: Cards challenge

  A challenge type where the user has to select the correct card

  Scenario: Getting a cards challenge
    Given I open "course/test-1/skill/cards-test"
    Then cards challenge looks correct
    And I read "Which of these is"
    And I see 3 cards
    And I see 3 inactive cards
    And I see a panel with a Skip, Cancel and disabled "Submit" button

  Scenario: Getting a cards challenge in an iPhone
    Given that I have an iPhone 6
    And I open "course/test-1/skill/cards-test"
    Then I see 4 cards

  Scenario: Clicking a card
    Given I open "course/test-1/skill/cards-test"
    And I click a card
    And I see an enabled "Submit" button
    And the highlighted card looks correct
    And I see an active card
    And I see 2 inactive cards
    And I see a "Skip" button

  Scenario: Submitting the correct answer
    Given I open "course/test-1/skill/cards-test"
    And I click the correct card
    And I click "Submit"
    Then I read "Correct solution"
    And I see a "Continue" button

  Scenario: Submitting the incorrect answer
    Given I open "course/test-1/skill/cards-test"
    And I click an incorrect card
    And I click "Submit"
    Then I read "Incorrect solution"
    And I see a "Continue" button