from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_field = (By.CSS_SELECTOR, "#country")
    linkText_USA = (By.LINK_TEXT, "United States of America")
    checkBox = (By.CSS_SELECTOR, ".checkbox")
    purchaseButton = (By.CSS_SELECTOR, "input[value='Purchase']")
    successMessage = (By.CSS_SELECTOR, ".alert-success")

    def getCountryField(self):
        return self.driver.find_element(*ConfirmPage.country_field)

    def getlinkText_USA(self):
        return self.driver.find_element(*ConfirmPage.linkText_USA)

    def clickCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getPurchaseBox(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)





