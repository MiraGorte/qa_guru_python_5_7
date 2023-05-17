import os

from selene import browser
from selenium import webdriver

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp
def test_download_file_with_browser():
    resources_package = os.path.join(PROJECT_ROOT_PATH, 'resources')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": resources_package,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    assert os.path.exists(resources_package), "File not found!"
