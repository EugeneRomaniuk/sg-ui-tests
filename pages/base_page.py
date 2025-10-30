import time
from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from utils import js_util
from utils.wait_util import WaitUtil


class BasePage(ABC):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WaitUtil(self.driver)
        self._init_elements()

    @abstractmethod
    def _init_elements(self) -> None:
        pass

    def scroll_down_with_delay(self, delay=0) -> None:
        js_util.scroll_down(self.driver)
        if delay > 0:
            time.sleep(delay)

    """
       Waits until the page's DOM structure becomes stable — the number of elements
       in the DOM stops changing for a specified period of time.
    """

    def wait_for_page_load(self, timeout: int = 5, poll_interval: float = 0.5, stable_time: int = 1) -> None:
        end_time = time.time() + timeout
        last_len = len(self.driver.find_elements("xpath", "//*"))
        stable_start = time.time()

        while time.time() < end_time:
            time.sleep(poll_interval)
            current_len = len(self.driver.find_elements("xpath", "//*"))
            if current_len == last_len:
                if time.time() - stable_start >= stable_time:
                    return
            else:
                stable_start = time.time()
                last_len = current_len

        raise TimeoutError(f"Page was not loaded within {timeout} seconds")
