import time

import allure
import pytest

from App_ObjectRepo.ChatWit.AddNewChat import AddNewChat
from App_ObjectRepo.ChatWit.LoginPage import Login


@pytest.mark.run(order=3)
class Test_AddNewChatBot:
    chatbot = AddNewChat
    loginP = Login

    def test_1_addnewchatbot(self, driver, config):
        # time.sleep(2)
        # Test_AddNewChatBot.loginP(driver).login_from("divyesh.patel@codezeros.com", "Test@123456",
        #                                              "Chatwit | AI-powered chatbot to boost user engagement")
        time.sleep(3)
        Test_AddNewChatBot.chatbot(driver).addnewchat(config['url'])

    def test__2_crawling(self, driver):
        Test_AddNewChatBot.chatbot(driver).add_crawl_url('testtest.com')
        time.sleep(3)
        Test_AddNewChatBot.chatbot(driver).validate_crawl_url()

    def test_3_crawling(self, driver, config):
        Test_AddNewChatBot.chatbot(driver).add_crawl_url(config['curl'])
        Test_AddNewChatBot.chatbot(driver).click_fetch()
        time.sleep(2)
        Test_AddNewChatBot.chatbot(driver).validate_fetch()
        Test_AddNewChatBot.chatbot(driver).validation_toast_message()
        time.sleep(25)

    @pytest.mark.skip
    def test_4_deletelink(self, driver):
        time.sleep(1)
        Test_AddNewChatBot.chatbot(driver).delete_crawl_link()
        time.sleep(1)
        Test_AddNewChatBot.chatbot(driver).validation_toast_message()

    def test_5_createchatbot(self, driver, config):
        time.sleep(1)
        Test_AddNewChatBot.chatbot(driver).create_chat()
        time.sleep(5)
        Test_AddNewChatBot.chatbot(driver).get_addchat_url(config['url'] + "/price")

    #@pytest.mark.skip
    def test_6_selctplan(self, driver, config):
        time.sleep(2)
        #Test_AddNewChatBot.chatbot(driver).select_plan()
        #time.sleep(2)
        Test_AddNewChatBot.chatbot(driver).validate_select_plan()
        time.sleep(2)
        Test_AddNewChatBot.chatbot(driver).click_next()
        time.sleep(2)
        Test_AddNewChatBot.chatbot(driver).get_addchat_url(config['url'] + "/chatbot-interface")
        time.sleep(2)

    def test_7_chatbotinterface(self, driver):
        Test_AddNewChatBot.chatbot(driver).modify_initial_message()
        time.sleep(2)

