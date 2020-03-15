// For authoring Nightwatch tests, see
// https://nightwatchjs.org/guide

module.exports = {
  "default e2e tests": browser => {
    browser
      .init()
      .waitForElementVisible("#app")
      .assert.containsText(".navbar-brand", "Recruiterbox Kudos")
      .assert.containsText("h1", "Recruiterbox Kudos")
      .assert.containsText(
        "p.lead:nth-child(2)",
        "A place to appreciate your colleagues for their work, contributions and help by giving them kudos."
      )
      .assert.containsText(
        "p.lead:nth-child(4)",
        "Just Sign In and start giving kudos to your colleagues."
      )
      .assert.containsText(".btn", "Login")
      .click(".btn")
      .setValue("#input-1", "root1")
      .setValue("#input-2", "qazwsxedc123!@#RFV")
      .click(".btn")
      .pause(5000)
      .assert.containsText("#kudos-received > a:nth-child(1)", "Kudos Received")
      .assert.containsText("#kudos-given > a:nth-child(1)", "Kudos Given")
      .assert.containsText(".btn", "Give Kudo")
      .assert.elementCount("div.my-2", 9)
      .click("li.nav-item:nth-child(2) > a:nth-child(1)")
      .assert.elementCount("div.my-2", 9)
      .click("#nav-collapse > ul.navbar-nav.ml-auto > ul > li:nth-child(2) > a")
      .pause(5000)
      .click("#input-1 > option:nth-child(2)")
      .setValue("#input-2", "Kudo 1")
      .setValue("#input-3", "This is the description of the kudo 1.")
      .click("#app > div > div > div:nth-child(2) > form > button")
      .waitForElementVisible(".swal-button")
      .assert.containsText(".swal-title", "Kudo is away ...")
      .assert.containsText(".swal-text", "You now have 2 left.")
      .click(".swal-button")
      .pause(5000)
      .assert.containsText(
        "div.my-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)",
        "Kudo 1"
      )
      .assert.containsText(
        "div.my-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2)",
        "This is the description of the kudo 1."
      )
      .click("#nav-collapse > ul.navbar-nav.ml-auto > ul > li:nth-child(2) > a")
      .pause(5000)
      .click("#input-1 > option:nth-child(2)")
      .setValue("#input-2", "Kudo 2")
      .setValue("#input-3", "This is the description of the kudo 2.")
      .click("#app > div > div > div:nth-child(2) > form > button")
      .waitForElementVisible(".swal-button")
      .assert.containsText(".swal-title", "Kudo is away ...")
      .assert.containsText(".swal-text", "You now have 1 left.")
      .click(".swal-button")
      .pause(5000)
      .assert.containsText(
        "div.my-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)",
        "Kudo 2"
      )
      .assert.containsText(
        "div.my-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2)",
        "This is the description of the kudo 2."
      )
      .click("#nav-collapse > ul.navbar-nav.ml-auto > ul > li:nth-child(2) > a")
      .pause(5000)
      .click("#input-1 > option:nth-child(2)")
      .setValue("#input-2", "Kudo 3")
      .setValue("#input-3", "This is the description of the kudo 3.")
      .click("#app > div > div > div:nth-child(2) > form > button")
      .waitForElementVisible(".swal-button")
      .assert.containsText(".swal-title", "Kudo is away ...")
      .assert.containsText(".swal-text", "You now have 0 left.")
      .click(".swal-button")
      .pause(5000)
      .assert.containsText(
        "div.my-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)",
        "Kudo 3"
      )
      .assert.containsText(
        "div.my-2:nth-child(1) > div:nth-child(1) > div:nth-child(1) > p:nth-child(2)",
        "This is the description of the kudo 3."
      )
      .click("#logout")
      .pause(2000)
      .assert.containsText(".navbar-brand", "Recruiterbox Kudos")
      .assert.containsText("h1", "Recruiterbox Kudos")
      .assert.containsText(
        "p.lead:nth-child(2)",
        "A place to appreciate your colleagues for their work, contributions and help by giving them kudos."
      )
      .assert.containsText(
        "p.lead:nth-child(4)",
        "Just Sign In and start giving kudos to your colleagues."
      )
      .assert.containsText(".btn", "Login")
      .end();
  }
};
