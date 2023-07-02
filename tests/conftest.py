import pytest
from appium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    caps = {}
    caps["appium:deviceName"] = "Pixel 5"
    caps["appium:udid"] = "emulator-5554"
    caps["appium:appPackage"] = "com.pozitron.hepsiburada"
    caps["appium:appActivity"] = "com.hepsiburada.ui.startup.SplashActivity"
    caps["appium:app"] = "/Users/dogukandere/Desktop/hepsiburada.apk"
    caps["platformName"] = "Android"
    caps["appium:automationName"] = "UiAutomator2"
    caps["appium:autoAcceptAlerts"] = True
    caps["appium:noReset"] = True
    driver = webdriver.Remote("http://0.0.0.0:4723", caps)
    request.cls.driver = driver
    driver.implicitly_wait(15)
    yield
    driver.quit()