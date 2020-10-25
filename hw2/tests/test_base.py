# import allure
import pytest
# from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
from selenium.webdriver.common.by import By


from tests.base import BaseCase


class Test(BaseCase):

    @pytest.mark.UI
    def test_success_login(self, dashboard_page):
        dashboard_page.find(dashboard_page.locators.AUTH_EMAIL)

    @pytest.mark.UI
    def test_error_login(self):
        self.base_page.click(self.main_page.locators.LOGIN_BUTTON)
        self.base_page.find(self.modal_login.locators.LOGIN).send_keys('kondratenya21@yahoo.ru')
        self.base_page.find(self.modal_login.locators.PASSWORD).send_keys('Qwerty')
        self.base_page.click(self.modal_login.locators.SUBMIT_BUTTON)
        self.base_page.find(self.modal_login.locators.ERROR_LOGIN)

    @pytest.mark.UI
    def test_create_campaign(self, dashboard_page):
        create_campaign_page = dashboard_page.start_creating_campaign()
        campaign_name = create_campaign_page.create_campaign()
        dashboard_page.find((By.XPATH, f'//a[contains(text(), "{campaign_name}")]'))

    @pytest.mark.UI
    def test_create_segment(self, dashboard_page):
        segment_page = dashboard_page.goToSegment()
        name = segment_page.create_segment()
        segment_page.find((By.XPATH, f'//a[contains(text(), "{name}")]'))

    @pytest.mark.UI
    def test_create_and_delete_segment(self, dashboard_page):
        segment_page = dashboard_page.goToSegment()
        name = segment_page.create_segment()
        segment_page.delete_segment(name)
        segment_page.hide_element((By.XPATH, f'//a[contains(text(), "{name}")]'))
