import allure
from selenium.webdriver.common.by import By

from Utils.global_driver_utility import GlobalLocator as gl


class Resister:

    def __init__(self, driver):
        self.driver = driver

    def register_form(self, name, email, number, password):
        self.launch_url()
        self.add_Name(name)
        self.add_email(email)
        self.select_country()
        self.add_mobileNumber(number)
        self.add_password(password)
        self.click_register()
        self.get_title()

    def launch_url(self):
        gl(self.driver).launch_url("https://www.chatwit.ai/register")

    @allure.step("Add User Name")
    def add_Name(self, name):
        byName = (By.XPATH, "//input[@id='name']")
        gl(self.driver).send_key(*byName, value=name)

    @allure.step("Add User Email")
    def add_email(self, email):
        byEmail = (By.XPATH, "")
        gl(self.driver).send_key(*byEmail, value=email)

    @allure.step("Select Country")
    def select_country(self, code):
        byDropdwon = (By.XPATH, "xpath=//div/div[2]")
        byCode = (By.XPATH, "//div[@id='react-select-3-listbox']/div[100]")
        gl(self.driver).click(*byDropdwon)
        gl(self.driver).click(*byCode)

    @allure.step("Add User MobileNumber")
    def add_mobileNumber(self, number):
        byNumber = (By.XPATH, "")
        gl(self.driver).send_key(*byNumber, value=number)

    @allure.step("Add User Password")
    def add_password(self, password):
        byPassword = (By.XPATH, "")
        gl(self.driver).send_key(*byPassword, value=password)

    @allure.step("Click on Register Button")
    def click_register(self):
        byButton = (By.XPATH, "")
        gl(self.driver).click(*byButton)

    @allure.step("Verify The URL Title")
    def get_title(self):
        getCurrentURL = self.driver.current_url
        assert (getCurrentURL.endswith('/login'), '/login')
