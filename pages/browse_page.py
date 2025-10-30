from selenium.webdriver.common.by import By

from element.element import Element
from pages.base_page import BasePage


class BrowsePage(BasePage):
    _SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    _GET_CATEGORY_LINK_BY_NAME = "//p[@title='{}']/ancestor::a[contains(@href,'directory/category')]"

    def _init_elements(self) -> None:
        self.search_input = Element(self._SEARCH_INPUT, self.driver)

    def get_category_link_by_name(self, game_name: str) -> Element:
        return Element((By.XPATH, self._GET_CATEGORY_LINK_BY_NAME.format(game_name)), self.driver)

    def search_for(self, query: str) -> None:
        self.search_input.should.be_visible().send_keys(query)
