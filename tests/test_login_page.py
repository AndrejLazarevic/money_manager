import pytest

from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage


@pytest.mark.usefixtures("formDriver")
class TestLoginPage:

    @pytest.mark.valid_login
    def test_positive_login(self):
        """ Positive login scenario """
        welcome_page = WelcomePage()
        welcome_page.go_to_login_page()

        login_page = LoginPage()
        login_page.log_in_with_valid_data('andrej777lazarevic@gmail.com', 'Test1234')

    @pytest.mark.invalid_email_login
    def test_invalid_email_login(self):
        """ Invalid email login scenario """
        welcome_page = WelcomePage()
        welcome_page.go_to_login_page()

        login_page = LoginPage()
        login_page.log_in_with_invalid_email_and_verify_error("notanemail")

    @pytest.mark.invalid_email_login
    def test_invalid_password_login(self):
        """ Incorrect password login scenario """
        welcome_page = WelcomePage()
        welcome_page.go_to_login_page()

        login_page = LoginPage()
        login_page.log_in_with_incorrect_password_and_verify_error("goodemail@yopmail.com", "aws")
