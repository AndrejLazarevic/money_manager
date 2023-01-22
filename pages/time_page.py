from appium.webdriver.common.appiumby import AppiumBy
from driver.driver_object import DriverObject
from base.mobile_element import MobileElement
from base.mobile_page import MobilePage


class TimePage(MobilePage):

    def __init__(self, locator_type=AppiumBy.ACCESSIBILITY_ID, locator_name='', page_name='Time Page'):
        super().__init__(locator_type=locator_type, locator_name=locator_name, page_name=page_name)
        driver = DriverObject.get_driver()
        self.driver = driver

        self.time_hours_switch = MobileElement(AppiumBy.ID, 'android:id/hours', 'Hours Switch')
        self.time_minutes_switch = MobileElement(AppiumBy.ID, 'android:id/minutes', 'Minutes Switch')
        self.time_am_switch = MobileElement(AppiumBy.ID, 'android:id/am_label', 'AM Switch')
        self.time_pm_switch = MobileElement(AppiumBy.ID, 'android:id/pm_label', 'PM Switch')

        self.toggle_text_mode = MobileElement(AppiumBy.XPATH,
                                              '//android.widget.ImageButton[@content-desc="Switch to text input mode for the time input."]',
                                              'Text Mode Toggle')
        self.toggle_clock_mode = MobileElement(AppiumBy.XPATH,
                                               '//android.widget.ImageButton[@content-desc="Switch to clock mode for the time input."]',
                                               'Clock Mode Toggle')

        self.time_hours_input = MobileElement(AppiumBy.ID, 'android:id/input_hour', 'Hours Input')
        self.time_minutes_input = MobileElement(AppiumBy.ID, 'android:id/input_minute', 'Minutes Input')
        self.time_am_pm_button = MobileElement(AppiumBy.ID, 'android:id/am_pm_spinner', 'AM/PM Select Button')
        self.time_am_option = MobileElement(AppiumBy.XPATH, '//android.widget.CheckedTextView[1]', 'AM Option')
        self.time_pm_option = MobileElement(AppiumBy.XPATH, '//android.widget.CheckedTextView[2]', 'PM Option')

    def switch_to_text_mode(self):
        self.toggle_text_mode.wait_for_element()
        self.toggle_text_mode.click()

    def switch_to_clock_mode(self):
        self.toggle_clock_mode.wait_for_element()
        self.toggle_clock_mode.click()

    def set_time_in_text_mode_to(self, time):
        split = time.split(":")
        hours = split[0]
        minutes = split[1].split(' ')[0]
        period = split[1].split(' ')[1]

        self.time_hours_input.send_text(hours)
        self.time_minutes_input.send_text(minutes)
        self.time_am_pm_button.click()
        if period == "PM":
            self.time_pm_option.wait_for_element()
            self.time_pm_option.click()
        else:
            self.time_am_option.wait_for_element()
            self.time_am_option.click()

    def verify_time_is_set_to(self, time):
        split = time.split(":")
        hours = split[0]
        minutes = split[1].split(' ')[0]
        period = split[1].split(' ')[1]

        self.time_hours_switch.assert_text_to_equal(hours)
        self.time_minutes_switch.assert_text_to_equal(minutes)
        if period == "PM":
            self.time_pm_switch.assert_checked()
            self.time_am_switch.assert_not_checked()
        else:
            self.time_am_switch.assert_checked()
            self.time_pm_switch.assert_not_checked()
