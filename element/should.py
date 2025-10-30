from typing import TYPE_CHECKING

from utils.logger import simple_element_log_decorator
from utils.wait_util import WaitUtil

if TYPE_CHECKING:
    from element.element import Element


class Should:
    def __init__(self, element: "Element"):
        self.element = element
        self.wait = WaitUtil(element.driver)
        self.locator = element.locator

    @simple_element_log_decorator
    def be_present(self, timeout: int = None) -> "Element":
        self.wait.wait_for_element_to_be_present(self.locator, timeout)
        return self.element

    @simple_element_log_decorator
    def be_visible(self, timeout: int = None) -> "Element":
        self.wait.wait_for_element_to_be_visible(self.locator, timeout)
        return self.element

    @simple_element_log_decorator
    def be_clickable(self, timeout: int = None) -> "Element":
        self.wait.wait_for_element_to_be_clickable(self.locator, timeout)
        return self.element

    @simple_element_log_decorator
    def be_clickable_non_failing(self, timeout: int = None) -> "Element | None":
        optional_element = self.wait.wait_for_element_to_be_clickable_non_failing(self.locator, timeout)
        return self.element if optional_element else None
