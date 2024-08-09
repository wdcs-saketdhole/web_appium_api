import allure

from Utils.global_driver_utility import GlobalLocator as gl


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def homepage(self, url):
        self.launch_url(url)
        self.get_title()

    @allure.step("Open Url")
    def launch_url(self, url):
        gl(self.driver).launch_url(url)

    @allure.step("Verify the Url title")
    def get_title(self):
        currentUrl = self.driver.title
        assert (currentUrl, "Chatwit | AI-powered chatbot to boost user engagement")
