from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


# Given Steps
@given('Open Home Page')
def open_home_page(context):
    context.app.home_page.open_home_page()


# When Steps
@when('Click the TESLA Logo')
def click_tesla_logo(context):
    context.app.home_page.click_tesla_logo()


# Then Steps
@then('Verify user account BTN appears')
def verify_user_account_btn(context):
    context.app.home_page.verify_user_account_btn()
