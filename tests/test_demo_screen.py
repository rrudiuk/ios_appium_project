import pytest

from .pages.welcome_page import WelcomePage
from .pages.demo_page import DemoPage

import time


@pytest.mark.demo
class TestDemoPage:
    def test_access_demo_molding_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = DemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()

    def test_access_demo_debug_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = DemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()
        demo_page.tap_debug_button()
        demo_page.should_be_demo_debug_screen()

    def test_check_first_two_items_codes(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = DemoPage(driver)
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

    @pytest.mark.activate_curing
    @pytest.mark.first_molding
    def test_curring_mode_activation(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = DemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_demo_flow_button()
        welcome_page.tap_demo_flow_button()
        demo_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(6)
        demo_page.should_be_debug_button()
        demo_page.tap_debug_button()
        demo_page.activate_curring_mode()
