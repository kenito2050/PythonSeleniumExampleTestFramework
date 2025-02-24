import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, locator):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, locator)))

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def screenshot(result, tc_name):
        myScreenshot = pyautogui.screenshot()
        if result == "pass":
            screenshot_name = "PASSED" + "_" + tc_name + ".png"
        else:
            screenshot_name = "FAILED" + "_" + tc_name + ".png"
        # screenshot_path = r'C:\CRDLogs\'' + screenshot_name
        screenshot_path = "..\\Screenshots\\" + screenshot_name
        myScreenshot.save(screenshot_path)