from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from element.element import Element
from pages.base_page import BasePage


class HomePage(BasePage):
    _ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='consent-banner-accept']")
    _BROWSE_BUTTON = (By.CSS_SELECTOR, "a[href='/directory']")
    _CLOSE_MOBILE_APP_DIALOG_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Activate to close dialog']")
    _EXPAND_MOBILE_APP_DIALOG_BUTTON = (By.CSS_SELECTOR, " button[aria-label='Activate to expand dialog']")

    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver)
        self._url = url

    def _init_elements(self) -> None:
        self.accept_cookies_button = Element(self._ACCEPT_COOKIES_BUTTON, self.driver)
        self.browse_button = Element(self._BROWSE_BUTTON, self.driver)
        self.close_enjoy_you_experience_button = Element(self._CLOSE_MOBILE_APP_DIALOG_BUTTON, self.driver)
        self.expand_mobile_app_dialog_button = Element(self._EXPAND_MOBILE_APP_DIALOG_BUTTON, self.driver)

    def open(self) -> None:
        self.driver.get(self._url)
        self._close_random_use_mobile_app_dialog()

    def _close_random_use_mobile_app_dialog(self) -> None:
        expand_dialog_button = self.expand_mobile_app_dialog_button.should.be_clickable_non_failing(timeout=2)
        if expand_dialog_button:
            expand_dialog_button.click_with_js()

        close_dialog_button = self.close_enjoy_you_experience_button.should.be_clickable_non_failing(timeout=2)
        if close_dialog_button:
            close_dialog_button.click_with_js()
