from appium import webdriver


def get_driver():
    desired_capabilities = {
        'platformName': 'Android',
        'appPackage': 'com.skill2lead.appiumdemo',
        'appActivity': 'com.skill2lead.appiumdemo.MainActivity',
        'automationName': 'UiAutomator2',
        'platformVersion': '11',
        'deviceName': 'Xiaomi Redmi 9',
        'app': '/Appium/test_app/apk/test_app.apk'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    return driver

