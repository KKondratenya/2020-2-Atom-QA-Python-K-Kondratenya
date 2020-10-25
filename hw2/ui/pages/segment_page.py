from ui.locators.basic_locators import SegmentLocators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import uuid


class SegmentPage(BasePage):
    locators = SegmentLocators()

    def create_segment(self):
        element = self.try_to_find(self.locators.CREATE_SEGMENT_BUTTON)
        if (element is not False and element.is_displayed()):
            element.click()
            self.click(self.locators.CHOOSE_SEGMENT)
        else:
            self.click(self.locators.CREATE_SEGMENT_LINK)

        self.click(self.locators.ADD_SEGMENT_CHECKBOX)
        self.click(self.locators.SUBMIT_ADD_SEGMENT)
        name = uuid.uuid4().hex
        input_name = self.find(self.locators.INPUT_SEGMENT_NAME)
        input_name.clear()
        input_name.send_keys(name)
        self.click(self.locators.SUBMIT_CREATE_SEGMENT)
        return name

    def delete_segment(self, name):
        self.click((By.XPATH, f'//a[contains(text(), "{name}")]/ancestor::div[@class="main-module-Cell-Z2qWrE"]/following-sibling::div[4]'))
        self.click(self.locators.SUBMIT_DELETE)
