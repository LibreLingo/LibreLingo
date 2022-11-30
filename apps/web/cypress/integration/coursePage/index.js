import dayjs from "dayjs"
import settings from "../../../src/settings"
import { Before, Then, Given, And } from "cypress-cucumber-preprocessor/steps"

const COURSE_PAGE_URL = "/course/test"
const SKILL_PAGE_URL = `${COURSE_PAGE_URL}/skill/short-input-test-0?testChallenge=14fc2ae4fb35`

Before(() => {
  // Reset database
  cy.window().then((window) => {
    cy.wrap(
      window.indexedDB.deleteDatabase(`_pouch_${settings.database.local}`)
    )
  })
  cy.visit(COURSE_PAGE_URL)
})

Then("I see {int} skills that are not started", (number) => {
  cy.get("[data-started=false]").should("have.length", number)
})

Then("I see a skill that has no image set", () => {
  cy.get(".column:first-child .card img").should("have.length", 0)
})

Given("I have a stale skill", () => {
  cy.window().then((window) => {
    const db = window._DB
    cy.wrap(null).then(() => {
      return db
        .put({
          _id: "skills/38c2ea1c36d2",
          practiced: [
            { at: +dayjs().subtract(1, "year") },
            { at: +dayjs().subtract(1, "month") },
            { at: +dayjs().subtract(3, "month") },
            { at: +dayjs().subtract(6, "month") },
          ],
        })
        .then(() => {
          cy.reload()
        })
    })
  })
})

Then("I see a stale skill", () => {
  cy.get("[data-completed=true][data-stale=true]").should("have.length", 1)
})

Then("I don't see any stale skills", () => {
  cy.get("[data-completed=true][data-stale=true]").should("have.length", 0)
})

Given("I complete a lesson", () => {
  cy.visit(SKILL_PAGE_URL)
  cy.get("input[type=text]").type("el perro")
  cy.contains("Submit").click()
  cy.contains("Continue").click()
  cy.get("[aria-label=Cancel]").should("be.visible")
  cy.contains("Continue to course page").click()
})

Then("I'm redirected to the course page", () => {
  cy.url().should("match", new RegExp(`.*${COURSE_PAGE_URL}/?$`))
})

Then("I see a completed skill", () => {
  cy.get("[data-completed=true][data-stale=false]").should("have.length", 1)
  cy.get(".svg-inline--fa").should("be.visible")
})

Then("I see a started skill", () => {
  cy.get("[data-started=true][data-stale=false]").should("have.length", 1)
})

And("I see a skill with 20% progress", () => {
  cy.get("[data-test='skill card'] progress").should("have.value", 0.2)
  cy.get("[data-test='skill card'] progress").should("have.attr", "max", "1")
})

Given("practice statistics are saved correctly", () => {
  cy.window().then((window) => {
    const db = window._DB
    cy.wrap(null).then(() => {
      return db.get("skills/e70976d68b28").then((doc) => {
        cy.wrap(doc.practiced[0].incorrect).should("equal", 0)
        cy.wrap(doc.practiced[0].correct).should("equal", 1)
      })
    })
  })
})
