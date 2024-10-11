import pytest
from selene import browser
import time


@pytest.fixture(scope='function', autouse=True)
def set_browser():
    browser.config.base_url = 'https://demoqa.com/'
    # browser.config.driver.set_window_size(1280, 720)
    browser.config.window_width = 1280
    browser.config.window_height = 720
    yield
    time.sleep(5)
    browser.quit()
