import time

import allure
import pytest

from App_ObjectRepo.ChatWit.LoginPage import Login


@allure.title("Verify the Login")
@pytest.mark.run(order=2)
class Test_Login:
    loginP = Login

    @allure.title("Verify Login With Wrong Password")
    def test_loginvalidation_wrongpassword(self, driver):
        time.sleep(2)
        Test_Login.loginP(driver).click_loginbt()
        Test_Login.loginP(driver).login_validation("divyesh.patel@codezeros.com", "Test@34")

    @allure.title("Verify Login With Wrong email")
    def test_loginvalidation_wrongemail(self, driver):
        time.sleep(2)
        Test_Login.loginP(driver).login_validation("divyesh.pa@codezeros.com", "Test@123456")

    @allure.title("Verify invalid email format")
    def test_loginvalidation_invalidemail(self, driver):
        time.sleep(2)
        Test_Login.loginP(driver).login_email_validation("divyesh.patelcoderzeros")

    @allure.title("Verify invalid password format")
    def test_loginvalidation_invalidpassword(self, driver):
        time.sleep(2)
        Test_Login.loginP(driver).login_password_validation("Test@1")

    @allure.title("Verify the  Login")
    def test_login(self, driver):
        Test_Login.loginP(driver).login_from("divyesh.patel@codezeros.com", "Test@123456",
                                             "Chatwit | AI-powered chatbot to boost user engagement")

    # @allure.title("Verify the Logout")
    # def test_logout(self, driver,config):
    #     time.sleep(2)
    #     Test_Login.loginP(driver).get_logout("Chatwit | AI-powered chatbot to boost user engagement")
    #     time.sleep(1)

