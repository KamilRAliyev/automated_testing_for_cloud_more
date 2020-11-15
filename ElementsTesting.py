import unittest
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox(executable_path="./webdriver/geckodriver")
WEBSITE_URL = "https://web.cloudmore.com/"

class ElementsTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = firefox
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