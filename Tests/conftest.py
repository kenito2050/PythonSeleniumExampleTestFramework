import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Tests.Environments import Environments

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="uat",
                     help="Environment to run test against")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run test against")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    env = request.config.getoption("env")
    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser.lower() == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    baseURL = Environments.return_environments(env)
    print(baseURL)
    driver.get(baseURL)
    #driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()