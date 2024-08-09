import time

from selenium.webdriver.common.by import By

from Utils.global_driver_utility import GlobalLocator
import allure


class LoginAdmin:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Login")
    def login(self, username, password):
        byUser = (By.CSS_SELECTOR, '#login_form > div:nth-child(3) > input')
        byPass = (By.CSS_SELECTOR, '#login_form > div:nth-child(4) > input')
        byLogin = (By.ID, 'kt_login_singin_form_submit_button')
        GlobalLocator(self.driver).send_key(byUser, value=username)
        GlobalLocator(self.driver).send_key(byPass, value=password)
        GlobalLocator(self.driver).click(*byLogin)
        time.sleep(1)

    def get_title(self):
        return self.driver.title
