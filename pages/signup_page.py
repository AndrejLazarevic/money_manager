import time

from appium.webdriver.common.appiumby import AppiumBy

from base.mobile_element import MobileElement
from base.mobile_page import MobilePage
from driver.driver_object import DriverObject
from localization.translation import get_translation_for_key


class SignupPage(MobilePage):

    def __init__(self, page_name='Sigup Page'):
        super().__init__(page_name=page_name)
        self.driver = DriverObject.get_driver()

        self.back_button = MobileElement(AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                                         "/android.view.View/android.view.View/android.view.View/android.view.View"
                                         "/android.view.View[1]/android.widget.Button",
                                         "Back button")
        self.signup_title = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("signup"), "Sign up title")
        self.enter_email_label = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                               get_translation_for_key("enter_email"),
                                               "Enter email label")
        self.email_input = MobileElement(AppiumBy.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                         '/android.view.View/android.view.View/android.view.View/android.view.View'
                                         '/android.widget.EditText', "Email input")
        self.next_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("next"), "Next button")
        self.create_password_label = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                                   get_translation_for_key("create_password"),
                                                   "Create password label")
        self.re_enter_password_label = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                                     get_translation_for_key("re_enter_password"),
                                                     "Re-enter password label")
        self.password_input = MobileElement(AppiumBy.XPATH,
                                            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                            '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                            '/android.view.View/android.view.View/android.view.View/android.view.View'
                                            '/android.widget.EditText', "Password input")
        self.incorrect_password_error = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                                      get_translation_for_key("incorrect_password"),
                                                      "Incorrect password error")
        self.invalid_email_error = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                                 get_translation_for_key("Invalid email address"),
                                                 "Invalid email error")
        self.thank_you_label = MobileElement(AppiumBy.ACCESSIBILITY_ID, get_translation_for_key("you_are_signed_up"),
                                             "Thank you label")
        self.email_sent_label = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                              get_translation_for_key("we_have_sent_you_email"),
                                              "Email sent label")

    def signup_with_valid_data(self, email, password):
        self.signup_title.wait_for_element()
        self.signup_title.assert_text_to_equal(get_translation_for_key("signup"))
        self.enter_email_label.assert_text_to_equal(get_translation_for_key("enter_email"))
        self.next_button.assert_not_enabled()
        self.email_input.send_text(email)
        time.sleep(1)
        self.next_button.click()
        self.create_password_label.wait_for_element()
        self.create_password_label.assert_text_to_equal(get_translation_for_key("create_password"))
        self.next_button.assert_not_enabled()
        self.password_input.send_text(password)
        time.sleep(1)
        self.next_button.click()
        self.re_enter_password_label.wait_for_element()
        self.re_enter_password_label.assert_text_to_equal(get_translation_for_key("re_enter_password"))
        self.password_input.send_text(password)
        time.sleep(1)
        self.next_button.click()
        self.thank_you_label.wait_for_element()
        self.thank_you_label.assert_text_to_equal(get_translation_for_key("you_are_signed_up"))
        self.email_sent_label.assert_text_to_equal(get_translation_for_key("we_have_sent_you_email"))
        self.hide_keyboard()
