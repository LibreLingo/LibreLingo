Feature: Fanfare screen

  A screen to display to the user when a practice session is successfully completed

  Scenario: Getting to the fanfare screen
    Given I open "/course/test-1/skill/continuous"
    Then fanfare screen looks correct
    And fanfare screen looks cute
    And I read "Lesson completed!"
    And I see a "Continue to course page" button
    And I see a "Tweet about LibreLingo" button
    And I see a twitter icon

  Scenario: Going to course page using the button
    Given I open "/course/test-1/skill/continuous"
    And I click "Continue to course page"
    Then I should be on "/course/test-1"

  Scenario: Going to course page using the keyboard
    Given I open "/course/test-1/skill/continuous"
    And I hit the enter key
    Then I should be on "/course/test-1"
