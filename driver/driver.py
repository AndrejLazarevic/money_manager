from appium import webdriver

from config import phone_region, app_location, phone_language, android_device, android_os_version


def form_driver():
    desired_capabilities = dict(
        platformName='Android',
        appPackage='ru.innim.my_finance',
        appActivity='ru.innim.my_finance.MainActivity',
        automationName='UiAutomator2',
        platformVersion=android_os_version,
        deviceName=android_device,
        language=phone_language,
        locale=phone_region,
        app=app_location
    )

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    return driver
