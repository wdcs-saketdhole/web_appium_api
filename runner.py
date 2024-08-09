import datetime
import os
import shutil
import subprocess
from time import sleep
import pytest
from jproperties import Properties
#from hybrid.Cron.config_allure_report import allure_misc_config
from Utils.commonlib import delete_img
from Utils.commonlib import delete_vid
from Utils.commonlib import remove_file
import site
import socket

parent_dir = os.getcwd()
date_time = datetime.datetime.now(datetime.timezone.utc).strftime('%m-%d-%y-%H%M')
date = datetime.datetime.now(datetime.timezone.utc).strftime('%m-%d')
project_dir = os.path.join(parent_dir, 'Test_ObjectRepo', 'zizle')
allure_reports = os.path.join(parent_dir, project_dir, 'Reports')
allure_images = os.path.join(parent_dir, project_dir, 'Images')
ALLURE_HOME = shutil.which("allure")
ANSIBLE_HOME = shutil.which("ansible-playbook")
DOCKER_PATH = os.path.join(os.getcwd(), 'Docker', 'docker.yml')
target_dir = '.venv/lib/python3.10/site-packages/'
site_packages_dirs = site.getsitepackages()

for dir2 in site_packages_dirs:
    if dir2.endswith("site-packages"):
        target_dir = dir2
        break
    else:
        target_dir = '.venv/lib/python3.10/site-packages/'


def main():
    """
    :return:
    1. This main will Delete the Old Images and videos if Present.
    2. This main method will execute Pytest command to execute and run tests mentioned in the Pytest.ini files
    3. This main method will generate allure report from the allure results
    4. This main method will make some modification in the allure report at the end to generate custom allure report.
    """
    allure_file_html_name_old = f'{allure_reports}/html{get_value_from_prop("allure_file_html_name")}'
    allure_result_file = f'{allure_reports}/allure_results-{date_time}'
    allure_html_file = f'{allure_reports}/html/allure_report-html-{date_time}'
    update_prop_file(f'date_time', date_time)
    update_prop_file(f'allure_results', f'allure_results-{date_time}')
    update_prop_file(f'allure_file_html_name', f'allure_report-html-{date_time}')
    pytest.main([project_dir, '--P=ChatWit', '-B=ch', '-A=mo', '-D=mo', '-c' f'{parent_dir}/pytest.ini',
                 f'--alluredir={allure_result_file}',
                 '-v', f'--junitxml={allure_reports}/xml/allure_results_xml_{date_time}.xml'],
                )
    if os.path.exists(allure_result_file):
        if 'history' not in os.listdir(allure_result_file):
            os.mkdir(f'{allure_result_file}/history')
    copy_tree(src=allure_file_html_name_old, destination=allure_result_file)
    sleep(2)
    update_prop_file('allure_file_html_name', f'allure_report-html-{date_time}')
    if ALLURE_HOME is None:
        ALLURE = get_value_from_prop('allure_home')
        try:
            subprocess.call([f'{ALLURE}', 'generate', allure_result_file, '-o', allure_html_file, '--clean'])
        except FileNotFoundError as e:
            print(e)
    else:
        try:
            subprocess.call([f'{ALLURE_HOME}', 'generate', allure_result_file, '-o', allure_html_file, '--clean'])
        except FileNotFoundError as e:
            print(e)
    sleep(2)
    #allure_misc_config(allure_html_file)
    subprocess.run([f'{ALLURE_HOME}', 'open', allure_html_file, '--host', get_ipv4_address(), '--port', '4444'])


def update_prop_file(key, val):
    CONFIG_FILE_PATH_PROP = os.path.join('Utils', 'allure.properties')

    prop_config = Properties()
    with open(CONFIG_FILE_PATH_PROP, 'rb') as r_file:
        prop_config.load(r_file)

        data = prop_config.get(key).data
        print(f'Current Data in the {key}:: {data} ===')
    prop_config[key] = val
    with open(CONFIG_FILE_PATH_PROP, 'wb') as w_file:
        prop_config.store(w_file)
        data = prop_config.get(key).data
        print(f'New value of {key}:: {data}')


def get_value_from_prop(key):
    CONFIG_FILE_PATH_PROP = os.path.join('Utils', 'allure.properties')

    with open(CONFIG_FILE_PATH_PROP, 'r') as file:
        for line in file.readlines():
            if key in line:
                file_path = line.split('=')[1].strip()
                return file_path


def copy_tree(src, destination):
    if os.path.exists(src):
        root_dir = os.listdir(src)
        for dirs in root_dir:
            if dirs == 'history':
                shutil.copytree(src=f'{src}/history', dst=f'{destination}/history', dirs_exist_ok=True)
                break


def get_ipv4_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ipv4_address = s.getsockname()[0]
        s.close()
        return ipv4_address
    except socket.error as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    if not os.path.exists(allure_reports):
        os.makedirs(allure_reports)
    if not os.path.exists(allure_images):
        os.makedirs(allure_images)
    remove_file(allure_reports)
    remove_file(allure_images)
    main()
