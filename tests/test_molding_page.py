import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import HomeScreenWelcomeDialogPage
from .pages.landing_page import LandingPage
from .pages.molding_page import MoldingPage
from .pages.home_page import HomePage
from .pages.welcome_page import WelcomePage

import time


@pytest.mark.bt_connected
@pytest.mark.smoke_test_not_molded
class TestMoldingPage:
    def test_should_be_try_them_page(self, driver):
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
        molding_page.should_be_try_them_page_title()
        molding_page.should_be_correct_try_them_page_subtitle()
        molding_page.should_be_try_them_animation()
        molding_page.should_be_try_them_button()

    def test_should_be_get_ready_page(self, driver):
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
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
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
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.check_bt_dialog_presence_and_accept_it()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
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
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.check_bt_dialog_presence_and_accept_it()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        molding_page.background_app_for_5_seconds()
        molding_page.should_be_get_ready_page_title()

    def test_should_start_soon_page2(self, driver):
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
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        molding_page.should_be_cancel_button()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    def test_cancel_molding_on_count(self, driver):
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
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        time.sleep(3)
        molding_page.should_be_cancel_button()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    @pytest.mark.first_molding
    def test_molding_complete(self, driver):
        analytics_page = AnalyticsPage(driver)
        # eq_presets_page = EqPresetsPage(driver)
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        # home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.check_bt_dialog_presence_and_accept_it()
        landing_page.should_be_landing_page_title()
        time.sleep(12)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_try_them_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_do_this_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(20)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        time.sleep(45)
        molding_page.should_be_progress_bar()
        time.sleep(40)

        molding_page.should_be_congratulations_title()
        molding_page.should_be_congratulations_subtitle()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button()
        # molding_page.tap_skip_for_now_button()
        time.sleep(5)

        # home_page.should_be_earbuds_name()
        # home_page.should_be_connected_state()
        # home_page.should_be_hamburger_menu()
        # home_page.should_be_settings_icon()
        # home_page.should_be_left_earbud_image()
        # home_page.should_be_left_battery_image()
        # home_page.should_be_left_battery_percents()
        # home_page.should_be_right_earbud_image()
        # home_page.should_be_right_battery_image()
        # home_page.should_be_right_battery_percents()
        # home_page.should_be_case_image()
        # home_page.should_be_case_battery_image()
        # home_page.should_be_case_battery_percents()
        # eq_presets_page.should_be_eq_expand_icon()
        # eq_presets_page.should_be_eq_name()
        # eq_presets_page.should_be_ue_signature_eq_selected()
        # eq_presets_page.should_be_eq_curve_image()

    # def test_molding_complete_and_open_learn_more(self, driver):
    #     analytics_page = AnalyticsPage(driver)
    #     eq_presets_page = EqPresetsPage(driver)
    #     landing_page = LandingPage(driver)
    #     learn_more_page = LearnMorePage(driver)
    #     molding_page = MoldingPage(driver)
    #     home_page = HomePage(driver)
    #     welcome_page = WelcomePage(driver)
    #     welcome_page.should_be_correct_welcome_title()
    #     welcome_page.tap_welcome_screen_get_started()
    #     analytics_page.should_be_analytics_title()
    #     analytics_page.tap_share_analytics_button()
    #     landing_page.check_bt_dialog_presence_and_accept_it()
    #     landing_page.should_be_landing_page_title()
    #     time.sleep(12)
    #     molding_page.should_be_try_them_page_title()
    #     molding_page.tap_main_button()
    #     molding_page.should_be_get_ready_page_title()
    #     molding_page.tap_main_button()
    #     molding_page.should_be_how_is_bass_title()
    #     time.sleep(19)
    #     molding_page.should_be_starting_soon_title()
    #     molding_page.should_be_starting_soon_subtitle1()
    #     time.sleep(6)
    #     molding_page.should_be_starting_soon_title()
    #     molding_page.should_be_starting_soon_subtitle2()
    #     time.sleep(45)
    #     molding_page.should_be_progress_bar()
    #     time.sleep(40)
    #
    #     molding_page.should_congratulations_title()
    #     molding_page.should_congratulations_subtitle_after_first_molding()
    #     molding_page.should_skip_for_now_button()
    #     molding_page.should_skip_for_now_button_text()
    #     molding_page.should_be_take_the_tour_button()
    #     molding_page.should_be_take_the_tour_button_text()
    #     molding_page.tap_take_the_tour_button()
    #     learn_more_page.should_be_double_tap_control_title()
    #     learn_more_page.should_be_double_tap_control_message()
    #     learn_more_page.should_be_double_tap_control_video()
    #     learn_more_page.should_be_close_button()
    #     learn_more_page.tap_close_button()
    #
    #     home_page.should_be_earbuds_name()
    #     home_page.should_be_connected_state()
    #     home_page.should_be_hamburger_menu()
    #     home_page.should_be_settings_icon()
    #     home_page.should_be_left_earbud_image()
    #     home_page.should_be_left_battery_image()
    #     home_page.should_be_left_battery_percents()
    #     home_page.should_be_right_earbud_image()
    #     home_page.should_be_right_battery_image()
    #     home_page.should_be_right_battery_percents()
    #     home_page.should_be_case_image()
    #     home_page.should_be_case_battery_image()
    #     home_page.should_be_case_battery_percents()
    #     eq_presets_page.should_be_eq_expand_icon()
    #     eq_presets_page.should_be_eq_name()
    #     eq_presets_page.should_be_ue_signature_eq_selected()
    #     eq_presets_page.should_be_eq_curve_image()
    #
    # @pytest.mark.test
    # def test_mold_new_tips_carousel(self, driver):
    #     analytics_page = AnalyticsPage(driver)
    #     home_page = HomePage(driver)
    #     menu_page = MenuPage(driver)
    #     mold_new_tips_page = MoldNewTipsPage(driver)
    #     welcome_page = WelcomePage(driver)
    #     welcome_page.tap_welcome_screen_get_started()
    #     analytics_page.tap_share_analytics_button()
    #     landing_page.check_bt_dialog_presence_and_accept_it()
    #     time.sleep(10)
    #     home_page.should_be_earbuds_name()
    #     home_page.tap_hamburger_menu_icon()
    #     menu_page.tap_mold_new_tips_item()
    #     # Change your tips
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_not_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_change_tips_title()
    #     mold_new_tips_page.should_be_change_tips_subtitle()
    #     # Remove inserts
    #     mold_new_tips_page.swipe_left()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_not_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_remove_inserts_title()
    #     mold_new_tips_page.should_be_remove_inserts_subtitle()
    #     # Match them up
    #     mold_new_tips_page.swipe_left()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_not_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_match_them_up_title()
    #     mold_new_tips_page.should_be_match_them_up_subtitle()
    #     # Attach your tips
    #     mold_new_tips_page.swipe_left()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_not_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_attach_your_tips_title()
    #     mold_new_tips_page.should_be_attach_your_tips_subtitle()
    #     # Check the fit
    #     mold_new_tips_page.swipe_left()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_check_the_fit_title()
    #     mold_new_tips_page.should_be_check_the_fit_subtitle()
    #     # Attach your tips
    #     mold_new_tips_page.swipe_right()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_attach_your_tips_title()
    #     mold_new_tips_page.should_be_attach_your_tips_subtitle()
    #     # Match them up
    #     mold_new_tips_page.swipe_right()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_match_them_up_title()
    #     mold_new_tips_page.should_be_match_them_up_subtitle()
    #     # Remove inserts
    #     mold_new_tips_page.swipe_right()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_remove_inserts_title()
    #     mold_new_tips_page.should_be_remove_inserts_subtitle()
    #     # Change your tips
    #     mold_new_tips_page.swipe_right()
    #     mold_new_tips_page.should_be_close_button()
    #     mold_new_tips_page.should_be_scroll_dots()
    #     mold_new_tips_page.should_next_button()
    #     mold_new_tips_page.should_next_button_text()
    #     mold_new_tips_page.next_button_enabled()
    #     mold_new_tips_page.should_be_image_item()
    #     mold_new_tips_page.should_be_change_tips_title()
    #     mold_new_tips_page.should_be_change_tips_subtitle()
    #     # Return to Home screen
    #     mold_new_tips_page.tap_close_button()
    #     menu_page.tap_exit_x_button()
    #     home_page.should_be_earbuds_name()
