import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures("formDriver")
class TestHomePage:

    @pytest.mark.long_click
    def test_long_click(self):
        """ Test if modal is displayed on long click """
        home_page = HomePage()
        home_page.long_click_on_long_click_button_and_verify()
