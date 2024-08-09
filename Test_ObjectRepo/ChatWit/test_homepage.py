import allure
import pytest

from App_ObjectRepo.ChatWit.HomePage import HomePage


@pytest.mark.run(order=1)
class Test_HomePage:
    homepage = HomePage

    def test_homepage(self, driver, config):
        Test_HomePage.homepage(driver).launch_url(config['url'])
