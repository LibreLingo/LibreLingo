Feature: Homepage button

  Scenario: I'm on course page
    When I open "/course/test-1/"
    And I click on link "logo"
    Then I should be on "/course/test-1/"

  Scenario: I'm on skill introduction page
    When I open "/course/test-1/skill/animals/introduction"
    And I click on link "logo"
    Then I should be on "/course/test-1/"

  Scenario: I'm on skill page
    When I open "/course/test-1/skill/animals"
    And I click on link "logo"
    Then I should be on "/course/test-1/"
