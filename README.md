# qa-automation-framework
qa-automation-framework



1.Packages need to install
    -Pytest
    -Selenium
    -Appium-Python-Client
    -allure
    -allure-pytest
    -allure-pytest-commons
    -PyYaml
    -hybrid
    -pyscreenrec
    -pandas
    -openpyxl
2.Application in System
    -Python IDE (Any)
    -Java JDK 8 and above
    -allure server
    -Appium server
    -Appium 
    -Appium-Inspector

3.Framework Folder structure 
    -APP_ObjectRepo: POM files of any project
        -Project Folder
            - Module Folder
                - POM files ( .py file)
    -Test ObjectRepo: Testcase files
        -Project Folder
            -Module Folder
                - Testcase files (.py)
    -Utils
        -commonlip.py: For common function use for logic  like delete folder and files , app configuration.
        -config.py For set config method from  Config.yml file
        -global_driver_utility.py For selenium locator's methods like send key , click . element list , Select , Action, Scroll, windows list, etc
    -Config
        -Config.yml : for set configuration parameter like project url, mobile os version, UDID, username,password, etc.
    -Data
        -For additional data files for testcase logic. like Excel file , Json file, etc.
    -Reports
        -For Allure reports flies
    -Download
        -For set download path and any file download from logic
    -conftest.py
        -Base class file for testcase, it has browser selection method , parser.addoption parameter, @pytest.fixture setup and tear down methods, screenshot  and video file attached with report
    -pytest.ini
        -For Pytest configuration
    -runner.py
        -Automation run configuration file.

4.How to Run 
    - For testcase run ,the need to run runner file.
      - configuration of runner file
          run main method from runner.py file. in main method there are pytest parameters set with below list.            
                -parent_dir : os.getcwd()  current directory of  
                -project_dir = os.path.join(parent_dir, 'Test_ObjectRepo', <set for ypu project testcase folder name)
                -pytest.main([project_dir, '--P=now_medical_admin', '-B=ch', '-A=web', '-D=web', '-c', f'{parent_dir}/pytest.ini',
                 f'--alluredir={allure_result_file}',
                 '-v', f'--junitxml={parent_dir}/Reports/xml/allure_results_xml_{date_time}.xml'], )
                    --P=<you project name same yml file configuration>
                    -B=<browser name like chrome, firefox, safari
                    -A=<Web application or Mobile application  need set  web or mobile
                    -D=<Device Name Mobile or PC, set mobile for mobile  and web and desktop for PC>
