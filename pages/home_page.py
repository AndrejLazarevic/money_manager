from appium.webdriver.common.appiumby import AppiumBy
from driver.driver_object import DriverObject
from base.mobile_element import MobileElement
from base.mobile_page import MobilePage


class HomePage(MobilePage):

    def __init__(self, page_name='Home Page'):
        super().__init__(page_name=page_name)
        self.driver = DriverObject.get_driver()

        self.button_enter_some_value = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Btn1", "Enter Some Value Button")
        self.button_scroll_view = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Btn3', "Scroll View Button")
        self.button_tab_activity = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Btn4", "Tab Activity Button")
        self.button_long_click = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Btn7", "Long Click Button")
        self.button_time = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Btn8", "Time Button")
        self.button_date = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Btn9", "Date Button")
        self.long_press_alert = MobileElement(AppiumBy.ID, 'android:id/alertTitle', "Long Press alert title")

    def verify_elements(self):
        self.button_enter_some_value.wait_for_element()
        self.button_enter_some_value.assert_text_to_equal("ENTER SOME VALUE")
        self.button_scroll_view.assert_text_to_equal("ScrollView")
        self.button_tab_activity.assert_text_to_equal("TAB ACTIVITY")
        self.button_long_click.assert_text_to_equal("LONG CLICK")
        self.button_time.assert_text_to_equal("TIME")
        self.button_date.assert_text_to_equal("DATE")

    def go_to_scroll_page(self):
        self.button_scroll_view.wait_for_element()
        self.button_scroll_view.click()

    def go_to_enter_some_value_page(self):
        self.button_enter_some_value.wait_for_element()
        self.button_enter_some_value.click()

    def long_click_on_long_click_button_and_verify(self):
        self.button_long_click.long_click()
        self.long_press_alert.assert_text_to_equal('Get your password')

    def go_to_tab_page(self):
        self.button_tab_activity.click()

    def go_to_time_page(self):
        self.button_time.click()

    def go_to_date_page(self):
        self.button_date.click()
