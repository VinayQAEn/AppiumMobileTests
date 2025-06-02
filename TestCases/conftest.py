import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="class")
def setup(request):
    options = UiAutomator2Options()
    options.platformName = "Android"
    options.deviceName = "emulator-5554"
    options.platformVersion = "16"
    options.noReset = True	
    options.fullReset = True
    options.autoGrantPermissions = True
    options.newCommandTimeout = 6000
   

    options.automationName = "UiAutomator2"
    options.app = ("/Users/riyabakoria/Downloads/Meesho_Online_Shopping_App_v14.7.apk")
    





   
    driver = webdriver.Remote("http://localhost:4723", options=options)
    driver.implicitly_wait(30)
    
    # Assign to the class instance
    request.cls.driver = driver

    yield driver
    driver.quit()
    