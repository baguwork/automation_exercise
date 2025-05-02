import pytest
from playwright.sync_api import sync_playwright
from pathlib import Path
from automation_exercise_test.UI_test.config.config_reader import ConfigReader
from automation_exercise_test.UI_test.search_page_test.data.test_page_object import ProductPageObject


@pytest.fixture(scope="function")
def page(config):
    with sync_playwright() as p:
        browser = getattr(p, config.browser)
        browser = browser.launch(headless=config.headless, slow_mo=config.slow_mo)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope='function')
def product_page(page, config):
    product_page = ProductPageObject(page, config.base_url)
    product_page.open()
    product_page.click_cookie()
    return product_page

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    config_path = Path(f"config/{env}.yaml")
    return ConfigReader(config_path=config_path)

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="local", help="Environment name")

