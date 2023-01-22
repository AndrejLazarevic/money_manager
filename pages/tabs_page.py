from appium.webdriver.common.appiumby import AppiumBy
from driver.driver_object import DriverObject
from base.mobile_element import MobileElement
from base.mobile_page import MobilePage


class TabsPage(MobilePage):

    def __init__(self, locator_type=AppiumBy.ACCESSIBILITY_ID, locator_name='', page_name='Tabs Page'):
        super().__init__(locator_type=locator_type, locator_name=locator_name, page_name=page_name)
        driver = DriverObject.get_driver()
        self.driver = driver

        self.navigation_bar_back_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Navigate up", "Back Button")
        self.navigation_bar_title = MobileElement(AppiumBy.XPATH, '//android.widget.TextView[@text="Tab View"]',
                                                  'Tab View')

        self.home_tab = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Home", "Home Tab")
        self.sport_tab = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Sport", "Sport Tab")
        self.movie_tab = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Movie", "Movie Tab")

        self.home_tab_content_text = MobileElement(AppiumBy.XPATH, '//android.widget.TextView[@text="Home fragment"]',
                                                   'Home fragment')
        self.sport_tab_content_text = MobileElement(AppiumBy.XPATH, '//android.widget.TextView[@text="Sport fragment"]',
                                                    'Sport fragment')
        self.movie_tab_content_text = MobileElement(AppiumBy.XPATH, '//android.widget.TextView[@text="Movie fragment"]',
                                                    'Movie fragment')

    def swipe_tabs_and_verify(self):
        self.home_tab.wait_for_element()
        self.home_tab.assert_selected()
        self.swipe_left()
        self.sport_tab.assert_selected()
        self.swipe_left()
        self.movie_tab.assert_selected()

    def click_on_tabs_and_verify(self):
        self.home_tab.wait_for_element()
        self.home_tab.assert_selected()
        self.sport_tab.click()
        self.sport_tab.assert_selected()
        self.movie_tab.click()
        self.movie_tab.assert_selected()

    def verify_tab_content_text(self):
        self.home_tab_content_text.wait_for_element()
        self.home_tab_content_text.assert_text_to_equal("Home fragment")
        self.swipe_left()
        self.sport_tab_content_text.assert_text_to_equal("Sport fragment")
        self.swipe_left()
        self.movie_tab_content_text.assert_text_to_equal("Movie fragment")

    def go_back_to_home_page(self):
        self.navigation_bar_back_button.wait_for_element()
        self.navigation_bar_back_button.click()
