import time
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GlobalLocator:
    maps = {}

    def __init__(self, driver):
        self.driver = driver
        self.window_handles = driver.window_handles
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for_visibility_of_ele(self, ele):
        self._wait.until(EC.visibility_of(ele))

    def launch_url(self, url):
        self.driver.get(url)

    def send_key(self, *args, value):
        self.driver.find_element(*args).send_keys(value)

    def click(self, *args):
        self.driver.find_element(*args).click()

    def gettext(self, *args):
        text = self.driver.find_element(*args).text()
        return text

    def clear(self, *args):
        self.driver.find_element(*args).clear()

    def element_list(self, *args):
        listofelement = self.driver.find_elements(*args)
        return listofelement

    def enterkey(self, *args):
        self.driver.find_element(*args).send_keys(Keys.ENTER)

    def mouse_rightKey(self, *args):
        self.driver.find_element(*args).send_keys(Keys.ENTER)

    def get_window_handles_map(self):
        set_of_handles = self.driver.window_handles
        iterator = iter(set_of_handles)
        pID = next(iterator)
        cID = next(iterator)
        maps = {
            "parentID": pID,
            "childID": cID
        }
        return maps

    def selectByIndex(self, *args, Index):
        sel = Select(self.driver.find_element(*args))
        sel.select_by_index(Index)

    def selectByValue(self, *args, Value):
        sel = Select(self.driver.find_element(*args))
        sel.select_by_value(Value)

    def selectByText(self, *args, Text):
        sel = Select(self.driver.find_element(*args))
        sel.select_by_visible_text(Text)

    def selectByOption(self, *args, path, option):
        sel = Select(self.driver.find_element(*args))
        plist = sel.options
        for x in plist:
            op = str(x.text)
            if op.__contains__(option):
                x.click()

    def scroll_by_visibility_of_element(self, *args, path):
        js = self.driver.execute_script
        js("arguments[0].scrollIntoView();", self.driver.find_element(*args))
        time.sleep(2)

    def scrollToTop(self):
        self.driver.execute_script(self.driver, script="window.scrollTo(document.body.scrollHeight, 0);")

    def alertCancel(self):
        alt = Alert(self.driver)
        alt.accept()

    def attachFile(self, *args, filepath):
        self.driver.find_element(*args).send_keys(filepath)

    def is_element_displayed(self, *args):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(*args)
            )
            # Check if the element is displayed
            return element.is_displayed()
        except:
            return False

    def get_attribute(self, *args, attribute):
        atr = self.driver.find_element(*args)
        return atr.get_attribute(attribute)
