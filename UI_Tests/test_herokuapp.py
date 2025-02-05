import allure
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture()
def setup_test():
    print('\ntest was started')
    yield
    print('\ntest was finished')

@allure.feature('Login Page')
@allure.story('Positive login')
def test_login_positive(page: Page, setup_test):
    with allure.step('Open Login Page'):
        page.goto('https://the-internet.herokuapp.com/login')
    with allure.step('Input login and password'):
        page.locator('#username').fill('tomsmith')
        page.locator('#password').fill('SuperSecretPassword!')
    with allure.step('Click login button'):
        page.locator('//button').click()
    with allure.step('Login successful'):
        message = page.locator('#flash')
        expect(message).to_be_visible()
        expect(message).to_contain_text('You logged into a secure area!')

@allure.feature('Login Page')
@allure.story('Negative login')
def test_login_negative(page: Page):
    with allure.step('Open Login Page'):
        page.goto('https://the-internet.herokuapp.com/login')
    with allure.step('Input invalid credentials'):
        page.locator('#username').fill('test')
        page.locator('#password').fill('test')
        page.locator('//button').click()
    with allure.step('Login unsuccessful'):
        message = page.locator('#flash')
        expect(message).to_be_visible()
        expect(message).to_contain_text('Your username is invalid!')

@allure.feature('Login Page')
@allure.story('Dummy test')
def test_login_falled(page: Page):
    with allure.step('Open Login Page'):
        page.goto('https://the-internet.herokuapp.com/login')
    with allure.step('Input invalid credentials'):
        page.locator('#username').fill('test')
        page.locator('#password').fill('test')
        page.locator('//button').click()
    with allure.step('Login successful'):
        message = page.locator('#flash')
        expect(message).to_be_visible()
        expect(message).to_contain_text('This Dummy test should fail.')