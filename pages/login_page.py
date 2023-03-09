from appium.webdriver.common.appiumby import AppiumBy

from base.mobile_element import MobileElement
from base.mobile_page import MobilePage
from driver.driver_object import DriverObject


class LoginPage(MobilePage):

    def __init__(self, page_name='Login Page'):
        super().__init__(page_name=page_name)
        self.driver = DriverObject.get_driver()

        self.back_button = MobileElement(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                                         ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                         ".FrameLayout/android.widget.FrameLayout/android.view.View"
                                                         "/android.view.View/android.view.View/android.view.View"
                                                         "/android.view.View[1]/android.widget.Button", "Back button")
        self.login_title = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Log in', "Log in title")
        self.enter_email_label = MobileElement(AppiumBy.ACCESSIBILITY_ID,
                                               'Please enter the email address you registered with',
                                               "Enter email label")
        self.email_input = MobileElement(AppiumBy.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                         '/android.view.View/android.view.View/android.view.View/android.view.View'
                                         '/android.widget.EditText', "Email input")
        self.next_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Next', "Next button")
        self.enter_password_label = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Enter your password',
                                                  "Enter password label")
        self.password_input = MobileElement(AppiumBy.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                         '/android.view.View/android.view.View/android.view.View/android.view.View'
                                         '/android.widget.EditText', "Password input")
        self.forgot_password_link = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Forgot your password?',
                                                  "Forgot password link")

    def log_in(self, email, password):
        self.email_input.wait_for_element()
        self.next_button.assert_not_enabled()
        self.email_input.send_text(email)
        self.next_button.assert_enabled()
        self.next_button.click()
        self.password_input.wait_for_element()
        self.next_button.assert_not_enabled()
        self.password_input.send_text(password)
        self.next_button.assert_enabled()
        self.next_button.click()
