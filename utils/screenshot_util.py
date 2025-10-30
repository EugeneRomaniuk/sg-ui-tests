import datetime
import os

from _pytest.fixtures import FixtureRequest
from selenium.webdriver.remote.webdriver import WebDriver


class ScreenshotUtil:

    def __init__(self, driver: WebDriver, request: FixtureRequest):
        self.driver = driver
        self.request = request

    def save_screenshot(self) -> None:
        os.makedirs("screenshots", exist_ok=True)
        test_name = self.request.node.name
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M')
        self.driver.save_screenshot(f"screenshots/{test_name}_{time}.png")
