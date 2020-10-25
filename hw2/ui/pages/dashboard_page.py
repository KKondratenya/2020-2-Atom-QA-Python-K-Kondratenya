from ui.locators.basic_locators import DashboardLocators
from ui.pages.base_page import BasePage
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.segment_page import SegmentPage


class DashboardPage(BasePage):
    locators = DashboardLocators()

    def start_creating_campaign(self):
        element = self.try_to_find(self.locators.CREATE_CAMPAIGN_BUTTON)
        if (element is not False and element.is_displayed()):
            element.click()
        else:
            self.click(self.locators.CREATE_CAMPAIGN_LINK)
        return CreateCampaignPage(self.driver)

    def goToSegment(self):
        self.click(self.locators.GO_TO_SEGMENT)
        return SegmentPage(self.driver)
