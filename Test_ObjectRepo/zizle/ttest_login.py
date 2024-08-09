
from appium import webdriver
from App_ObjectRepo.zizle.login_email import login





class Test_login_email:

    def test_click_login(self, driver):
        obj_click = login(driver)
        obj_click.CLICK_PHONE_OR_EMAIL()


    def test_enter_email(self,driver):
        obj_email=login(driver)
        obj_email.ENTER_EMAIL("saket.zizle@yopmail.com")

    def test_click_email_continue(self,driver):
        obj_continue=login(driver)
        obj_continue.CLICK_EMAIL_CONTINUE_BUTTON()

    def test_enter_pwd(self,driver):
        obj_email=login(driver)
        obj_email.ENTER_PASSWORD("Test@123")

    def test_click_pwd_continue(self,driver):
        obj_pwd_con=login(driver)
        obj_pwd_con.CLICK_PWD_CONTINUE_BUTTON()










