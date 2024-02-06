Feature: Skill introduction page

  An introduction page for skills, where the user can read the contents of an (optional)
  markdown file, which explains the grammar in the skill.

  Scenario: Opening the introduction page
    When I open "/course/test-1"
    And I click "Practice"
    Then I should be on "/course/test-1/skill/animals/introduction"
    Then I read "Introduction to animals"

  Scenario: Practicing the skill from the introduction page
    When I open "/course/test-1/skill/animals/introduction"
    Then I read "Introduction to animals"
    When I click "Practice Animals"
    Then I should be on "/course/test-1/skill/animals"
