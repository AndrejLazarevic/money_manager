import pytest
from pages.home_page import HomePage
from pages.tabs_page import TabsPage


@pytest.mark.usefixtures("formDriver")
class TestTabsPage:

    @pytest.mark.tabs_swipe
    def test_tabs_by_swiping_them(self):
        """ Test if you can change tabs by swiping them """
        home_page = HomePage()
        home_page.go_to_tab_page()

        tabs_page = TabsPage()
        tabs_page.swipe_tabs_and_verify()

    @pytest.mark.tabs_click
    def test_tabs_by_clicking_them(self):
        """ Test if you can change tabs by clicking on them """
        home_page = HomePage()
        home_page.go_to_tab_page()

        tabs_page = TabsPage()
        tabs_page.click_on_tabs_and_verify()

    @pytest.mark.tabs_content_text
    def test_tabs_content_text(self):
        """ Test the text of each tab contents """
        home_page = HomePage()
        home_page.go_to_tab_page()

        tabs_page = TabsPage()
        tabs_page.verify_tab_content_text()

    @pytest.mark.tabs_back_redirection
    def test_tabs_back_redirection(self):
        """ Test the redirection to Home Page """
        home_page = HomePage()
        home_page.go_to_tab_page()

        tabs_page = TabsPage()
        tabs_page.go_back_to_home_page()
        home_page.verify_elements()
