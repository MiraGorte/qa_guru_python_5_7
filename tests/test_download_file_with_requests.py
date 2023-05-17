import os.path
import requests
from selene import browser
from selenium import webdriver

def test_downloaded_file_size():
    PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    resources_package = os.path.join(PROJECT_ROOT_PATH, '../resources')
    # TODO сохранять и читать из tmp, использовать универсальный путь
    url = 'https://selenium.dev/images/selenium_logo_square_green.png'

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": resources_package,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    browser.config.driver_options = options

    r = requests.get(url)
    with open('selenium_logo.png', 'wb') as file:
        file.write(r.content)

    size = os.path.getsize('selenium_logo.png')

    assert size == 30803
