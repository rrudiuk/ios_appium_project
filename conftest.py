import pytest
from appium import webdriver

from pathlib import Path


@pytest.fixture(scope="function")
def driver(request):
    """Runs before and after each test. Sets up and quits driver"""
    dc = {}
    driver = None

    # This is the Application and ‘app’ desired capability to specify a path to Appium
    path_to_current_directory = Path().absolute()
    dc['app'] = str(path_to_current_directory) + '/app/app-debug.ipa'
    dc["xcodeOrgId"] = "9AGXVW6QVL"
    dc["xcodeSigningId"] = "iPhone Developer"
    dc["udid"] = "auto"
    dc["platformName"] = "iOS"
    dc["platformVersion"] = "14.6"
    dc["deviceName"] = "Ruslan's iPhone"
    dc["automationName"] = "XCUITest"
    # dc["bundleId"] = "com.logitech.uefits"
    # dc["showIOSLog"] = "true"
    # accept alerts and grant permissions
    # dc['autoAcceptAlerts'] = 'true'
    # dc['autoGrantPermissions'] = 'true'
    # Creating the Driver by passing Desired Capabilities
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)

    yield driver

    print("\nquit driver..")
    driver.quit()
