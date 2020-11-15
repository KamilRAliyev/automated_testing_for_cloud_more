import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path

WEBSITE_URL = "https://web.cloudmore.com/"

class DesktopScreenshotTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def test_screenshot(self):
        search_key = "Högset"
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(30)
        iterator = 0
        while(self.driver.find_element_by_css_selector("a.hs-search-results__next-page") and iterator <=3):
            self.driver.find_element_by_css_selector("a.hs-search-results__next-page").click()
        self.driver.get_screenshot_as_file("screenshot.png")
        self.assertTrue(os.path.isfile('screenshot.png'), msg="Desktop size image is not found.")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class MobileScreenshotTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=360,640')
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver", options=options)
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def test_screenshot(self):
        search_key = "Högset"
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(30)
        iterator = 0
        while(self.driver.find_element_by_css_selector("a.hs-search-results__next-page") and iterator <=3):
            self.driver.find_element_by_css_selector("a.hs-search-results__next-page").click()
        self.driver.get_screenshot_as_file("screenshot_mobile.png")
        self.assertTrue(os.path.isfile('screenshot_mobile.png'), msg="Mobile size image is not found.")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()