Feature: Landing page

  A landing page built with the purpose of giving a short introduction to the project and
  directing the user to the demo course or the about page

    Scenario: Opening landing page
      Given I open "/"
      Then landing page looks correct
      Then landing page looks cute
      And I read "LibreLingo"
      And I see a "Start learning Spanish" button
      And I see an "About LibreLingo" link
      And "Licensed under AGPL - Free as in Freedom" is graphically represented
