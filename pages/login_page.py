import time

from appium.webdriver.common.appiumby import AppiumBy

from base.mobile_element import MobileElement
from base.mobile_page import MobilePage
from driver.driver_object import DriverObject
from localization.translation import get_translation_for_key


class LoginPage(MobilePage):

    def __init__(self, page_name='Login Page'):
        super().__init__(page_name=page_name)
        self.driver = DriverObject.get_driver()

        self.back_button = MobileElement(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                                         ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                         ".FrameLayout/android.widget.FrameLayout/android.view.View"
                                                         "/android.view.View/android.view.View/android.view.View"
                                                         "/android.view.View[1]/android.widget.Button", "Back button")
        self.login_title = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("login"), "Log in title")
        self.enter_email_label = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                               get_translation_for_key("enter_registrated_email"),
                                               "Enter email label")
        self.email_input = MobileElement(AppiumBy.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                         '/android.view.View/android.view.View/android.view.View/android.view.View'
                                         '/android.widget.EditText', "Email input")
        self.next_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("next"), "Next button")
        self.enter_password_label = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("enter_password"),
                                                  "Enter password label")
        self.password_input = MobileElement(AppiumBy.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                            '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                            '/android.view.View/android.view.View/android.view.View/android.view.View'
                                            '/android.widget.EditText', "Password input")
        self.forgot_password_link = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("forgot_password"),
                                                  "Forgot password link")
        self.incorrect_password_error = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                                      get_translation_for_key("incorrect_password"),
                                                      "Incorrect password error")
        self.invalid_email_error = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("invalid_email"),
                                                 "Invalid email error")

    def log_in_with_valid_data(self, email, password):
        self.login_title.wait_for_element()
        self.login_title.assert_text_to_equal(get_translation_for_key("login"))
        self.next_button.assert_text_to_equal(get_translation_for_key("next"))
        self.enter_email_label.assert_text_to_equal(get_translation_for_key("enter_registrated_email"))
        self.next_button.assert_not_enabled()
        self.email_input.send_text(email)
        time.sleep(1)
        self.next_button.click()
        self.enter_password_label.wait_for_element()
        self.forgot_password_link.assert_text_to_equal(get_translation_for_key("forgot_password"))
        self.enter_password_label.assert_text_to_equal(get_translation_for_key("enter_password"))
        self.next_button.assert_not_enabled()
        self.password_input.send_text(password)
        time.sleep(1)
        self.next_button.click()

    def log_in_with_invalid_email_and_verify_error(self, email):
        self.login_title.wait_for_element()
        self.next_button.assert_not_enabled()
        self.email_input.send_text(email)
        self.invalid_email_error.wait_for_element()
        self.invalid_email_error.assert_text_to_equal(get_translation_for_key("invalid_email"))
        self.next_button.assert_not_enabled()

    def log_in_with_incorrect_password_and_verify_error(self, email, password):
        self.login_title.wait_for_element()
        self.next_button.assert_not_enabled()
        self.email_input.send_text(email)
        time.sleep(1)
        self.next_button.click()
        self.enter_password_label.wait_for_element()
        self.next_button.assert_not_enabled()
        self.password_input.send_text(password)
        self.incorrect_password_error.wait_for_element()
        self.incorrect_password_error.assert_text_to_equal(get_translation_for_key("incorrect_password"))
        self.next_button.assert_enabled()
