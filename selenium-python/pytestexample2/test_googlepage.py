import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_google(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
