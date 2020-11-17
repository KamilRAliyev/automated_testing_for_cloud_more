__author__ = "Ismayil Aliyev"

from pyunitreport import HTMLTestRunner
import unittest
import os
import utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "https://web.cloudmore.com/"
MENU_LINKS = utils.get_menu_links(WEBSITE_URL)

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

class SearchNoResultTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    
    @unittest.expectedFailure
    def test_search_Ismayil(self):
        search_key = "Ismayil"
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        results = self.driver.find_elements_by_css_selector('ul.hs-search-results__listing > li')
        if len(results) > 0:
            flag = True
        else:
            flag = False
        self.assertTrue(flag, msg=f"No Results for {search_key}")
    

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class SearchResultsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def test_search_hogset(self):
        search_key = "Högset"
        self.driver.find_element_by_css_selector('span.search > i').click()
        search_box = self.driver.find_element_by_css_selector("input[type='search'].hs-input")
        search_box.send_keys(search_key)
        search_button = self.driver.find_element_by_css_selector("button[type='submit'].hs-button")
        search_button.click()
        self.driver.implicitly_wait(30)
        results = self.driver.find_elements_by_css_selector('ul.hs-search-results__listing > li')
        if len(results) > 0:
            flag = True
        else:
            flag = False
        self.assertTrue(flag, msg=f"No Results for {search_key}")
    
    
    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class PlatformTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(MENU_LINKS['platform'])
        inst.driver.title

    def test_logo(self):
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at page.")
    
    def test_footer_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector("input[value='Submit'].hs-button").is_displayed()
        self.assertTrue(form_bool, msg="Footer Contact Us form is not displayed")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class SolutionsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(MENU_LINKS['solutions'])
        inst.driver.title

    def test_logo(self):
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at page.")
    
    def test_footer_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector("input[value='Submit'].hs-button").is_displayed()
        self.assertTrue(form_bool, msg="Footer Contact Us form is not displayed")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class AboutUsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(MENU_LINKS['about us'])
        inst.driver.title

    def test_logo(self):
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at page.")
    
    def test_footer_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector("input[value='Submit'].hs-button").is_displayed()
        self.assertTrue(form_bool, msg="Footer Contact Us form is not displayed")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class BlogTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(MENU_LINKS['blog'])
        inst.driver.title

    def test_logo(self):
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at page.")
    
    def test_footer_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector("input[value='Submit'].hs-button").is_displayed()
        self.assertTrue(form_bool, msg="Footer Contact Us form is not displayed")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class CaseStudiesTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(MENU_LINKS['case studies'])
        inst.driver.title

    def test_logo(self):
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at page.")
    
    def test_footer_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector("input[value='Submit'].hs-button").is_displayed()
        self.assertTrue(form_bool, msg="Footer Contact Us form is not displayed")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class ContactUsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(MENU_LINKS['contact us'])
        inst.driver.title

    def test_logo(self):
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at page.")
    
    def test_footer_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector("input[value='Submit'].hs-button").is_displayed()
        self.assertTrue(form_bool, msg="Footer Contact Us form is not displayed")
    
    def test_body_contact_form(self):
        form_bool = self.driver.find_element_by_css_selector('input[value="Click Here"].hs-button').is_displayed()
        self.assertTrue(form_bool, msg="Body Contact Us form is not displayed")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

class ElementsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Firefox(executable_path="./webdriver/geckodriver")
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    def test_logo_image(self):
        logo_bool = self.driver.find_element_by_xpath('//*[@id="hs-link-module_14891423382401005"]/img').is_displayed()
        self.assertTrue(logo_bool, msg="Logo is not displayed.")

    def menu_item_element_tester(self, text, depth):
        menu_items = self.driver.find_elements_by_css_selector(f"li.hs-menu-item.hs-menu-depth-{depth} > a")
        for element in menu_items:
            if element.text.lower() == text:
                flag = element.is_displayed()
                break
            else:
                flag = False
        self.assertTrue(flag, msg=f"{text} - menu item, is not here")
    
    def test_navElements(self):
        names = ["platform", "solutions", "about us", "contact us", "blog", "case studies"]
        for text in names:
            with self.subTest():
                self.menu_item_element_tester(text, 1)

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
       unittest.main()