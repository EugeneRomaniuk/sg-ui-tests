import pytest

# commandline arguments
REMOTE = "--remote"
DEVICE = "--device"
APP_URL = "--app-url"


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(REMOTE, action="store", default=False, help="Use remote WebDriver instead of local")
    parser.addoption(DEVICE, action="store", default="Pixel 2", help="Device type (e.g. 'iPhone X', 'Pixel 2')")
    parser.addoption(APP_URL, action="store", default="https://m.twitch.tv/", help="Initial app page url")
