import time

import allure
from selenium.webdriver.common.by import By
from Utils.global_driver_utility import GlobalLocator as gl


class CodeZeros:


    def __init__(self, driver):
        self.driver = driver

    def ContactUS_Form(self, url, name, emailed, phone, skypeID, project_des):
        self.open_url(url)
        time.sleep(3)
        self.select_services()
        self.add_name(name)
        self.add_email(emailed)
        self.add_phone(phone)
        self.add_skype(skypeID)
        self.add_ProjectDescription(project_des)
        self.submit_form()
        time.sleep(3)
        self.thankyou_email()

    @allure.step("Launch the URL")
    def open_url(self, url):
        gl(self.driver).launch_url(url)

    @allure.step("Select Service")
    def select_services(self):
        bySelect1 = (By.XPATH, "//span[@class='MultiSelect_placeholder__SgCUD MultiSelect_placeholder-empty__I4PDR']")
        bySelectVal = (By.CSS_SELECTOR, "ul[class*='MultiSelect_options'] li")
        gl(self.driver).click(*bySelect1)
        listOfValue = gl(self.driver).element_list(*bySelectVal)
        listOfValue[1].click()

    @allure.step("Add Name")
    def add_name(self, name):
        byName = (By.ID, "name")
        gl(self.driver).send_key(*byName, value=name)

    @allure.step("Add Email ID")
    def add_email(self, emailid):
        byEmail = (By.ID, 'email')
        gl(self.driver).send_key(*byEmail, value=emailid)

    @allure.step("Add Phone")
    def add_phone(self, phone):
        byPhone = (By.ID, 'number')
        gl(self.driver).send_key(*byPhone, value=phone)

    @allure.step("Add SkypeID")
    def add_skype(self, skype):
        bySkypeID = (By.ID, 'skypeId')
        gl(self.driver).send_key(*bySkypeID, value=skype)

    @allure.step("Add ProjectDescription")
    def add_ProjectDescription(self, project_des):
        byProjDes = (By.CSS_SELECTOR, "textarea[name=description]")
        gl(self.driver).send_key(*byProjDes, value=project_des)

    @allure.step("Submit ContactUs Form")
    def submit_form(self):
        bySubmitbt = (By.XPATH, '//body/div[@id="__next"]/div[1]/main[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[7]/div[1]/button[1]')
        gl(self.driver).click(*bySubmitbt)

    @allure.step("Thank you email")
    def thankyou_email(self):
        getCurrentURL = self.driver.title
        assert (getCurrentURL == 'Thank You - Codezeros')


