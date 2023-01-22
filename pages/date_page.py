from appium.webdriver.common.appiumby import AppiumBy
from driver.driver_object import DriverObject
from base.mobile_element import MobileElement
from base.mobile_page import MobilePage


class DatePage(MobilePage):

    def __init__(self, locator_type=AppiumBy.ACCESSIBILITY_ID, locator_name='', page_name='Date Page'):
        super().__init__(locator_type=locator_type, locator_name=locator_name, page_name=page_name)
        driver = DriverObject.get_driver()
        self.driver = driver

        self.date_header_year = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'android:id/date_picker_header_year',
                                              'Header Year')
        self.date_header_date = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'android:id/date_picker_header_date',
                                              'Header Date')
        self.date_calendar = MobileElement(AppiumBy.ID, 'android:id/month_view', 'Date Calendar')

        self.next_month_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Next month', 'Next Month Button')
        self.previous_month_button = MobileElement(AppiumBy.ACCESSIBILITY_ID, 'Previous month', 'Previous Month Button')

    def select_date_from_future_months_and_verify(self, date, months_into_future):
        self.date_calendar.wait_for_element()
        for month in range(months_into_future):
            self.next_month_button.click()

        target_date = MobileElement(AppiumBy.XPATH, '//android.view.View[@text="' + date + '"]', date)
        target_date.click()
        target_date.assert_checked()

    def select_date_from_past_months_and_verify(self, date, months_into_past):
        self.date_calendar.wait_for_element()
        for month in range(months_into_past):
            self.previous_month_button.click()

        target_date = MobileElement(AppiumBy.XPATH, '//android.view.View[@text="' + date + '"]', date)
        target_date.click()
        target_date.assert_checked()
