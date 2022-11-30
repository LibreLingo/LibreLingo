import { Given } from "cypress-cucumber-preprocessor/steps"

Given(/I see an? "(.*)" button/, (text) => {
  cy.findByRole('button', { name: text }).should("be.visible")
})

Given(/I don't see an? "(.*)" button/, (text) => {
  cy.findByRole('button', { name: text }).should("not.exist")
})
