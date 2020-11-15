from selenium import webdriver
browser = webdriver.Firefox(executable_path="./webdriver/geckodriver")

browser.get('http://seleniumhq.org/')