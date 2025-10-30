from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from element.should import Should
from utils import js_util
from utils.logger import simple_element_log_decorator


class Element:

    def __init__(self, locator: tuple[str, str], driver: WebDriver):
        self.locator = locator
        self.driver = driver
        self.should = Should(self)

    def get_element(self) -> WebElement:
        return self.driver.find_element(*self.locator)

    @simple_element_log_decorator
    def click(self) -> None:
        self.get_element().click()

    @simple_element_log_decorator
    def click_with_js(self) -> None:
        js_util.click(self.driver, self.get_element())

    @simple_element_log_decorator
    def click_on_element_in_view_port(self) -> None:
        elements = self.driver.find_elements(*self.locator)
        js_util.click_on_first_in_viewport(self.driver, elements)

    @simple_element_log_decorator
    def send_keys(self, text: str, clear_first: bool = True) -> None:
        element = self.get_element()
        if clear_first:
            element.clear()
        element.send_keys(text)
