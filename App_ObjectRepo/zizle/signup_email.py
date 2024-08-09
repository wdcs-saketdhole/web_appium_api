from appium import webdriver
from appium.webdriver.common.appiumby import By, AppiumBy
from appium_flutter_finder import FlutterFinder, FlutterElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class signup_email:
    key_value_otp_inputfield="otp_text_field"
    key_value_password_inputbox = "create_password_field"
    text_password_continue_button="Continue"
    key_value_dob_inputbox="birthday_text_field"
    text_dob_continue_button="Continue"
    key_value_displayname_inputbox="name_text_field"
    key_value_username_inputbox="username_text_field"
    key_value_usernamecontinue_button="username_continue_button"
    text_skip_button="Skip"
    text_skip_wallet="SKIP"
    text_airdroppopoup_go_button="Let's go!"

    
    def __init__(self,driver):
        self.driver=driver
        #self.driver=webdriver.Remote()
        self.finder=FlutterFinder()

    def ENTER_OTP(self,otp):
        ele_otp=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_otp_inputfield))
        print(otp)
        # sleep(3)
        # self.driver.execute_script('flutter:enterText', otp)
        # sleep(2)
        #ele_otp.send_keys(otp)
        try:
            sleep(3)
            self.driver.execute_script('flutter:enterText', otp)
            sleep(2)
            #ele_otp.send_keys(otp)
            print("Sent OTP")
        except Exception as E:
            print(E)
            assert False

    def ENTER_PASSWORD(self,pwd):
        ele_pwd=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_password_inputbox))
        ele_pwd.clear()
        sleep(2)
        ele_pwd.send_keys(pwd)
        sleep(2)

    def CLICK_PASSWORD_CONTINUE(self):
        FlutterElement(self.driver, self.finder.by_text(self.text_password_continue_button)).click()

    def SET_DOB(self,dob):

        ele_dob=FlutterElement(self.driver, self.finder.by_value_key(self.key_value_dob_inputbox))
        ele_dob.clear()
        ele_dob.send_keys(dob)
        #self.driver.execute_script('flutter:enterText', dob)
        sleep(2)
        #ele_dob.send_keys(dob)

    def CLICK_DOB_CONTINUE(self):
        FlutterElement(self.driver, self.finder.by_text(self.text_dob_continue_button)).click()

    def ENTER_DISPLAYNAME(self,dname):
        ele_displayname=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_displayname_inputbox))
        ele_displayname.clear()
        ele_displayname.send_keys(dname)
        #self.driver.execute_script('flutter:enterText', dname)

    def ENTER_USERNAME(self,uname):
        ele_uname=FlutterElement(self.driver,self.finder.by_value_key(self.key_value_username_inputbox))
        ele_uname.clear()
        ele_uname.send_keys(uname)

        #ele_uname.clear()
        #self.driver.execute_script('flutter:enterText', uname)

    def CLICK_NAME_CONTINUE_BUTTON(self):
        FlutterElement(self.driver, self.finder.by_value_key(self.key_value_usernamecontinue_button)).click()


    def CLICK_SKIP_CODE(self):
        FlutterElement(self.driver, self.finder.by_text(self.text_skip_button)).click()
        sleep(1)

    def CLICK_SKIP_WALLET(self):
        FlutterElement(self.driver, self.finder.by_text(self.text_skip_wallet)).click()




    def FIND_GO_BUTTON(self):
        ele_go=FlutterElement(self.driver, self.finder.by_text(self.text_airdroppopoup_go_button))
        try:
            ele_go.click()
        except Exception as E:
            print(E)
            assert False











