from selenium.webdriver.common.by import By

from element.element import Element
from pages.base_page import BasePage


class CategoryPage(BasePage):
    _STREAM_BUTTON = (By.XPATH, "//button[contains(@class, 'tw-link')]")

    def _init_elements(self) -> None:
        self.stream_button = Element(self._STREAM_BUTTON, self.driver)

    def click_on_any_stream(self) -> None:
        self.stream_button.click_on_element_in_view_port()
