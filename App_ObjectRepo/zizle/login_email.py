from appium import webdriver
from appium.webdriver.common.appiumby import By, AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_flutter_finder import FlutterFinder, FlutterElement




class login:
    xpath_phone_or_email = '//android.widget.ImageView[@content-desc="Use Phone or Email"]'
    key_value_email_inputbox ="email_text_field"
    key_value_emailcontinue_button="email_continue_button"
    key_value_password_inputbox="enter_password_field"
    key_value_pwdcontinue_button="enter_password_continue_button"

    def __init__(self, driver):
        self.driver = driver
        self.finder=FlutterFinder()

    def CLICK_PHONE_OR_EMAIL(self):
        self.driver.switch_to.context('NATIVE_APP')
        self.wait = WebDriverWait(self.driver, timeout=5)
        ele_okay = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath_phone_or_email)))
        ele_okay.click()

    def ENTER_EMAIL(self, email, value_key=None):
        self.driver.switch_to.context('FLUTTER')
        ele_email=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_email_inputbox))
        ele_email.clear()
        ele_email.send_keys(email)

    def CLICK_EMAIL_CONTINUE_BUTTON(self):
        ele_click_continue=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_emailcontinue_button))
        ele_click_continue.click()

    def ENTER_PASSWORD(self,pwd):
        ele_password_inputbox=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_password_inputbox))
        ele_password_inputbox.clear()
        ele_password_inputbox.send_keys(pwd)

    def CLICK_PWD_CONTINUE_BUTTON(self):
        ele_click_continue = FlutterElement(self.driver, self.finder.by_value_key(self.key_value_pwdcontinue_button))
        ele_click_continue.click()












