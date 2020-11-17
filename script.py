__author__ = "Ismayil Aliyev"

from tests.settings import *
from tests import utils
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
import tests.ElementsTesting
import tests.MenuItemTesting
import tests.ScreenshotTesting
import tests.SearchTesting

# example_tests = TestLoader().loadTestsFromTestCase(ExampleTests)
# example2_tests = TestLoader().loadTestsFromTestCase(Example2Test)

ElementTest = TestLoader().loadTestsFromTestCase(tests.ElementsTesting.ElementsTesting)
MenuAboutUsTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.AboutUsTesting)
MenuBlogTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.BlogTesting)
MenuCaseStudiesTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.CaseStudiesTesting)
MenuContactUsTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.ContactUsTesting)
MenuPlatformTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.PlatformTesting)
MenuSolutionTest = TestLoader().loadTestsFromTestCase(tests.MenuItemTesting.SolutionsTesting)
ScreenshotDesktopTest = TestLoader().loadTestsFromTestCase(tests.ScreenshotTesting.DesktopSizeScreenshotTesting)
ScreenshotMobileTest = TestLoader().loadTestsFromTestCase(tests.ScreenshotTesting.MobileSizeScreenshotTesting)
SearchResultsTest = TestLoader().loadTestsFromTestCase(tests.SearchTesting.SearchResultsTesting)
SearchNoResultsTest = TestLoader().loadTestsFromTestCase(tests.SearchTesting.SearchNoResultTesting)

suite = TestSuite([ElementTest, MenuAboutUsTest, MenuBlogTest, MenuCaseStudiesTest, MenuContactUsTest, MenuPlatformTest, MenuSolutionTest, ScreenshotDesktopTest, ScreenshotMobileTest, SearchResultsTest, SearchResultsTest])
kwargs = {
    "output": "reports",
    "report_name": "testing_result",
    "failfast": True
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)
