import pytest

from .pages.welcome_page import WelcomePage
from .pages.sebulba_demo_page import SebulbaDemoPage

import time


@pytest.mark.sebulba_demo
class TestSebulbaDemoPage:
    def test_access_sebulba_centurion_screen(self, driver):
        welcome_page = WelcomePage(driver)
        centurion_page = SebulbaDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_centurion_button()
        welcome_page.tap_centurion_button()
        centurion_page.check_bt_dialog_presence_and_accept_it()
        centurion_page.wait_for_connection()
        centurion_page.should_be_close_button()
        centurion_page.should_be_send_button()
        centurion_page.should_be_payload_title()
        centurion_page.should_payload_input()
        # centurion_page.should_be_feature_id_title()
        # centurion_page.should_be_function_id_title()
        centurion_page.should_feature_selector()
        centurion_page.should_function_selector()
        centurion_page.should_be_m_button()

    @pytest.mark.sebulba_activate_curing
    @pytest.mark.sebulba_first_molding
    def test_ohboy_curring_mode_activation(self, driver):
        welcome_page = WelcomePage(driver)
        centurion_page = SebulbaDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_centurion_button()
        welcome_page.tap_centurion_button()
        centurion_page.check_bt_dialog_presence_and_accept_it()
        centurion_page.wait_for_connection()
        centurion_page.should_feature_selector()
        centurion_page.tap_feature_selector()
        centurion_page.swipe_up()
        time.sleep(2)
        centurion_page.swipe_up()
        time.sleep(2)
        centurion_page.swipe_down()
        time.sleep(2)
        centurion_page.swipe_up()
        time.sleep(2)
        centurion_page.swipe_up()
        time.sleep(2)
