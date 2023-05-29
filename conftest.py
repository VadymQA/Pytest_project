import time

import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language!")

#
@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")

    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})


    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser

    print("\nquit browser..")

    time.sleep(2)
    browser.quit()






