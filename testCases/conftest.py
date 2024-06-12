import os
import pytest
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
    config.stash[metadata_key]["url"] = "https://automationteststore.com/"

    unwanted_keys = ["JAVA_HOME", "Plugins", "Platform"]  #Removing unwanted keys from environment table of HTML report
    for keys in unwanted_keys:
        config.stash[metadata_key].pop(keys, None)
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if (report.when == 'call' or report.when == "setup") and (report.skipped or report.failed ):
        file_path = f"Screenshots/{report.nodeid.replace(':', '_')}.png"
        
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Corrected path and filename
            driver.save_screenshot(file_path)  # Corrected method call
        # Construct HTML code to embed the image
            extra_html = f'<div><img src="{file_path}" style="width:250px; height:200px;" /></div>'
            extra.append(pytest_html.extras.html(extra_html))
        except Exception as e:
            print(f"Failed to save Screenshot: {e}")

        
        report.extra = extra
    



