import unittest
import utils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

WEBSITE_URL = "https://web.cloudmore.com/"
MENU_LINKS = utils.get_menu_links(WEBSITE_URL)

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


if __name__ == '__main__':
    unittest.main()