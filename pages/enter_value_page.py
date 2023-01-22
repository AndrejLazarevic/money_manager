from appium.webdriver.common.appiumby import AppiumBy
from driver.driver_object import DriverObject
from base.mobile_element import MobileElement
from base.mobile_page import MobilePage


class EnterValuePage(MobilePage):

    def __init__(self, locator_type=AppiumBy.ACCESSIBILITY_ID, locator_name='', page_name='Enter Some Value Page'):
        super().__init__(locator_type=locator_type, locator_name=locator_name, page_name=page_name)
        driver = DriverObject.get_driver()
        self.driver = driver

        self.input_enter_some_value = MobileElement(AppiumBy.ID, "com.skill2lead.appiumdemo:id/Et1", "Input")
        self.button_submit = MobileElement(AppiumBy.ID, "com.skill2lead.appiumdemo:id/Btn1", "Submit button")

    def type_in_input_enter_some_value(self, text):
        self.input_enter_some_value.wait_for_element()
        self.input_enter_some_value.send_text(text)

    def clear_input_enter_some_value(self):
        self.input_enter_some_value.wait_for_element()
        self.input_enter_some_value.clear_text()

    def get_text_from_submit(self):
        self.button_submit.wait_for_element()
        text = self.button_submit.get_text()
        return str(text)

    def verify_button_submit_is_visible(self):
        self.button_submit.assert_visible()

    def verify_button_submit_text_is(self, text):
        self.button_submit.assert_text_to_equal(text)

    def verify_button_submit_text_is_not(self, text):
        self.button_submit.assert_text_to_not_equal(text)
