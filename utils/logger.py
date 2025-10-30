import functools
import logging
import sys


def get_logger(name: str = None, level=logging.INFO):
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


log = get_logger("")


def simple_element_log_decorator(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        locator = getattr(self, "locator")
        log.info("")
        log_args = f"args={args}" if args else ""
        log.info(f"{method.__name__} : {locator} {log_args}")
        try:
            result = method(self, *args, **kwargs)
            return result
        except Exception as e:
            log.error(f"{method.__name__} failed for {locator} | exception: {e}")
            raise

    return wrapper
