from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver


    products = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    addToCartButton = (By.XPATH, "div/button")
    chkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    successButton = (By.CSS_SELECTOR, "button[class='btn btn-success']")


    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getProductName(self):
        return self.driver.find_element(*CheckOutPage.productName)

    def addToCartButton(self):
        return self.driver.find_element(*CheckOutPage.addToCartButton)

    def checkOut(self):
        return self.driver.find_element(*CheckOutPage.chkoutButton)

    def clickSuccessButton(self):
        return self.driver.find_element(*CheckOutPage.successButton)