from time import sleep
from selenium.webdriver.common.by import By
from pages.base_page import Page


class HomePage(Page):
    TESLA = (By.CSS_SELECTOR, 'a.tds-site-logo-link')
    USER_BTN = (By.CSS_SELECTOR, 'svg.tds-icon.tds-icon-person')

    def open_home_page(self):
        self.open_url('https://www.tesla.com/')

    def click_tesla_logo(self):
        self.find_element(*self.TESLA).click()

    def verify_user_account_btn(self):
        self.find_element(*self.USER_BTN)
