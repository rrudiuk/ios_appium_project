import pytest

from .pages.welcome_page import WelcomePage
from .pages.ohboy_demo_page import OhboyDemoPage

import time


@pytest.mark.ohboy_demo
class TestOhboyDemoPage:
    def test_access_ohboy_demo_molding_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = OhboyDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()

    def test_access_ohboy_demo_debug_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = OhboyDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()
        demo_page.tap_debug_button()
        demo_page.should_be_demo_debug_screen()

    def test_check_first_two_items_codes_ohboy_demo(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = OhboyDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()
        demo_page.tap_debug_button()
        demo_page.should_be_demo_debug_screen()
        demo_page.tap_first_commands_list_item()
        demo_page.tap_second_commands_list_item()

    @pytest.mark.ohboy_activate_curing
    @pytest.mark.ohboy_first_molding
    def test_ohboy_curring_mode_activation(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = OhboyDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()
        demo_page.tap_debug_button()
        demo_page.activate_curring_mode()
