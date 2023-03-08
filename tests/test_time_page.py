import pytest
from pages.home_page import HomePage
from pages.time_page import TimePage


@pytest.mark.usefixtures("formDriver")
class TestTimePage:

    @pytest.mark.time_night
    def test_time_night(self):
        """ Test if you can set the time in the night (PM) """
        time = "10:46 PM"

        home_page = HomePage()
        home_page.go_to_time_page()

        time_page = TimePage()
        time_page.switch_to_text_mode()
        time_page.set_time_in_text_mode_to(time)
        time_page.switch_to_clock_mode()
        time_page.verify_time_is_set_to(time)

    @pytest.mark.time_morning
    def test_time_morning(self):
        """ Test if you can set the time in the morning (AM) """
        time = "9:15 AM"

        home_page = HomePage()
        home_page.go_to_time_page()

        time_page = TimePage()
        time_page.switch_to_text_mode()
        time_page.set_time_in_text_mode_to(time)
        time_page.switch_to_clock_mode()
        time_page.verify_time_is_set_to(time)
