import time

import allure
import pytest
from App_ObjectRepo.NowMedical.Admin.home_page import HomePage

@allure.testcase("Verify the Home page")
def test_homepage(driver, config):
    time.sleep(1)
    home_page = HomePage(driver)
    home_page.open(config['url'])
    time.sleep(3)
    assert home_page.get_titel() == 'Now-Medical | '
