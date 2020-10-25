from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from ui.locators.basic_locators import BasePageLocators

RETRY_COUNT = 3


class BasePage(object):
    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def hide_element(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until_not(EC.presence_of_element_located(locator))

    def try_to_find(self, locator, timeout=None) -> WebElement:
        try:
            element = self.find(locator, timeout)
            return element
        except TimeoutException:
            return False

    def click(self, locator, timeout=None):
        # попытки чтобы кликнуть
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def search(self, query):
        search_field = self.find(self.locators.QUERY_LOCATOR)
        search_field.clear()
        search_field.send_keys(query)
        self.find(self.locators.GO_BUTTON).click()
