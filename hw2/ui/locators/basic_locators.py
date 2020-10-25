from selenium.webdriver.common.by import By
from auth import email


class BasePageLocators(object):
    AUTH_EMAIL = (By.XPATH, f'//div[contains(concat(" ", @class, " "), " right-module-userNameWrap") and contains(text(), "{email}")]')


class MainPageLocators(BasePageLocators):
    LOGIN_BUTTON = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')


class ModalLoginLocators(BasePageLocators):
    LOGIN = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    SUBMIT_BUTTON = (By.XPATH, '//div[contains(concat(" ", @class, " "), " authForm-module-button")]')
    ERROR_LOGIN = (By.XPATH, '//div[@class="formMsg_text" and contains(text(), "Invalid login or password")]')


class DashboardLocators(BasePageLocators):
    CREATE_CAMPAIGN_LINK = (By.CSS_SELECTOR, 'a[href="/campaign/new"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(concat(" ", @class, " "), " button-module-textWrapper") and contains(text(), "Создать кампанию")]')
    GO_TO_SEGMENT = (By.CSS_SELECTOR, 'a[href="/segments"]')


class CreateCampaignLocators(BasePageLocators):
    CREATE_AUDIO_CAMPAIGN = (By.CSS_SELECTOR, '._audiolistening')
    INPUT_CAMPAIGN_NAME = (By.XPATH, '//div[@class="input input_campaign-name input_with-close"]//input[@type="text"]')
    BANNER_FORMAT_BUTTON = (By.CSS_SELECTOR, '.banner-format-item')
    INPUT_FILE = (By.XPATH, '//div[@class="input__file-wrap"]//input[@type="file"]')
    SUBMIT_CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')


class SegmentLocators(BasePageLocators):
    CREATE_SEGMENT_LINK = (By.CSS_SELECTOR, 'a[href="/segments/segments_list/new/"]')
    CREATE_SEGMENT_BUTTON = (By.CLASS_NAME, 'button__text')
    CHOOSE_SEGMENT = (By.XPATH, '//div[@class="adding-segments-item"]')
    ADD_SEGMENT_CHECKBOX = (By.CSS_SELECTOR, 'input.adding-segments-source__checkbox')
    SUBMIT_ADD_SEGMENT = (By.XPATH, '//div[@class="button__text" and contains(text(), "Добавить сегмент")]')
    INPUT_SEGMENT_NAME = (By.XPATH, '//div[@class="input input_create-segment-form"]//input[@type="text"]')
    SUBMIT_CREATE_SEGMENT = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать сегмент")]')
    SUBMIT_DELETE = (By.XPATH, '//div[@class="button__text" and contains(text(), "Удалить")]')
