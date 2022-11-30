import { Given } from "cypress-cucumber-preprocessor/steps"

Given(/I see an? "(.*)" link/, (text) => {
  cy.findByRole('link', { name: text }).should("be.visible")
})

Given(/I don't see an? "(.*)" link/, (text) => {
  cy.findByRole('link', { name: text }).should("not.exist")
})
