import pytest

from pages.signup_page import SignupPage
from pages.welcome_page import WelcomePage
from utilities.random_generator import RandomGenerator


@pytest.mark.usefixtures("formDriver")
class TestSignupPage:

    @pytest.mark.valid_signup
    def test_positive_signup(self):
        """ Positive signup scenario """
        welcome_page = WelcomePage()
        welcome_page.go_to_signup_page()

        signup_page = SignupPage()
        signup_page.signup_with_valid_data(RandomGenerator.generate_mail(), 'Test1234')
        welcome_page.verify_elements_after_signup()
