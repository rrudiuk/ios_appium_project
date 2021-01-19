import time

import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.home_page import HomePage
from .pages.landing_page import LandingPage
from .pages.menu_page import MenuPage
from .pages.learn_more_page import LearnMorePage
from .pages.welcome_page import WelcomePage


class TestLearnMorePage:
    def test_learn_more_carousel(self, driver):
        analytics_page = AnalyticsPage(driver)
        home_page = HomePage(driver)
        landing_page = LandingPage(driver)
        learn_more_page = LearnMorePage(driver)
        menu_page = MenuPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.tap_share_analytics_button()
        landing_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_learn_more_item()
        # Double tap control
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_subtitle()
        learn_more_page.should_be_double_tap_control_animation()
        learn_more_page.swipe_left()
        # Custom Control
        learn_more_page.should_be_custom_control_title()
        learn_more_page.should_be_custom_control_subtitle()
        learn_more_page.should_be_custom_control_image()
        learn_more_page.swipe_left()
        # Switching devices
        learn_more_page.should_be_switching_devices_title()
        learn_more_page.should_be_switching_devices_subtitle()
        learn_more_page.should_be_switching_devices_image()
        learn_more_page.swipe_left()
        # EQ Customization
        learn_more_page.should_be_eq_customization_title()
        learn_more_page.should_be_eq_customization_subtitle()
        learn_more_page.should_be_eq_customization_image()
        learn_more_page.swipe_left()
        # Test your fit
        learn_more_page.should_be_test_your_fit_title()
        learn_more_page.should_be_test_your_fit_subtitle()
        learn_more_page.should_be_test_your_fit_image()
        learn_more_page.swipe_left()
        # Pair a new device
        learn_more_page.should_be_pair_new_device_title()
        learn_more_page.should_be_pair_new_device_subtitle()
        learn_more_page.should_be_pair_new_device_animation()
        learn_more_page.should_be_pair_new_device_notice()
        learn_more_page.swipe_left()
        # Status Indicators
        learn_more_page.should_be_status_indicators_title()
        learn_more_page.should_be_status_indicators_subtitle()
        learn_more_page.should_be_status_indicators_image()
        learn_more_page.should_be_status_indicators_notice()
        learn_more_page.swipe_right()
        # Pair a new device
        learn_more_page.should_be_pair_new_device_title()
        learn_more_page.should_be_pair_new_device_subtitle()
        learn_more_page.should_be_pair_new_device_animation()
        learn_more_page.should_be_pair_new_device_notice()
        learn_more_page.swipe_right()
        # Test your fit
        learn_more_page.should_be_test_your_fit_title()
        learn_more_page.should_be_test_your_fit_subtitle()
        learn_more_page.should_be_test_your_fit_image()
        learn_more_page.swipe_right()
        # EQ Customization
        learn_more_page.should_be_eq_customization_title()
        learn_more_page.should_be_eq_customization_subtitle()
        learn_more_page.should_be_eq_customization_image()
        learn_more_page.swipe_right()
        # Switching devices
        learn_more_page.should_be_switching_devices_title()
        learn_more_page.should_be_switching_devices_subtitle()
        learn_more_page.should_be_switching_devices_image()
        learn_more_page.swipe_right()
        # Custom Control
        learn_more_page.should_be_custom_control_title()
        learn_more_page.should_be_custom_control_subtitle()
        learn_more_page.should_be_custom_control_image()
        learn_more_page.swipe_right()
        # Double tap control
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_subtitle()
        learn_more_page.should_be_double_tap_control_animation()
        # Quit learn more
        learn_more_page.tap_learn_more_close_button()
        menu_page.should_be_learn_more_item()
