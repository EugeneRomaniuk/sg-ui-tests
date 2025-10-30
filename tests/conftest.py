import pytest
from _pytest.config import Config
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

from pages.app import App
from tests.hooks import REMOTE, DEVICE, APP_URL
from utils.screenshot_util import ScreenshotUtil

pytest_plugins = ["tests.hooks"]


@pytest.fixture(scope="session")
def config(request: FixtureRequest) -> Config:
    return request.config


@pytest.fixture
def driver(config: Config):
    if config.getoption(REMOTE):
        raise RuntimeError("Remote mode is not implemented yet")
    else:
        driver = get_local_chrome_driver(config)

    yield driver

    driver.quit()


@pytest.fixture()
def app(driver: WebDriver, config: Config) -> App:
    return App(driver, config.getoption(APP_URL))


@pytest.fixture()
def screenshot_util(driver: WebDriver, request: FixtureRequest) -> ScreenshotUtil:
    return ScreenshotUtil(driver, request)


def get_local_chrome_driver(config: Config) -> WebDriver:
    device = config.getoption(DEVICE)
    mobile_emulation = {"deviceName": device}
    options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(service=Service(), options=options)
