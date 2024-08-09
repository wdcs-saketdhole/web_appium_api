from Utils.commonlib import readexcelfile
from App_ObjectRepo.NowMedical.Admin.login_page import LoginAdmin


def test_login(driver, config):
    login_page = LoginAdmin(driver)
    for test in readexcelfile("Data/userdetails.xlsx"):
        username = test.get("username")
        password = test.get("password")
        login_page.login(username, password)
