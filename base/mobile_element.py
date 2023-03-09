from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

from driver.driver_object import DriverObject
from utilities.logger import log


class MobileElement:

    def __init__(self, locator_type, locator_name, element_name=None):
        self.driver = DriverObject.get_driver()
        self.locator_type = locator_type
        self.locator_name = locator_name
        self.element_name = element_name if element_name is not None else locator_name

    # Find and Wait
    def get_element(self):
        return self.driver.find_element(self.locator_type, self.locator_name)

    def wait_for_element(self, seconds=30):
        wait = WebDriverWait(self.driver, seconds, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        log("Waiting for {0}.".format(self.element_name))
        element = wait.until(lambda x: x.find_element(self.locator_type, self.locator_name))
        return element

    # Actions
    def click(self):
        element = self.get_element()
        element.click()
        log("Clicking on {0}.".format(self.element_name))

    def long_click(self):
        element = self.get_element()
        action = TouchAction(self.driver)
        action.long_press(element).perform()
        log("Long clicking on {0}.".format(self.element_name))

    def send_text(self, text):
        element = self.get_element()
        element.send_keys(text)
        log("Typing '{0}' into {1}.".format(text, self.element_name))

    def get_text(self):
        element = self.get_element()
        if element.text is None:
            text = str(element.text)
        else:
            text = str(element.get_attribute('content-desc'))

        log("Getting text from {0}.".format(self.element_name))
        return text

    def clear_text(self):
        element = self.get_element()
        element.clear()
        log("Cleared text from {0}.".format(self.element_name))

    def set_value(self, value):
        element = self.get_element()
        element.set_value(value)
        log("Set value {0} to the {1}.".format(value, self.element_name))

    # Assertions
    def assert_visible(self):
        element = self.get_element()
        assert element.is_displayed() is True
        log("Element {0} is visible.".format(self.element_name))

    def assert_not_visible(self):
        element = self.get_element()
        assert element.is_displayed() is False
        log("Element {0} is not visible.".format(self.element_name))

    def assert_text_to_equal(self, text):
        element_text = self.get_text()
        log("Asserting if {0} is equal to {1}.".format(element_text, text))
        assert element_text == text

    def assert_text_to_not_equal(self, text):
        element_text = self.get_text()
        log("Asserting if {0} is not equal to {1}.".format(element_text, text))
        assert element_text != text

    def assert_selected(self):
        element = self.get_element()
        assert element.is_selected() is True
        log("Element {0} is selected.".format(self.element_name))

    def assert_not_selected(self):
        element = self.get_element()
        assert element.is_selected() is False
        log("Element {0} is not selected.".format(self.element_name))

    def assert_checked(self):
        element = self.get_element()
        checked = element.get_attribute('checked')
        assert checked == 'true'
        log("Element {0} is checked.".format(self.element_name))

    def assert_not_checked(self):
        element = self.get_element()
        checked = element.get_attribute('checked')
        assert checked == 'false'
        log("Element {0} is not checked.".format(self.element_name))

    def assert_enabled(self):
        element = self.get_element()
        enabled = element.get_attribute('enabled')
        assert enabled == 'true'
        log("Element {0} is enabled.".format(self.element_name))

    def assert_not_enabled(self):
        element = self.get_element()
        enabled = element.get_attribute('enabled')
        assert enabled == 'false'
        log("Element {0} is not enabled.".format(self.element_name))
