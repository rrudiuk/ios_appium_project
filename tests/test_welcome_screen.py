import time

import pytest

from .pages.welcome_page import WelcomePage


class TestWelcomePage:
    @pytest.mark.welcome
    def test_should_be_welcome_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_get_started_button()

    def test_should_be_welcome_screen_after_background(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_get_started_button()
        welcome_page.background_app_for_5_seconds()
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_get_started_button()

    def test_should_be_flow_selection_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.should_be_centurion_button()

    @pytest.mark.skip
    def test_should_be_welcome_code_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.should_be_welcome_edit_text_input()
        welcome_page.should_be_welcome_edit_text_input_text()
        welcome_page.should_be_welcome_code_get_started_button()

    @pytest.mark.skip
    def test_can_access_home_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_home_screen_code()
        welcome_page.tap_screen_code_get_started()
        welcome_page.check_bt_dialog_presence_and_accept_it()
