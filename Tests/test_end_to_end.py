import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.BaseClass import BaseClass
from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import *


class TestOne(BaseClass):

    def test_end_to_end(self):
        tc_name = "End_to_End_Scenario"
        try:
            log = self.getLogger()
            homepage = HomePage(self.driver)
            checkOutPage = CheckOutPage(self.driver)
            confirmPage = ConfirmPage(self.driver)

            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_1" + ".png")

            # Click Shop link to access Checkout Page
            homepage.shopItems().click()
            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_2" + ".png")

            # Retrieve list of products; iterate thru list to find Blackberry product & add to cart
            log.info("getting products")
            products = checkOutPage.getProducts()
            #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

            # for product in products:
            #     productName = product.find_element(By.XPATH, "div/h4/a").text
            #     if productName == "Blackberry":
            #         product.find_element(By.XPATH, "div/button").click()

            for product in products:
                productName = product.text
                if "Blackberry" in productName:
                    product.find_element(By.XPATH, "div/button").click()
                    #checkOutPage.addToCartButton().click() # Not working

            # Click Checkout Button
            checkOutPage.checkOut().click()
            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_3" + ".png")
            #self.driver.find_element(By.CSS_SELECTOR, ".nav-link.btn.btn-primary").click()

            # Click Checkout Button (Success Button)
            checkOutPage.clickSuccessButton().click()
            #self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()

            # Enter United States in Country field
            log.info("Entering country name as United")
            confirmPage.getCountryField().send_keys("United")
            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_4" + ".png")
            #self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("United")

            # Use Explicit Wait until United States of America displays
            #wait = WebDriverWait(self.driver, 10)
            # wait.until(expected_conditions.presence_of_element_located((confirmPage.getlinkText_USA())))
            # confirmPage.getlinkText_USA().click()
            self.verifyLinkPresence("United States of America")
            self.driver.find_element(By.LINK_TEXT, "United States of America").click()

            # Select Checkbox
            confirmPage.clickCheckBox().click()
            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_5" + ".png")
            #self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()

            # Click Purchase button
            confirmPage.getPurchaseBox().click()
            #self.driver.find_element(By.CSS_SELECTOR, "input[value='Purchase']").click()

            # Confirm success message
            successText = confirmPage.getSuccessMessage().text
            #successText = self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text
            assert "Success! Thank you!" in successText
            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_6" + ".png")

        except:
            self.driver.save_screenshot("..\\Screenshots\\" + "FAIL_" + tc_name + ".png")
            raise