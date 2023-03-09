import pytest

from pages.welcome_page import WelcomePage


@pytest.mark.usefixtures("formDriver")
class TestWelcomePage:

    @pytest.mark.elements_present
    def test_if_page_elements_are_present(self):
        """ Test if all page elements are present """
        welcome_page = WelcomePage()
        welcome_page.verify_elements()
