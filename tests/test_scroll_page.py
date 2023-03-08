import pytest
from pages.home_page import HomePage
from pages.scroll_page import ScrollPage


@pytest.mark.usefixtures("formDriver")
class TestScrollPage:

    @pytest.mark.scroll_to_button_16
    def test_scroll_to_button_16(self):
        """ Test if you can scroll to Button 16 and back to Button 1 """
        home_page = HomePage()
        home_page.go_to_scroll_page()

        scroll_page = ScrollPage()
        scroll_page.scroll_to_button_16_and_back_to_button_1_and_verify()
