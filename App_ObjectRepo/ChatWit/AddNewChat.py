import time

import allure
from selenium.webdriver.common.by import By

from Utils.global_driver_utility import GlobalLocator as gl


class AddNewChat:

    def __init__(self, driver):
        self.driver = driver

    def addnewchat(self, url):
        self.click_addnewchat()
        time.sleep(2)
        self.get_addchat_url(url + "/data-sources")


    @allure.step("Click on AddNewChat button")
    def click_addnewchat(self):
        byAddNewChat = (By.XPATH, "//button[contains(text(),'ADD new chatbot')]")
        gl(self.driver).click(*byAddNewChat)

    @allure.step("Verify current page appear")
    def get_addchat_url(self, currentUrl):
        getCurrentURL = self.driver.current_url
        print(getCurrentURL)
        assert (getCurrentURL, currentUrl)

    @allure.step("Add Crawling Url")
    def add_crawl_url(self, url):
        byUrl = (By.XPATH, "//input[@name='url']")
        gl(self.driver).clear(*byUrl)
        time.sleep(2)
        gl(self.driver).send_key(*byUrl, value=url)
        time.sleep(2)

    @allure.step("Varify invalid url")
    def validate_crawl_url(self):
        byAlert = (By.XPATH, "//p[contains(text(),'URL must be valid')]")
        flag = gl(self.driver).is_element_displayed(*byAlert)
        print(flag)
        assert (flag, True)

    @allure.step("Clcik on Fetch Link")
    def click_fetch(self):
        byFetch = (By.XPATH, "//button[contains(text(),'Fetch Links')]")
        gl(self.driver).click(*byFetch)

    @allure.step("Validate fetch link")
    def validate_fetch(self):
        byProgress = (By.XPATH, "//body/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]")
        flag = gl(self.driver).is_element_displayed(*byProgress)
        assert (flag, True)

    @allure.step("Click on Create Chat")
    def create_chat(self):
        byCreate = (By.XPATH, "//button[contains(text(),'Create chatbot')]")
        gl(self.driver).click(*byCreate)

    @allure.step("Verify the Chatbot create")
    def validate_createchatbot(self):
         currenturl = gl(self.driver)

    @allure.step("Verify the validation message")
    def validation_toast_message(self):
        byMessage = (By.CSS_SELECTOR, ".Toastify__toast-body > div:nth-child(2)")
        flag = gl(self.driver).is_element_displayed(*byMessage)
        assert (flag, True)

    @allure.step("Delete Crawl links")
    def delete_crawl_link(self):
        byDelete = (By.XPATH, "//body/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]")
        gl(self.driver).click(*byDelete)

    @allure.step("Select Plan")
    def select_plan(self):
        byGetstart = (By.XPATH, "//button[contains(text(),'Upgrade plan')]")
        elements = gl(self.driver).element_list(*byGetstart)
        if elements:
            elements[0].click()


    @allure.step("Validate the Selection plan")
    def validate_select_plan(self):
        byActive = (By.XPATH, "//button[contains(text(),'ACTIVE PLAN')]")
        flag = gl(self.driver).is_element_displayed(*byActive)
        assert (flag, True)

    @allure.step("Click on Next")
    def click_next(self):
        byNext = (By.XPATH, "//button[contains(text(),'Next')]")
        gl(self.driver).click(*byNext)

    @allure.step("Modify the Initial message")
    def modify_initial_message(self):
        byInitial = (By.XPATH, "//input[@name = 'widgetConfig.initialMessage']")
        gl(self.driver).clear(*byInitial)
        gl(self.driver).send_key(*byInitial, value="Hello Divyesh,  how can i help you?")

    @allure.step("Validate Initial Message Changes")
    def validate_initial_message(self):
        byMessage = (By.XPATH, "//div[contains(text(),'Hello Divyesh,  how can i help you?')]")
        message = gl(self.driver).gettext(*byMessage)
        assert (message, "Hello Divyesh,  how can i help you?")

    @allure.step("Modify the Display Name")
    def modify_display_name(self):
        byName = (By.XPATH, "//input[@name='widgetConfig.headerName']")
        gl(self.driver).clear(*byName)
        gl(self.driver).send_key(*byName, value="QA ChatWit")

    @allure.step("Validate Display Name Change")
    def validate_display_name(self):
        byName = (By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/h2[1]")
        header = gl(self.driver).gettext(*byName)
        assert (header, "QA ChatWit")

    @allure.step("Add Company Name")
    def add_company_name(self):
        byName = (By.XPATH, "//input[@name='name']")
        gl(self.driver).send_key(*byName, value=" QA Team")

    @allure.step("Validate Company Name")
    def validate_company_name(self):
        byAlert = (By.XPATH, "//p[contains(text(),'Please enter company name')]")
        gl(self.driver).is_element_displayed(*byAlert)

    @allure.step("Save the chat's changes")
    def save_changes(self):
        bySave = (By.XPATH, "//button[contains(text(),'Save Changes')]")
        gl(self.driver).click(*bySave)

    @allure.step("Launch ChatBot")
    def launch_chatbot(self):
        byLaunch = (By.XPATH, "//button[contains(text(),'Launch Chatbot')]")
        gl(self.driver).click(*byLaunch)

    def chatbot_id(self):
        byID = (By.CSS_SELECTOR, "div.text-base.Sora-sb.break-all")
        return gl(self.driver).gettext(*byID)

    @allure.step("Verify the Chatbot ID")
    def launch_chatbot_id(self):
        byID = (By.TAG_NAME, "code")
        code = gl(self.driver).gettext(*byID)
        assert (str(self.chatbot_id) in code)

    @allure.step("Go To DashBord")
    def click_GotoDashboard(self):
        byDashboard = (By.XPATH, "//a[contains(text(),'Go to Dashboard')]")
        gl(self.driver).click(*byDashboard)

    @allure.step("Varify ChatBot Create with active")
    def validate_chatbot_active(self):
        byActive = (By.XPATH, "//input[@name='taglinevalue']")
        attribute = gl(self.driver).get_attribute(*byActive, attribute="checked")
        assert (attribute, "")

    @allure.step("Delete the ChatBoat")
    def delete_chatbot(self):
        byDelete = (By.XPATH, "//button[@title = 'delete chatbot']")
        gl(self.driver).click(*byDelete)
        byDeletebt = (By.XPATH, "//button[contains(text(),'DELETE')]")
        gl(self.driver).click(*byDeletebt)
