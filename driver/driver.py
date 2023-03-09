from appium import webdriver


def form_driver():
    desired_capabilities = {
        'platformName': 'Android',
        'appPackage': 'ru.innim.my_finance',
        'appActivity': 'ru.innim.my_finance.MainActivity',
        'automationName': 'UiAutomator2',
        'platformVersion': '12',
        'deviceName': 'Xiaomi Redmi 9',
        'app': '/Appium/money_manager/apk/money_manager.apk'
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    return driver

