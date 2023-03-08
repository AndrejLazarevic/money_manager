import pytest
from pages.home_page import HomePage
from pages.date_page import DatePage


@pytest.mark.usefixtures("formDriver")
class TestDatePage:

    @pytest.mark.date_next_month
    def test_date_future(self):
        """ Test if you can set the date in the future """
        date = '24'
        months_into_future = 4

        home_page = HomePage()
        home_page.go_to_date_page()

        date_page = DatePage()
        date_page.select_date_from_future_months_and_verify(date, months_into_future)

    @pytest.mark.date_past_month
    def test_date_past(self):
        """ Test if you can set the date in the past """
        date = '13'
        months_into_past = 2

        home_page = HomePage()
        home_page.go_to_date_page()

        date_page = DatePage()
        date_page.select_date_from_past_months_and_verify(date, months_into_past)
