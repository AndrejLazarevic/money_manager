import pytest

from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage


@pytest.mark.usefixtures("formDriver")
class TestLoginPage:

    @pytest.mark.long_click
    def test_positive_login(self):
        """ Test positive login scenario """
        welcome_page = WelcomePage()
        welcome_page.go_to_login_page()

        login_page = LoginPage()
        login_page.log_in('andrej777lazarevic@gmail.com', 'Test1234')
