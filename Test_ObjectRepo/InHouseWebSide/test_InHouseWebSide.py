from typing import Type

import pytest

from App_ObjectRepo.InHouseWebSide.CentralWebsideCall import CWC


def test_ContactusForm(driver, config, websites):
    obj = CWC(driver)
    ur = get_url(str(websites))
    obj.get_webside(websites).contactus_form(url=config[f'{ur.get("url")}'], name="Divyesh Patel",
                                             emailed="divyesh.patel@codezeros.com",
                                             phone="1234567890", skypeID="Test SkypeID",
                                             project_des="QA Team doing Testing On this")


@pytest.fixture(params=["codezeros"])
def websites(request):
    return request.param


def get_url(web):
    result = dict()
    if web == "codezeros":
        result["url"] = 'curl'
        return result
    else:
        print("Url Not Found")

