import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def set_browser():
#   browser.config.base_url = 'https://demoqa.com/'
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield

    browser.quit()
