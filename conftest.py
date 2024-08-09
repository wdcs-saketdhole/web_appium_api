import inspect
import logging
import os
import time
from datetime import date, datetime
from logging import Logger
import allure
import cv2
import numpy as np
import pytest
import requests
from PIL import ImageGrab
import pyscreenrec
import subprocess
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import Utils.config
import runner
from Utils import commonlib
from Utils.config import load_config
from appium import webdriver as appiumdriver
from appium.options.android import UiAutomator2Options

PROJECT_PATH = os.path.abspath(os.curdir)
OUTPUT_DIR = os.path.join(PROJECT_PATH, "Test_ObjectRepo")
screenshots_dirI = os.path.join(OUTPUT_DIR, "Images")
screenshots_dirV = os.path.join(OUTPUT_DIR, "Videos")

import pytest




def pytest_addoption(parser):
    parser.addoption("-D", '--device', action="store", default="default", help="Environment to run tests against")
    parser.addoption("-A", '--application', action="store", default="default", help="Environment to run tests against")
    parser.addoption("--P", action="store", default="default", help="Environment to run tests against")
    parser.addoption("-B", '--browser', action="store", default="default", help="Environment to run tests against")


@pytest.fixture(scope='session')
def config(request):
    """Load configuration based on the command line environment option."""
    env = request.config.getoption("--P")
    return load_config(env)


@pytest.fixture(scope='session')
def driver(config, request):
    Application_name = request.config.getoption('--application')
    Device_type = request.config.getoption('--device')
    Device_name = 'android'
    browser_name = request.config.getoption('--browser')
    if Application_name == 'web':
        if Device_type.startswith('mo'):
            options = UiAutomator2Options()
            options.load_capabilities(commonlib.mobile_config(Device_name, Utils.config.config()))
            driver = appiumdriver.Remote('http://127.0.0.1:4723', options=options)
            driver.maximize_window()
            yield driver
            driver.quit()
        else:
            if browser_name.startswith('c'):
                chrome_options = Options()
                chrome_options.add_experimental_option("useAutomationExtension", False)
                chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
                driver = webdriver.Chrome(chrome_options)
            elif browser_name.startswith('f'):
                geckodriver_path = "/snap/bin/geckodriver"
                driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)
                driver = webdriver.Firefox(service=driver_service)
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")
            driver.maximize_window()
            yield driver
            driver.quit()
    elif Application_name.startswith('mo'):
        options = UiAutomator2Options()
        options.load_capabilities(commonlib.mobileapp_config(Device_name, Utils.config.config()))
        driver = appiumdriver.Remote('http://127.0.0.1:4723', options=options)
        #driver.maximize_window()
        yield driver
        driver.quit()

    elif Application_name.startswith('bs'):
        options = UiAutomator2Options()
        options.load_capabilities(commonlib.mobileapp_config(Device_name,Utils.config.config()))
        driver = appiumdriver.Remote('http://hub.browserstack.com/wd/hub',  options=options)
        #driver.maximize_window()
        yield driver
        driver.quit()
    else:
        driver = webdriver.Chrome()
        yield driver
        driver.quit()
        print("Automation run for APi Testing")


@pytest.fixture(scope="session")
def api_client():
    client = None
    try:
        client = requests.Session()
        yield client
    except Exception as e:
        pytest.fail(f"Failed to initialize API client: {e}")
    finally:
        if client:
            client.close()




@pytest.fixture(scope='function', autouse=True)
def setup_teardown(driver):
    yield
    #driver.delete_all_cookies()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            # Generate a safe file path
            screenshot_name = item.nodeid.replace("::", "_").replace("/", "_") + ".png"
            screenshot_path = os.path.join(screenshots_dirI, screenshot_name)
            driver.save_screenshot(screenshot_path)
            allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)


def record_video(video_path):
    recorder = pyscreenrec.ScreenRecorder()
    try:
        recorder.start_recording(video_path, fps=19)
        time.sleep(1)
    except Exception as e:
        print(f"Error while recording video: {e}")

    finally:
        recorder.stop_recording()


def pytest_ignore_collect(path, config):
    args = config.invocation_params.args
    ignore_files = False
    run_only_api = False

    # Check if '-A=web' or '-A=api' argument is present
    for arg in args:
        if arg.startswith('-A='):
            if arg != '-A=api':
                ignore_files = True
            elif arg == '-A=api':
                run_only_api = True
    rel_path = os.path.relpath(str(path), start=runner.project_dir)

    # If '-A=web' is present, ignore files containing 'api'
    if ignore_files:
        if 'api' in str(rel_path).lower() and path.ext == '.py':
            print(f"Ignoring {path} because it contains 'api'")
            return True

    # If '-A=api' is present, ignore files not containing 'api'
    if run_only_api:
        if 'api' not in str(rel_path).lower() or path.ext != '.py':
            print(f"Ignoring {path} because it does not contain 'api'")
            return True

    return False
