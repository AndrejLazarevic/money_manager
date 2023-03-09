from appium.webdriver.common.appiumby import AppiumBy

from base.mobile_element import MobileElement
from base.mobile_page import MobilePage
from driver.driver_object import DriverObject


class WelcomePage(MobilePage):

    def __init__(self, page_name='Welcome Page'):
        super().__init__(page_name=page_name)
        self.driver = DriverObject.get_driver()

        self.signup_label = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Sign up to save your information",
                                          "Sign up label")
        self.signup_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Sign up', "Sign up button")
        self.login_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Log in", "Log in button")
        self.login_label = MobileElement(AppiumBy.ACCESSIBILITY_ID, "Log in with", "Log in label")
        self.facebook_button = MobileElement(AppiumBy.XPATH,
                                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                             "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                             ".FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]",
                                             "Facebook button")
        self.google_button = MobileElement(AppiumBy.XPATH,
                                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                           ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                                           "/android.view.View/android.view.View/android.view.View/android.view.View"
                                           "/android.widget.ImageView[2]",
                                           "Google button")
        self.apple_button = MobileElement(AppiumBy.XPATH,
                                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                                          "/android.view.View/android.view.View/android.view.View/android.view.View"
                                          "/android.widget.ImageView[3]",
                                          "Apple button")
        self.vk_button = MobileElement(AppiumBy.XPATH,
                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                                       "/android.view.View/android.view.View/android.view.View/android.view.View"
                                       "/android.widget.ImageView[4]",
                                       "VK button")
        self.continue_without_account_button = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                                             "Continue without creating an account",
                                                             "Continue without account label")

    def verify_elements(self):
        self.signup_label.wait_for_element()
        self.signup_label.assert_text_to_equal("Sign up to save your information")
        self.signup_button.assert_text_to_equal("Sign up")
        self.login_button.assert_text_to_equal("Log in")
        self.login_label.assert_text_to_equal("Log in with")
        self.facebook_button.assert_visible()
        self.google_button.assert_visible()
        self.apple_button.assert_visible()
        self.vk_button.assert_visible()
        self.continue_without_account_button.assert_text_to_equal("Continue without creating an account")

    def go_to_signup_page(self):
        self.signup_button.wait_for_element()
        self.signup_button.click()

    def go_to_login_page(self):
        self.login_button.wait_for_element()
        self.login_button.click()
