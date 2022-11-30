import { Then } from "cypress-cucumber-preprocessor/steps"

Then("I see the challenge panel with no Skip button", () => {
  cy.get(".panel").should("be.visible")
  cy.get(".panel button").contains("Skip").should("not.exist")
})

Then("I see the challenge panel", () => {
  cy.get(".panel").should("be.visible")
})

Then("I see a panel with only a Skip button", () => {
  cy.wait(500) // This is necessary due to the animation
  cy.get(".panel button").contains("Skip").should("be.visible")
  cy.get(".panel ").find("button").should("have.length", 1)
})

Then("I see a panel with only a Skip and a Can't listen now button", () => {
  cy.wait(500) // This is necessary due to the animation
  cy.get(".panel button").contains("Skip").should("be.visible")
  cy.get(".panel button").contains("Can't listen now").should("be.visible")
  cy.get(".panel ").find("button").should("have.length", 3)
})

Then("I see a panel with only a Skip button", () => {
  cy.wait(500) // This is necessary due to the animation
  cy.get(".panel button").contains("Skip").should("be.visible")
  cy.get(".panel ").find("button").should("have.length", 2)
})

Then("I see a panel with only a Skip button", () => {
  cy.wait(500) // This is necessary due to the animation
  cy.get(".panel button").contains("Skip").should("be.visible")
  cy.get(".panel ").find("button").should("have.length", 3)
})
