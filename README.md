# PythonSeleniumExampleTestFramework
Python Selenium Automation Project - This project demonstrates the Python Selenium Automation Framework.  This project was written in Python and uses the Pytest framework, Selenium Webdriver and the Webdriver Manager libraries. Logging is handled by Log4j Library. Pytest-HTML library can be added for reporting.
Original source for this project comes from the following online Udemy Course: 
https://www.udemy.com/course/learn-selenium-automation-in-easy-python-language

Libraries:

This project requires installation of the following Python Libraries

pytest
pytest-html
selenium
webdriver-manager

**Key Features **

(1) Webdriver Manager library has been implemented to avoid downloading the latest webdriver when browser versions changed. 
In the conftest.py file, the following lines import the necessary Webdriver Manager libraries.

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
 
Next, in the conftest.py file, the following Else/If block determines which driver to use based on the value inputted at command line (chrome, firefox or edge)

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    elif browser.lower() == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

(2) Browser & Test Environment can be set at command line execution.

In the conftest.py file, the following pytest_addoption method adds "env" (environment) and "browser" options so that these variables can be set during command line execution.

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="uat",
                     help="Environment to run test against")
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run test against")

In the conftest.py file, the browser and env variables are stored in the def setup(request) method
				 
@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("browser")
    env = request.config.getoption("env")
	
The following statements in the conftest.py file, 

(a) import the environments from a data dictionary file called "Environments.py"

from Tests.Environments import Environments

(b) stores enviroment URL into variable "baseURL"

baseURL = Environments.return_environments(env)
print(baseURL)
driver.get(baseURL)

(c) The following lines are from the Environments.py Data Dictionary file

class Environments(dict):

    def return_environments(environment):

        # Data Dictionary of Environments
        environments={
            'dev': 'https://rahulshettyacademy.com/angularpractice/',
            'uat': 'https://rahulshettyacademy.com/angularpractice/',
            'prod': 'https://rahulshettyacademy.com/angularpractice/'
            }
        return environments[environment]

(d) To execute script from command line, use the following commands:
(i.e., browser = chrome & env = uat)

py.test .\test_end_to_end.py --browser chrome --env uat

(3) Reporting using Pytest-HTML library - Reports can be generated after each test run using the following commands:

<CHROME>
To Run All Tests:
py.test --browser chrome --env uat --html=test_results/report.html

To Run a Single Test:
py.test .\test_end_to_end.py --browser chrome --env uat --html=test_results/report.html

<FIREFOX>
To Run All Tests:
py.test --browser firefox --env uat --html=test_results/report.html

To Run a Single Test:
py.test .\test_end_to_end.py --browser firefox --env uat --html=test_results/report.html

<EDGE>
To Run All Tests:
py.test --browser edge --env uat --html=test_results/report.html

To Run a Single Test:
py.test .\test_end_to_end.py --browser edge --env uat --html=test_results/report.html

After test execution, report will be generated in Tests\test_results with name = "report.html".

(4) Screenshots
Screenshots are created using Selenium Webdriver save_screenshot() function. During test execution, screenshots are saved to Screenshots directory. Screenshots are
are prepended with either "Pass" or "Fail" and include test case name (tc_name). Screenshots are created in PNG format.

            self.driver.save_screenshot("..\\Screenshots\\" + "PASS_" + tc_name + "_1" + ".png")

(5) Logging 
Logging function is enabled using Log4j Library. The log file will be created in the "Tests" directory with file name "logfile.log".
The getLogger method is contained in BaseClass.py.

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

In the test script:

log = self.getLogger()
log.info("getting products")

(6) Try Blocks used in test case

  def test_end_to_end(self):
        tc_name = "End_to_End_Scenario"
        try:
            homepage = HomePage(self.driver)
            checkOutPage = CheckOutPage(self.driver)
            confirmPage = ConfirmPage(self.driver)

(7) Asserts used in test case

Confirm success message
            successText = confirmPage.getSuccessMessage().text
            assert "Success! Thank you!" in successText
