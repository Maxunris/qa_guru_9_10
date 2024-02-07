from selene.support import by
from selene.support.conditions import be
from selene import browser
from selenium import webdriver

def test_github_issue():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"

    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(browser.config.base_url)

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)