import os

import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.modal_login import ModalLogin
from ui.pages.create_campaign_page import CreateCampaignPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.modal_login: ModalLogin = request.getfixturevalue('modal_login')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.create_campaign_page: CreateCampaignPage = request.getfixturevalue('create_campaign_page')
