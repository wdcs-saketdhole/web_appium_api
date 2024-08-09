import time

import allure
from selenium.webdriver.common.by import By
from Utils.global_driver_utility import GlobalLocator as gl


class Login:

    def __init__(self, driver):
        self.driver = driver

    def login_from(self, email, password, title):
        self.click_loginbt()
        time.sleep(2)
        byEmail = (By.XPATH, "//input[@name='email']")
        gl(self.driver).clear(*byEmail)
        self.add_email(email)
        byPassword = (By.XPATH, "//input[@id='password']")
        gl(self.driver).clear(*byPassword)
        self.add_password(password)
        self.click_login()
        self.get_title(title)

    def login_validation(self, email, password):
        time.sleep(2)
        byEmail = (By.XPATH, "//input[@name='email']")
        gl(self.driver).clear(*byEmail)
        self.add_email(email)
        byPassword = (By.XPATH, "//input[@id='password']")
        gl(self.driver).clear(*byPassword)
        self.add_password(password)
        self.click_login()
        self.get_validation_message()

    def login_email_validation(self, email):
        time.sleep(2)
        byEmail = (By.XPATH, "//input[@name='email']")
        gl(self.driver).clear(*byEmail)
        self.add_email(email)
        self.get_validation_email()

    def login_password_validation(self, password):
        time.sleep(2)
        byPassword = (By.XPATH, "//input[@id='password']")
        gl(self.driver).clear(*byPassword)
        self.add_password(password)
        self.get_validation_password()

    def register_link(self, title):
        self.click_registerlink()
        self.get_title(title)

    def forgot_password(self, title):
        self.click_forgotpassword()
        self.get_title(title)

    def forgotpassword_sendemail(self, email, title):
        self.add_email(email)
        self.send_email()
        self.get_title(title)

    def get_logout(self,title):
        byAccount = (By.XPATH, "//a[contains(text(),'My Account')]")
        byLogout = (By.XPATH, "//button[contains(text(),'SIGN OUT')]")
        time.sleep(1)
        gl(self.driver).click(*byAccount)
        time.sleep(1)
        gl(self.driver).click(*byLogout)
        self.get_title(title)



    @allure.step("Click on Login Button")
    def click_loginbt(self):
        byloginbt = (By.XPATH, "//a[@id='header_login_btn']")
        gl(self.driver).click(*byloginbt)

    @allure.step("Add User Email as Username")
    def add_email(self, email):
        byEmail = (By.XPATH, "//input[@name='email']")
        gl(self.driver).send_key(*byEmail, value=email)

    @allure.step("Add User Password")
    def add_password(self, password):
        byPassword = (By.XPATH, "//input[@id='password']")
        gl(self.driver).send_key(*byPassword, value=password)

    @allure.step("Click on Login Button")
    def click_login(self):
        byLoginbt = (By.XPATH, "//button[contains(text(),'Login')]")
        gl(self.driver).click(*byLoginbt)

    @allure.step("Click on ForgotPassword")
    def click_forgotpassword(self):
        byLink = (By.XPATH, "//a[contains(text(),'Forgot password?')]")
        gl(self.driver).click(*byLink)

    @allure.step("Click on Register link")
    def click_registerlink(self):
        byRLink = (By.XPATH, "//a[contains(text(),'Register now')]")
        gl(self.driver).click(*byRLink)

    @allure.step("Click on Send Email button")
    def send_email(self):
        bySend = (By.XPATH, "//button[contains(text(),'Send mail')]")
        gl(self.driver).click(*bySend)

    @allure.step("Verify The URL Title")
    def get_title(self, title):
        getCurrentURL = self.driver.title
        assert (getCurrentURL == title)

    @allure.step("Verify the validation message")
    def get_validation_message(self):
        byMessage = (By.CSS_SELECTOR, ".Toastify__toast-body > div:nth-child(2)")
        flag = gl(self.driver).is_element_displayed(*byMessage)
        assert (flag, True)

    @allure.step("Verify the validation message for password")
    def get_validation_password(self):
        byMessage = (By.XPATH, "//p[contains(text(),'Please enter valid password')]")
        flag = gl(self.driver).is_element_displayed(*byMessage)
        assert (flag, True)

    @allure.step("Verify the validation message for email")
    def get_validation_email(self):
        byMessage = (By.XPATH, "//p[contains(text(),'Enter valid email')]")
        flag = gl(self.driver).is_element_displayed(*byMessage)
        assert (flag, True)
