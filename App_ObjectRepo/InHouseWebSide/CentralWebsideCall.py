from App_ObjectRepo.InHouseWebSide.codezeros import CodeZeros


class CWC:

    def __init__(self, driver):
        self.driver = driver
        self.__obj = None

    def get_webside(self,websitename):
        self.__obj = Websites_Call(self.driver).get_website_obj(websitename)
        return self

    def contactus_form(self, url, name, emailed, phone, skypeID, project_des):
        self.__obj.ContactUS_Form(url, name, emailed, phone, skypeID, project_des)


class Websites_Call:

    def __init__(self, driver):
        self.driver = driver

    def get_website_obj(self, website_name):
        if website_name == 'codezeros':
            return CodeZeros(self.driver)
        else:
            print("Wrong Webside added")


