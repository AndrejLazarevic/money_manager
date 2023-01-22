import pytest
from pages.enter_value_page import EnterValuePage
from pages.home_page import HomePage


@pytest.mark.usefixtures("beforeTest")
class TestEnterValuePage:

    @pytest.mark.one_test
    def test_everything(self):
        home_page = HomePage()
        home_page.go_to_enter_some_value_page()

        enter_value_page = EnterValuePage()
        text = enter_value_page.get_text_from_submit()
        enter_value_page.type_in_input_enter_some_value(text)
        enter_value_page.clear_input_enter_some_value()
        enter_value_page.verify_button_submit_is_visible()
        enter_value_page.verify_button_submit_text_is(text)

    @pytest.mark.another_test
    def test_everything_again(self):
        text = "SUBMITonja"

        home_page = HomePage()
        home_page.go_to_enter_some_value_page()

        enter_value_page = EnterValuePage()
        enter_value_page.type_in_input_enter_some_value(text)
        enter_value_page.clear_input_enter_some_value()
        enter_value_page.verify_button_submit_is_visible()
        enter_value_page.verify_button_submit_text_is_not(text)

