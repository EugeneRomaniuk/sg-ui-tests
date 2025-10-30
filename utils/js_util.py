from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def click_on_first_in_viewport(driver: WebDriver, elements: list[WebElement]) -> None:
    for element in elements:
        if is_element_visible_in_viewport(driver, element):
            ActionChains(driver).move_to_element(element).click().perform()
            return
    raise RuntimeError("No visible elements found in viewport")


def is_element_visible_in_viewport(driver: WebDriver, element: WebElement) -> bool:
    try:
        return driver.execute_script("""
            const rect = arguments[0].getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth) &&
                rect.width > 0 && rect.height > 0
            );
        """, element)
    except Exception:
        return False


def is_video_playing(driver: WebDriver, video: WebElement) -> bool:
    try:
        return driver.execute_script("return !arguments[0].paused && arguments[0].readyState > 2;", video)
    except Exception as e:
        print(f"Error during checking player state: {e}")
        return False


def click(driver: WebDriver, element: WebElement) -> None:
    driver.execute_script("arguments[0].click();", element)


def scroll_down(driver: WebDriver) -> None:
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
