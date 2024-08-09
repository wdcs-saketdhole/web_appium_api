from App_ObjectRepo.zizle.login_email import login
from appium import webdriver
from App_ObjectRepo.zizle.signup_email import signup_email
from Utils.commonlib import get_otp_from_db
from Utils.config import load_config
from time import sleep
from Utils.commonlib import random_str

import pytest


class Test_login_email:
    rs=random_str()
    email="script"+rs+"@yopmail.com"
    print(email)
    pwd="Test@123"
    dob="19/05/1996"
    uname=rs
    dname=rs


    @pytest.mark.run(order=1)
    def test_enter_email(self,driver):
        obj_email=login(driver)
        obj_email.CLICK_PHONE_OR_EMAIL()
        obj_email.ENTER_EMAIL(self.email)
        obj_email.CLICK_EMAIL_CONTINUE_BUTTON()
        sleep(2)

    @pytest.mark.run(order=2)
    def test_enter_otp(self,driver):
        obj_enter_otp=signup_email(driver)
        otp=get_otp_from_db(self.email)
        print(otp)
        obj_enter_otp.ENTER_OTP(otp)

    @pytest.mark.run(order=3)
    def test_enter_password(self,driver):
        obj_enter_pwd=signup_email(driver)
        obj_enter_pwd.ENTER_PASSWORD(self.pwd)


    @pytest.mark.run(order=4)
    def test_continue(self,driver):
        obj_click=signup_email(driver)
        obj_click.CLICK_PASSWORD_CONTINUE()

    @pytest.mark.run(order=5)
    def test_enterdob(self,driver):
        obj_click = signup_email(driver)
        obj_click.SET_DOB(self.dob)

    @pytest.mark.run(order=6)
    def test_dobcontinue(self,driver):
        obj_click = signup_email(driver)
        obj_click.CLICK_DOB_CONTINUE()

    @pytest.mark.run(order=7)
    def test_enter_displayname(self,driver):
        obj_click = signup_email(driver)
        obj_click.ENTER_DISPLAYNAME(self.dname)

    @pytest.mark.run(order=8)
    def test_enter_username(self,driver):
        obj_click = signup_email(driver)
        obj_click.ENTER_USERNAME(self.uname)

    @pytest.mark.run(order=9)
    def test_click(self,driver):
        obj_click = signup_email(driver)
        obj_click.CLICK_NAME_CONTINUE_BUTTON()

    @pytest.mark.run(order=10)
    def test_skip_invitation(self,driver):
        obj_click = signup_email(driver)
        obj_click.CLICK_SKIP_CODE()

    @pytest.mark.run(order=11)
    def test_skip_wallet(self,driver):
        obj_click = signup_email(driver)
        obj_click.CLICK_SKIP_WALLET()









