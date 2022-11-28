import pytest
from selenium import webdriver
from datetime import datetime
import os
from pages.login_page import LoginPage

def launch_app():
    driver = webdriver.Firefox()
    driver.get('https://demo.ebanq.com/log-in')
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def teardown(driver):
    test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1]
    test_name = test_name.split(']')[0]
    test_name = test_name.split(' ')[0]
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    driver.save_screenshot(fr'.\evidence\{test_name}_{timestamp}.png')
    driver.quit()


@pytest.fixture()
def setup():
    driver = launch_app()
    yield driver
    teardown(driver)

@pytest.fixture()
def user_setup():
    driver = launch_app()
    login_page = LoginPage(driver)
    login_page.user_login()
    yield driver
    teardown(driver)

@pytest.fixture()
def admin_setup():
    driver = launch_app()
    login_page = LoginPage(driver)
    login_page.admin_login()
    yield driver
    teardown(driver) 