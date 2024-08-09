import shutil

import pandas as rd
import os
import re
import time
from dotenv import load_dotenv
import os
# db_util.py
# db_util.py
from appium import webdriver
import mysql.connector
import string
import random

load_dotenv()
def get_otp_from_db(email):
    try:
        print("Entered for connection")
        print(os.getenv('USERS'))
        print(os.getenv('PASSWORD'))
        print(os.getenv('DATABASE'))

        conn = mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USERS'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE'),
            port=os.getenv('PORT')
        )
        print("Reached")
        cursor = conn.cursor()
        cursor.execute(f"SELECT otp FROM tbl_otp_requests WHERE email='{email}'")
        otp = cursor.fetchone()
        #print(type(otp))
        #cursor.close()
        conn.close()
        if otp:
            return otp[0]
        else:
            raise ValueError("No OTP found")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# otp = get_otp_from_db()
# print(f"Retrieved OTP: {otp}")

def random_str():
    N = 4
    res = ''.join(random.choices(string.ascii_lowercase, k=N))
    return str(res)
# rs=random_str()
# print(rs)
def generate_phone_number():
    first_digit = random.randint(1, 9)
    remaining_digits = random.choices(range(10), k=9)
    phone_number = str(first_digit) + ''.join(map(str, remaining_digits))
    return phone_number


# Example usage
print(generate_phone_number())
def readexcelfile(filepath):
    df = rd.read_excel(filepath)
    data = df.to_dict(orient='records')
    return data


def delete_img():
    # initializing the count
    deleted_files_count = 0

    # specify the path
    path = os.path.join(os.getcwd(), 'Test_ObjectRepo', 'Images')
    png_regex = re.compile('.*.png$')
    for root_dir, folder, files in os.walk(path):
        for file in files:
            if png_regex.match(file):
                print(file)
    print(path)
    # specify the days
    days = 0.25

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # checking whether the file is present in path or not
    try:
        if os.path.exists(path):
            # iterating over each and every folder and file in the path
            for root_folder, folders, files in os.walk(path):
                for file in files:
                    # file path
                    file_path = os.path.join(root_folder, file)
                    # comparing the days
                    if seconds >= get_file_or_folder_age(file_path):
                        # invoking the remove_file function
                        remove_file(file_path)
                        deleted_files_count += 1  # incrementing count
        else:
            # file/folder is not found
            print(f'"{path}" is not found')
    except FileNotFoundError as FNF:
        print(FNF)

    print(f"Total files deleted: {deleted_files_count}")


def delete_vid():
    # initializing the count
    deleted_files_count = 0

    # specify the path
    path = os.path.join(os.getcwd(), 'Test_ObjectRepo', 'Videos')
    webm_regex = re.compile(f'.*.webm$''.*.mp4$')
    for root_dir, folder, files in os.walk(path):
        for file in files:
            if webm_regex.match(file):
                print(file)
    print(path)
    # specify the days
    days = 0.25

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    try:
        # checking whether the file is present in path or not
        if os.path.exists(path):

            # iterating over each and every folder and file in the path
            for root_folder, folders, files in os.walk(path):
                for file in files:
                    # file path
                    file_path = os.path.join(root_folder, file)
                    # comparing the days
                    if seconds >= get_file_or_folder_age(file_path):
                        # invoking the remove_file function
                        remove_file(file_path)
                        deleted_files_count += 1  # incrementing count
        else:
            # file/folder is not found
            print(f'"{path}" is not found')
    except FileNotFoundError as FNF:
        print(FNF)

    print(f"Total files deleted: {deleted_files_count}")


def remove_file(path):
    # removing the file
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def get_file_or_folder_age(path):
    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime

    # returning the time
    return ctime


def mobile_config(Device_name, config):
    if Device_name.startswith('a'):
        capabilities = {
            "platformName": "Android",
            "browserName": "Chrome",
            "appium:platformVersion": config['androidWeb_config']['platformVersion'],
            "appium:automationName": "UiAutomator2",
            "appium:udid": config['androidWeb_config']['udid'],
            "appium:appWaitForLaunch": False,
            "unicodeKeyboard": False,
            "resetKeyboard": False
        }
    else:

        capabilities = {
            "platformName": "iOS",
            "app": "com.google.chrome.ios",
            "appium:platformVersion": config['isoWeb_config']['platformVersion'],
            "appium:automationName": "XCUITest",
            "appium:udid": config['isoWeb_config']['platformVersion'],
            "appium:appWaitForLaunch": False,
            "unicodeKeyboard": False,
            "resetKeyboard": False
        }
    return capabilities


def mobileapp_config(Device_name, config):
    if Device_name.startswith('a'):
        capabilities = {
            "platformName": "Android",
            "app": "/Users/webclues/Saket/Automation_WDCS/app-dev-debug.apk",
            "appium:platformVersion": config['androidWeb_config']['platformVersion'],
            "appium:automationName": "Flutter",
            "appium:udid": config['androidWeb_config']['udid'],
            # "appium:appWaitForLaunch": False, # Can not use this for flutter automation else it'll create issue.
            # "unicodeKeyboard": False,
            # "resetKeyboard": False,
            "autoGrantPermissions": True,
            'noReset': False,
            #'forceAppLaunch': True

        }
    elif Device_name.startswith('bs'):
        capabilities = {
            'bstack:options': {'userName': os.getenv('BS_USER_NAME'),
                               'accessKey': os.getenv('BS_ACCESS_KEY'),
                               'buildName': 'Staging Zizle App',
                               'sessionName': 'Zizle App Launch',
                               'projectName': 'Zizle',
                               'deviceName': 'Google Pixel 3',
                               'osVersion': '9.0'
                               },
            'app': 'bs://2b1d5044676323071569c110cd3e0d8e66e95fb4',
            'automationName': 'Flutter'
        }


    else:

        capabilities = {
            "platformName": "iOS",
            "app": "com.google.chrome.ios",
            "appium:platformVersion": config['androidApp_config']['platformVersion'],
            "appium:automationName": "XCUITest",
            "appium:udid": config['isoApp_config']['udid'],
            "appium:appWaitForLaunch": False,
            "unicodeKeyboard": False,
            "resetKeyboard": False
        }
    return capabilities
