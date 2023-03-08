from driver.driver_object import DriverObject
from utilities.logger import log


class MobilePage:

    def __init__(self, locator_type=None, locator_name=None, page_name=None):
        self.driver = DriverObject.get_driver()
        self.locator_type = locator_type
        self.locator_name = locator_name
        self.page_name = page_name

    def get_width(self):
        return self.driver.get_window_size()['width']

    def get_height(self):
        return self.driver.get_window_size()['height']

    def swipe(self, x_start, y_start, x_end, y_end):
        self.driver.swipe(x_start, y_start, x_end, y_end)

    def swipe_down(self):
        x_start = self.get_width() / 2
        y_start = self.get_height() / 2
        x_end = x_start
        y_end = self.get_height() / 8
        self.swipe(x_start, y_start, x_end, y_end)
        log("Swiping down")

    def swipe_up(self):
        x_start = self.get_width() / 2
        y_start = self.get_height() / 8
        x_end = x_start
        y_end = self.get_height() / 2
        self.swipe(x_start, y_start, x_end, y_end)
        log("Swiping up")

    def swipe_left(self):
        x_start = self.get_width() / 2
        y_start = self.get_height() / 2
        x_end = self.get_width() / 8
        y_end = y_start
        self.swipe(x_start, y_start, x_end, y_end)
        log("Swiping left")

    def swipe_right(self):
        x_start = self.get_width() / 8
        y_start = self.get_height() / 2
        x_end = self.get_width() / 2
        y_end = y_start
        self.swipe(x_start, y_start, x_end, y_end)
        log("Swiping right")

    def tap_by_coordinates(self, x, y):
        self.driver.tap([(x, y)])

    def hide_keyboard(self):
        self.tap_by_coordinates(1, self.get_height() / 2)
        log('Hide keyboard.')
