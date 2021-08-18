import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import HomeScreenUpdateDialogPage
from .pages.landing_page import LandingPage
from .pages.learn_more_page import LearnMorePage
from .pages.menu_page import MenuPage
from .pages.molding_page import MoldingPage
from .pages.home_page import HomePage
from .pages.welcome_page import WelcomePage

import time


class TestMoldingPage:
    @pytest.mark.skip
    def test_how_to_pair_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.check_bt_dialog_presence_and_accept_it()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        molding_page.should_be_how_to_pair_title()
        molding_page.should_be_how_to_pair_subtitle()
        molding_page.should_be_how_to_pair_animation()
        molding_page.tap_got_it_button()
        molding_page.should_be_back_arrow()

    def test_should_be_try_them_page(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.should_be_correct_try_them_page_subtitle()
        molding_page.should_be_try_them_animation()
        molding_page.should_be_try_them_button()

    def test_should_be_get_ready_page(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.should_be_message_title1()
        molding_page.should_be_message_title2()
        molding_page.should_be_message_title3()
        molding_page.should_be_message1()
        molding_page.should_be_message2()
        molding_page.should_be_message3()
        molding_page.should_be_smile()
        molding_page.should_be_stand_by_mirror_text()
        molding_page.should_be_do_this_button()

    def test_should_be_how_is_bass_page(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        # How is the bass
        molding_page.should_be_how_is_bass_title()
        molding_page.should_be_correct_how_is_bass_subtitle()
        molding_page.should_be_image_volume()
        molding_page.should_be_adjust_volume_bar()
        molding_page.should_be_cancel_button()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    def test_should_start_soon_page1(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        # How is the bass
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        molding_page.background_app_for_5_seconds()
        molding_page.should_be_get_ready_page_title()

    def test_should_start_soon_page2(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        # How is the bass
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(4)
        # Starting soon 2
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        molding_page.should_be_cancel_button()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    def test_cancel_molding_on_count(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        # How is the bass
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(4)
        # Starting soon 2
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        time.sleep(4)
        # Countdown
        molding_page.should_be_cancel_button()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    # @pytest.mark.first_molding
    def test_molding_complete(self, driver):
        analytics_page = AnalyticsPage(driver)
        dialog_page = HomeScreenUpdateDialogPage(driver)
        molding_page = MoldingPage(driver)
        home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        # How is the bass
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(4)
        # Starting soon 2
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        # Molding starts
        time.sleep(45)
        molding_page.should_be_progress_bar()
        time.sleep(40)
        # Congratulations
        molding_page.should_be_congratulations_title()
        molding_page.should_be_congratulations_subtitle()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button()
        molding_page.tap_skip_for_now_button()
        time.sleep(5)
        dialog_page.check_and_close_fw_update_dialog()
        home_page.should_be_hamburger_menu()

    # @pytest.mark.first_molding
    def test_molding_complete_and_open_learn_more(self, driver):
        analytics_page = AnalyticsPage(driver)
        dialog_page = HomeScreenUpdateDialogPage(driver)
        learn_more_page = LearnMorePage(driver)
        molding_page = MoldingPage(driver)
        home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        molding_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        # Get ready
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        # How is the bass
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(4)
        # Starting soon 2
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        # Molding starts
        time.sleep(45)
        molding_page.should_be_progress_bar()
        time.sleep(40)
        # Congratulations
        molding_page.should_be_congratulations_title()
        molding_page.should_be_congratulations_subtitle()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button()
        molding_page.tap_take_the_tour_button()
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_animation()
        learn_more_page.should_be_learn_more_menu_icon()
        learn_more_page.tap_learn_more_menu_icon()
        # Quit learn more
        learn_more_page.tap_learn_more_menu_icon()
        dialog_page.check_and_close_fw_update_dialog()
        home_page.should_be_hamburger_menu()
