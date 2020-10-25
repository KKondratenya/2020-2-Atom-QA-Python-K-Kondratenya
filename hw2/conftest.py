import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base_page import BasePage
from ui.pages.modal_login import ModalLogin
from ui.pages.main_page import MainPage
from ui.pages.dashboard_page import DashboardPage
from ui.pages.create_campaign_page import CreateCampaignPage
from auth import email, password


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--selenoid', default=False)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    selenoid = request.config.getoption('--selenoid')

    return {
        'browser': browser,
        'version': version,
        'url': url,
        'selenoid': selenoid,
    }


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def create_campaign_page(driver):
    return CreateCampaignPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def modal_login(driver):
    return ModalLogin(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    url = config['url']
    selenoid = config['selenoid']

    if selenoid is not False:
        options = ChromeOptions()

        driver = webdriver.Remote(command_executor=f'http://{selenoid}/wd/hub/',
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )
    elif browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        manager = ChromeDriverManager(version=version)
        driver = webdriver.Chrome(executable_path=manager.install(),
                                  options=options,
                                  desired_capabilities={'acceptInsecureCerts': True}
                                  )
    elif browser == 'firefox':
        manager = GeckoDriverManager(version=version)
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver

    driver.quit()


@pytest.fixture
def dashboard_page(driver):
    main_page = MainPage(driver)
    main_page.click(main_page.locators.LOGIN_BUTTON)
    modal_login = ModalLogin(driver)
    modal_login.find(modal_login.locators.LOGIN).send_keys(email)
    modal_login.find(modal_login.locators.PASSWORD).send_keys(password)
    modal_login.click(modal_login.locators.SUBMIT_BUTTON)
    return DashboardPage(driver)
