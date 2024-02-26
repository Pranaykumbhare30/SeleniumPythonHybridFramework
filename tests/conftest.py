import pytest
from selenium import webdriver
from utilities import ReadConfigerations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigerations.read_configuration("basic info", "browser")

    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Safari()
    else:
        print("Provide a valid browser name from this list Chrome,Firefox,Safari")

    driver.maximize_window()
    app_url = ReadConfigerations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
