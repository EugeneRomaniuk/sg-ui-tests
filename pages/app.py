from functools import cached_property

from selenium.webdriver.remote.webdriver import WebDriver

from pages.browse_page import BrowsePage
from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.streamer_page import StreamerPage


class App:

    def __init__(self, driver: WebDriver, app_url: str):
        self.driver = driver
        self.app_url = app_url

    @cached_property
    def home_page(self) -> HomePage:
        return HomePage(self.driver, self.app_url)

    @cached_property
    def browse_page(self) -> BrowsePage:
        return BrowsePage(self.driver)

    @cached_property
    def streamer_page(self) -> StreamerPage:
        return StreamerPage(self.driver)

    @cached_property
    def category_page(self) -> CategoryPage:
        return CategoryPage(self.driver)
