import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb", help="specify language: [ ru | en-gb | es | fr ]. Default is 'en'")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print(f"\nstart chrome browser with {language} language..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
