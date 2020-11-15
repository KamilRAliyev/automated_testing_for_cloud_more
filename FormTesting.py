import unittest
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox = webdriver.Firefox(executable_path="./webdriver/geckodriver")
WEBSITE_URL = "https://web.cloudmore.com/"

class FromTesting(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = firefox
        inst.driver.implicitly_wait(30)
        inst.driver.minimize_window()
        # navigate to the application home page
        inst.driver.get(WEBSITE_URL)
        inst.driver.title

    # def menuElements(self):
    #     menu_items = self.driver.find_elements_by_css_selector(f"li.hs-menu-item.hs-menu-depth-1 > a")
    #     for element in menu_items:
    #         MENU_LINKS += [element.text.lower(), element.get_attribute('href'), 1]
    #     menu_items = self.driver.find_elements_by_css_selector(f"li.hs-menu-item.hs-menu-depth-2 > a")
    #     for element in menu_items:
    #         MENU_LINKS += [element.text.lower(), element.get_attribute('href'), 2]
    
    def menu_logo_tester(self,link, name):
        self.driver.get(link)
        self.driver.implicitly_wait(30)
        logo_bool = self.driver.find_element_by_css_selector('img[alt*="Logo"]').is_displayed()
        self.driver.close()
        self.assertTrue(logo_bool, msg=f"Logo is not displayed at {name}:{link}.")

    def test_menu(self):
        menu_items = self.driver.find_elements_by_css_selector(f"li[class*='hs-menu-depth-'].hs-menu-item > a")
        for element in menu_items:
            with self.subTest():
                self.menu_logo_tester(element.get_attribute("href"), element.text)


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()