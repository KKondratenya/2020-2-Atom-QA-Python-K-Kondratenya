from ui.locators.basic_locators import CreateCampaignLocators
from ui.pages.base_page import BasePage
import os
import uuid


class CreateCampaignPage(BasePage):
    locators = CreateCampaignLocators()

    def create_campaign(self):
        self.click(self.locators.CREATE_AUDIO_CAMPAIGN)
        name = uuid.uuid4().hex
        input_name = self.find(self.locators.INPUT_CAMPAIGN_NAME)
        input_name.clear()
        input_name.send_keys(name)
        self.click(self.locators.BANNER_FORMAT_BUTTON)
        self.find(self.locators.INPUT_FILE).send_keys(os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'example', 'file_example.mp3')))
        self.wait(15)
        self.click(self.locators.SUBMIT_CREATE_CAMPAIGN_BUTTON)
        self.wait(15)
        return name
