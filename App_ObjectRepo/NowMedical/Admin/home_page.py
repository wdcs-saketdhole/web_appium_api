from selenium import webdriver
import allure


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Open the url")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Verify the url")
    def get_titel(self):
        return self.driver.title
