import pytest

from .pages.welcome_page import WelcomePage


class TestWelcomePage:
    def test_should_be_welcome_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()

    def test_should_be_welcome_screen_after_background(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()
        welcome_page.background_app_for_10_seconds()
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()

    def test_should_be_welcome_code_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.should_be_welcome_edit_text_input()
        welcome_page.should_be_welcome_edit_text_input_text()
        welcome_page.should_be_welcome_send_code_button()
        welcome_page.should_be_welcome_code_get_started_button_text()

    # def test_access_setup_code_screen(self, driver):
    #     welcome_page = WelcomePage(driver)
    #     welcome_page.should_be_correct_welcome_title()
    #     welcome_page.tap_welcome_screen_10_times()
    #     welcome_page.should_be_welcome_code_screen_title()
    #     welcome_page.tap_where_is_my_code()
    #     welcome_page.should_be_correct_setup_code_title()
    #     welcome_page.should_be_correct_welcome_setup_code_text()
    #     welcome_page.close_welcome_setup_code_screen()
    #     welcome_page.should_be_welcome_code_screen_title()

    def test_can_access_home_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_home_screen_code()
        welcome_page.tap_screen_code_get_started()
        welcome_page.check_bt_dialog_presence_and_accept_it()
