from typing import Tuple, Optional

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class WaitUtil:
    def __init__(self, driver: WebDriver, default_timeout: int = 5):
        self.driver = driver
        self.default_timeout = default_timeout

    def get_wait(self, timeout: Optional[int] = None) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout or self.default_timeout)

    def wait_for_element_to_be_clickable(self, locator: Tuple[str, str], timeout: Optional[int] = None):
        return self.get_wait(timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_element_to_be_present(self, locator: Tuple[str, str], timeout: Optional[int] = None):
        return self.get_wait(timeout).until(ec.presence_of_element_located(locator))

    def wait_for_element_to_be_visible(self, locator: Tuple[str, str], timeout: Optional[int] = None):
        return self.get_wait(timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable_non_failing(self, locator: Tuple[str, str], timeout: Optional[int] = None):
        try:
            return self.get_wait(timeout).until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            return None
