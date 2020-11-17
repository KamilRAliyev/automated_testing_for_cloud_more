import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "https://web.cloudmore.com/"

class DesktopSizeScreenshotTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def consent_banner(self):
        if self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button"):
            self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button").click()
            self.driver.implicitly_wait(30)

    def test_search_hogset(self):
        search_key = "Högset"
        self.consent_banner()
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(60)
        for i in range(2):
            try:
                self.driver.find_element_by_css_selector("a.hs-search-results__next-page").click()
                self.driver.implicitly_wait(30)
            except:
                break
        self.driver.get_screenshot_as_file("screenshot_desktop.png")
        self.assertTrue(os.path.isfile('screenshot_desktop.png'), msg="Desktop size image is not found.")
    
    

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class MobileSizeScreenshotTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.set_window_size(375,812)
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def consent_banner(self):
        if self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button"):
            self.driver.find_element_by_css_selector("a#hs-eu-confirmation-button").click()
            self.driver.implicitly_wait(30)

    def test_search_hogset(self):
        search_key = "Högset"
        self.consent_banner()
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(60)
        for i in range(2):
            try:
                self.driver.find_element_by_css_selector("a.hs-search-results__next-page").click()
                self.driver.implicitly_wait(30)
            except:
                break
        self.driver.get_screenshot_as_file("screenshot_mobile.png")
        self.assertTrue(os.path.isfile('screenshot_mobile.png'), msg="Desktop size image is not found.")
    
    

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()
if __name__ == '__main__':
    unittest.main()