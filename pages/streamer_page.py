from selenium.webdriver.common.by import By

from element.element import Element
from pages.base_page import BasePage
from utils import js_util


class StreamerPage(BasePage):
    _CONTENT_GATE_START_WATCHING_BUTTON = (By.XPATH,
                                           "//div[@data-a-target='content-classification-gate-overlay']//button")
    _CHAT_WELCOME_MESSAGE = (By.XPATH, "//div[@data-a-target='chat-welcome-message']/span")
    _VIDEO = (By.XPATH, "//video[@playsinline]")

    def _init_elements(self) -> None:
        self.content_gate_start_watching_button = Element(self._CONTENT_GATE_START_WATCHING_BUTTON, self.driver)
        self.chat_welcome_message = Element(self._CHAT_WELCOME_MESSAGE, self.driver)
        self.video = Element(self._VIDEO, self.driver)

    def close_content_gate_popup_if_appeared(self) -> None:
        button = self.content_gate_start_watching_button.should.be_clickable_non_failing(timeout=3)
        if button:
            button.click()

    def wait_for_video_to_be_played(self) -> None:
        video = self.video.should.be_visible().get_element()
        self.wait.get_wait().until(lambda driver: js_util.is_video_playing(driver, video))
