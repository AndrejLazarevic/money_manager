from appium.webdriver.common.appiumby import AppiumBy
from driver.driver_object import DriverObject
from base.mobile_element import MobileElement
from base.mobile_page import MobilePage


class ScrollPage(MobilePage):

    def __init__(self, page_name='Scroll Page'):
        super().__init__(page_name=page_name)
        self.driver = DriverObject.get_driver()

        self.button_1 = MobileElement(AppiumBy.XPATH, '//*[contains(@text,"BUTTON1")][@index ="1"]', "Button 1")
        self.button_16 = MobileElement(AppiumBy.XPATH, '//*[contains(@text,"BUTTON16")]', "Button 16")

    def scroll_to_button_16_and_back_to_button_1_and_verify(self):
        self.swipe_down()
        self.button_16.assert_text_to_equal("BUTTON16")
        self.swipe_up()
        self.button_1.assert_text_to_equal("BUTTON1")
