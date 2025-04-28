import logging
import time
from automation_exercise_test.UI_test.search_page_test.data.test_page_object import ProductPageObject

import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope='function')
def pw_open():
    with sync_playwright() as p:
        browser = p.chromium.launch(slow_mo=1500)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://www.automationexercise.com/products', wait_until='load')
        yield page
        browser.close()


