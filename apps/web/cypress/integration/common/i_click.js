import { Then } from "cypress-cucumber-preprocessor/steps"

Then("I click on link {string}", (text) => {
  cy.get(`a.${text}`).click()
})

Then("I click {string}", (text) => {
  cy.contains(text).click()
})

Then("I click the {string} button", (text) => {
  cy.findByRole("button", { name: text }).click()
})
