import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from pytest_metadata.plugin import metadata_key
import pytest_html.extras


driver = None
@pytest.fixture(scope="class")
def setup(request, browser):
    global driver

    if browser == "edge":
    #     todo add edge driver wala setup
       pass
    elif browser == "chrome":
        chrome_service = ChromeService()
        chrome_options = ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.maximize_window()
        request.cls.driver = driver # abhikk
        print("Launching Chrome Browser..................")
    else:
        chrome_service = ChromeService()
        chrome_options = ChromeOptions()
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.maximize_window()
        print("Launching Chrome Browser..................")

    
    yield driver  # The test will run here

    # Teardown code to close the browser after the entire class
    print("Closing the browser..................")
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser (chrome/edge)")
    parser.addoption("--html-report", action = "store", default = "Reports/HTML_Report.html", help = "path for HTML report")
    


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

# Generate HTML report
def pytest_html_report_title(report):     
    report.title = "Test Automation Report"
def pytest_configure(config):     
    config.option.htmlpath = config.getoption("--html")

def pytest_configure(config):  #Adding new keys in enironment table of HTML report
    config.stash[metadata_key]["Name"] = "Ujjawal Kumar"
    config.stash[metadata_key]["url"] = "https://tutorialsninja.com/demo"

    unwanted_keys = ["JAVA_HOME", "Plugins", "Platform"]  #Removing unwanted keys from environment table of HTML report
    for keys in unwanted_keys:
        config.stash[metadata_key].pop(keys, None)
    

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])

#     if (report.when == 'call' or report.when == "setup") and (report.skipped or report.failed ):
#         report_directory = os.path.dirname(item.config.option.htmlpath)
#         file_name = "screenshot/" + report.nodeid.replace("::", "_") + ".png"
#         file_path = os.path.join(report_directory, file_name)
#         # file_path = f"Screenshots/{report.nodeid.replace(':', '_')}.png"
        
#         try:
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Corrected path and filename
#             driver.save_screenshot(file_path)  # Corrected method call
#         # Construct HTML code to embed the image
#             # extra_html = f'<div><img src="{file_path}" style="width:250px; height:200px;" /></div>'
#             # extra_html = f'<div><img src="{file_path}" alt="screenshot" style="width:600px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
#             # extra.append(pytest_html.extras.html(extra_html))
#             # report.extras = extra

#             allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

#         except Exception as e:
#             print(f"Failed to save Screenshot: {e}")
            
        
        # report.extras = extra
    
# try:
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)
#             from selenium import webdriver  # Import webdriver module
#             # driver = webdriver.Chrome()  # Initialize the webdriver
#             driver.save_screenshot(file_path)
#             extra_html = f'<div><img src="{file_name}" alt="screenshot" style="width:600px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
#             extra.append(pytest_html.extras.html(extra_html))
#             report.extras = extra


# def take_screenshot(self, screenshot_name):
#         allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=AttachmentType.PNG)

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])

#     if (report.when == 'call' or report.when == "setup") and (report.skipped or report.failed ):
#         report_directory = os.path.dirname(item.config.option.htmlpath)
#         file_name = "screenshot/" + report.nodeid.replace("::", "_") + ".png"
#         file_path = os.path.join(report_directory, file_name)

#         try:
#             os.makedirs(os.path.dirname(file_path), exist_ok=True)  
#             driver.save_screenshot(file_path)  

#             screenshot_name = file_path.split("/")[-1]
#             allure.attach(driver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)

#         except Exception as e:
#             print(f"Failed to save Screenshot: {e}")


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()

#     if rep.when == "call" and rep.failed:
#         attach_screenshot(rep.nodeid, rep.message)

# def attach_screenshot(node_id, message):
#     try:
#         file_name = f"screenshot/{node_id}.png"
#         file_path = os.path.join(os.getcwd(), file_name)
#         driver.save_screenshot(file_path)
#         allure.attach(open(file_path, 'rb'), name=file_name, attachment_type=AttachmentType.PNG)
#         #os.remove(file_path)  # Remove the screenshot after it's attached to the report
#     except Exception as e:
#         print(f"Failed to save Screenshot: {e}")

# def pytest_addoption(parser):
#     parser.addoption("--browser", help="Specify the browser")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        mode, concept, _ = item.nodeid.rpartition("::")  # Get the test name
        file_name = f"screenshot/{mode}.png"
        file_path = os.path.join(os.getcwd(), file_name)
        try:
            driver.save_screenshot(file_path)  # Save the screenshot to the file path
            allure.attach(open(file_path, 'rb'), name=file_name, attachment_type=AttachmentType.PNG)
            os.remove(file_path)  # Remove the screenshot after it's attached to the report
        except Exception as e:
            print(f"Failed to save Screenshot: {e}")