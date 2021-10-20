import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import HomeScreenUpdateDialogPage
from .pages.email_entry_page import EmailEntryPage
from .pages.firmware_update_page import FirmwareUpdatePage
from .pages.home_page import HomePage
from .pages.learn_more_page import LearnMorePage
from .pages.menu_page import MenuPage
from .pages.molding_page import MoldingPage, MoldNewTipsPage
from .pages.sebulba_demo_page import SebulbaDemoPage
from .pages.support_page import SupportPage
from .pages.ugc_page import UGCPage
from .pages.user_guide_page import UserGuidePage
from .pages.welcome_page import WelcomePage

import time


def initial_setup_molding(driver):
    analytics_page = AnalyticsPage(driver)
    email_entry_page = EmailEntryPage(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.should_be_correct_welcome_title()
    welcome_page.tap_welcome_screen_get_started()
    email_entry_page.should_be_email_entry_title()
    email_entry_page.tap_no_thanks_button()
    analytics_page.should_be_analytics_title()
    analytics_page.tap_share_analytics_button()
    analytics_page.check_bt_dialog_presence_and_accept_it()
    analytics_page.wait_for_connection()


def initial_setup_non_molding(driver):
    analytics_page = AnalyticsPage(driver)
    email_entry_page = EmailEntryPage(driver)
    dialog_page = HomeScreenUpdateDialogPage(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.should_be_correct_welcome_title()
    welcome_page.tap_welcome_screen_get_started()
    email_entry_page.should_be_email_entry_title()
    email_entry_page.should_be_correct_email_entry_subtitle()
    email_entry_page.tap_no_thanks_button()
    analytics_page.tap_share_analytics_button()
    analytics_page.check_bt_dialog_presence_and_accept_it()
    dialog_page.wait_for_connection()
    dialog_page.check_and_close_fw_update_dialog()


"""That's the set of tests from all test files intended to run smoke test
Requires connected earbuds via BT classic pulled off out of the case"""


@pytest.mark.sebulba_smoke_test
class TestSmokeTest:
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

    def test_should_be_analytics_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        email_entry_page = EmailEntryPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        email_entry_page.should_be_email_entry_title()
        email_entry_page.should_be_correct_email_entry_subtitle()
        email_entry_page.tap_no_thanks_button()
        analytics_page.should_be_analytics_title()
        analytics_page.should_be_correct_analytics_subtitle()
        analytics_page.should_be_correct_share_analytics_button_text()
        analytics_page.should_be_correct_not_share_analytics_button_text()
        analytics_page.should_be_privacy_notice()

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
        centurion_page.should_be_feature_id_title()
        centurion_page.should_be_function_id_title()
        centurion_page.should_feature_selector()
        centurion_page.should_function_selector()
        centurion_page.should_be_m_button()

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
        centurion_page.tap_m_button()
        time.sleep(5)
        centurion_page.should_be_reset_button()
        centurion_page.tap_reset_button()
        welcome_page.should_be_correct_welcome_title()

    # Pre-molding
    def test_should_be_try_them_page(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
        # Try them on
        molding_page.should_be_try_them_page_title()
        molding_page.should_be_correct_try_them_page_subtitle()
        molding_page.should_be_try_them_animation()
        molding_page.should_be_try_them_button()

    def test_should_be_get_ready_page(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
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
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
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
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
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
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
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
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
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

    # Molding
    def test_molding_complete(self, driver):
        initial_setup_molding(driver)
        dialog_page = HomeScreenUpdateDialogPage(driver)
        molding_page = MoldingPage(driver)
        home_page = HomePage(driver)
        ugc_page = UGCPage(driver)

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
        time.sleep(45)

        # UGC
        ugc_page.should_be_ugc_title()
        ugc_page.should_be_correct_ugc_subtitle()
        ugc_page.tap_skip_button()

        # Congratulations
        molding_page.should_be_congratulations_title()
        molding_page.should_be_congratulations_subtitle()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button()
        molding_page.tap_skip_for_now_button()
        time.sleep(2)
        dialog_page.check_and_close_fw_update_dialog()
        home_page.should_be_hamburger_menu()

    def test_ohboy_curring_mode_activation1(self, driver):
        welcome_page = WelcomePage(driver)
        centurion_page = SebulbaDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_centurion_button()
        welcome_page.tap_centurion_button()
        centurion_page.check_bt_dialog_presence_and_accept_it()
        centurion_page.wait_for_connection()
        centurion_page.should_feature_selector()
        centurion_page.tap_m_button()
        time.sleep(5)
        centurion_page.should_be_reset_button()
        centurion_page.tap_reset_button()
        welcome_page.should_be_correct_welcome_title()

    def test_molding_complete_and_open_learn_more(self, driver):
        initial_setup_molding(driver)
        dialog_page = HomeScreenUpdateDialogPage(driver)
        learn_more_page = LearnMorePage(driver)
        molding_page = MoldingPage(driver)
        home_page = HomePage(driver)
        ugc_page = UGCPage(driver)

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

        # UGC
        ugc_page.should_be_ugc_title()
        ugc_page.should_be_correct_ugc_subtitle()
        ugc_page.tap_skip_button()

        # Congratulations
        molding_page.should_be_congratulations_title()
        molding_page.should_be_congratulations_subtitle()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button()
        molding_page.tap_take_the_tour_button()

        # Learn more
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_animation()
        learn_more_page.should_be_learn_more_menu_icon()
        learn_more_page.tap_learn_more_menu_icon()

        # Quit learn more
        learn_more_page.tap_learn_more_menu_icon()
        dialog_page.check_and_close_fw_update_dialog()
        home_page.should_be_hamburger_menu()

    # Menu
    def test_all_menu_items_appear(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_header()
        menu_page.should_be_app_logo()
        menu_page.should_be_exit_x_button()
        menu_page.should_be_home_item()
        menu_page.should_be_mold_new_tips_item()
        menu_page.should_be_test_your_fit_item()
        menu_page.should_be_user_guide_item()
        menu_page.should_be_support_item()
        menu_page.should_be_email_entry_item()
        menu_page.should_be_take_selfie_item()
        menu_page.tap_exit_x_button()
        home_page.should_be_earbuds_name()

    # Mold new tips
    def test_mold_new_tips_carousel(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_mold_new_tips_item()
        # Change your tips
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_change_tips_animation()
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.should_be_change_tips_subtitle()
        # Remove inserts
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_remove_inserts_image()
        mold_new_tips_page.should_be_remove_inserts_title()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        # Match them up
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_match_them_image()
        mold_new_tips_page.should_be_match_them_up_title()
        # mold_new_tips_page.should_be_match_them_up_subtitle()
        # Attach your tips
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_attach_tips_image()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.should_be_attach_your_tips_subtitle()
        # Check the fit
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_check_the_fit_image()
        mold_new_tips_page.should_be_check_the_fit_title()
        mold_new_tips_page.should_be_check_the_fit_subtitle()
        # Attach your tips
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_attach_tips_image()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.should_be_attach_your_tips_subtitle()
        # Match them up
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_match_them_image()
        mold_new_tips_page.should_be_match_them_up_title()
        # mold_new_tips_page.should_be_match_them_up_subtitle()
        # Remove inserts
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_remove_inserts_image()
        mold_new_tips_page.should_be_remove_inserts_title()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        # Change your tips
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_mnt_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_change_tips_animation()
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.should_be_change_tips_subtitle()
        # Return to Home screen
        mold_new_tips_page.tap_mnt_menu_icon()
        menu_page.should_be_mold_new_tips_item()

    def test_mnt_get_ready_screen(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_mold_new_tips_item()
        # Carousel
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_match_them_up_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_check_the_fit_title()
        mold_new_tips_page.tap_next_button()
        # How to pair screen
        mold_new_tips_page.should_be_got_it_button()
        mold_new_tips_page.tap_got_it_button()
        # Try them on screen
        time.sleep(10)
        mold_new_tips_page.should_be_try_them_button()
        mold_new_tips_page.tap_try_them_button()
        # Get Ready screen
        mold_new_tips_page.should_be_get_ready_page_title()
        mold_new_tips_page.should_be_message_title1()
        mold_new_tips_page.should_be_message_title2()
        mold_new_tips_page.should_be_message_title3()
        mold_new_tips_page.should_be_message1()
        mold_new_tips_page.should_be_message2()
        mold_new_tips_page.should_be_message3()
        mold_new_tips_page.should_be_smile()
        mold_new_tips_page.should_be_stand_by_mirror_text()
        mold_new_tips_page.should_be_do_this_button()
        mold_new_tips_page.should_be_back_arrow()
        mold_new_tips_page.tap_back_arrow()
        mold_new_tips_page.should_be_try_them_button()

    def test_mnt_warnings(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_mold_new_tips_item()
        # Carousel
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_match_them_up_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_check_the_fit_title()
        mold_new_tips_page.tap_next_button()
        # How to pair screen
        mold_new_tips_page.should_be_got_it_button()
        mold_new_tips_page.tap_got_it_button()
        # Try them on screen
        time.sleep(10)
        mold_new_tips_page.should_be_try_them_button()
        mold_new_tips_page.tap_try_them_button()
        # Get ready
        mold_new_tips_page.should_be_get_ready_page_title()
        mold_new_tips_page.tap_do_this_button()
        # How is the bass
        mold_new_tips_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        mold_new_tips_page.should_be_starting_soon_title()
        mold_new_tips_page.should_be_starting_soon_subtitle1()
        time.sleep(4)
        # Starting soon 2
        mold_new_tips_page.should_be_starting_soon_title()
        mold_new_tips_page.should_be_starting_soon_subtitle2()
        time.sleep(4)
        # Countdown
        mold_new_tips_page.should_be_cancel_button()
        mold_new_tips_page.background_app_for_5_seconds()
        mold_new_tips_page.should_be_get_ready_page_title()

    def test_mnt_molding(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_mold_new_tips_item()
        # Carousel
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_match_them_up_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_check_the_fit_title()
        mold_new_tips_page.tap_next_button()
        # How to pair screen
        mold_new_tips_page.should_be_got_it_button()
        mold_new_tips_page.tap_got_it_button()
        # Try them on screen
        time.sleep(10)
        mold_new_tips_page.should_be_try_them_button()
        mold_new_tips_page.tap_try_them_button()
        # Get ready screen
        mold_new_tips_page.should_be_get_ready_page_title()
        mold_new_tips_page.tap_do_this_button()
        # How is the bass
        mold_new_tips_page.should_be_how_is_bass_title()
        time.sleep(20)
        # Starting soon 1
        mold_new_tips_page.should_be_starting_soon_title()
        mold_new_tips_page.should_be_starting_soon_subtitle1()
        time.sleep(4)
        # Starting soon 2
        mold_new_tips_page.should_be_starting_soon_title()
        mold_new_tips_page.should_be_starting_soon_subtitle2()
        # Molding starts
        time.sleep(45)
        mold_new_tips_page.should_be_progress_bar()
        time.sleep(40)
        # Congratulations
        mold_new_tips_page.should_be_congratulations_title()
        mold_new_tips_page.should_be_congratulations_subtitle()
        mold_new_tips_page.should_be_finish_button()
        mold_new_tips_page.tap_finish_button()
        home_page.should_be_hamburger_menu()

    # User guide
    def test_all_user_guide_items_appear(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_pairing_item()
        user_guide_page.should_be_molding_item()
        user_guide_page.should_be_controls_item()
        user_guide_page.should_be_connectivity_and_switching_item()
        user_guide_page.should_be_charging_item()
        user_guide_page.should_be_adjusting_eq_item()
        user_guide_page.should_be_tyf_item()
        user_guide_page.should_be_updating_fw_item()
        user_guide_page.should_be_troubleshooting_item()

    def test_user_guide_pairing_sebulba(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_pairing_item()
        user_guide_page.tap_pairing_item()
        user_guide_page.should_be_pairing_sebulba_screen()

    def test_user_guide_molding(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_molding_item()
        user_guide_page.tap_molding_item()
        user_guide_page.should_be_molding_screen()

    def test_user_guide_controls(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_controls_item()
        user_guide_page.tap_controls_item()
        user_guide_page.should_be_controls_screen()

    def test_user_guide_connectivity_and_switching_sebulba(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_connectivity_and_switching_item()
        user_guide_page.tap_connectivity_and_switching_item()
        user_guide_page.should_be_connectivity_and_switching_sebulba_screen()

    def test_user_guide_charging(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_charging_item()
        user_guide_page.tap_charging_item()
        user_guide_page.should_be_charging_screen()

    def test_user_guide_adjusting_eq(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_adjusting_eq_item()
        user_guide_page.tap_adjusting_eq_item()
        user_guide_page.should_be_adjusting_eq_screen()

    def test_user_guide_tyf(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_tyf_item()
        user_guide_page.tap_tyf_item()
        user_guide_page.should_be_tyf_screen()

    def test_user_guide_updating_fw(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_updating_fw_item()
        user_guide_page.tap_updating_fw_item()
        user_guide_page.should_be_updating_fw_screen()

    def test_user_guide_troubleshooting(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_troubleshooting_item()
        user_guide_page.tap_troubleshooting_item()
        user_guide_page.should_be_troubleshooting_screen()

    # FW update
    def test_enable_push_notifications(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_push_notifications_image()
        firmware_update_page.should_be_push_notifications_title()
        firmware_update_page.should_be_push_notifications_subtitle()
        firmware_update_page.should_be_push_notifications_notice()
        firmware_update_page.should_be_push_notifications_close_button()
        firmware_update_page.should_be_push_notifications_enable_button()
        firmware_update_page.should_be_push_notifications_no_thanks_button()

    def test_firmware_update(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(2)
        firmware_update_page.check_push_notification_dialog_presence()
        time.sleep(3)
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()

    def test_firmware_update1(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(2)
        firmware_update_page.check_push_notification_dialog_presence()
        time.sleep(3)
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()

    @pytest.mark.skip
    def test_firmware_update2(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(2)
        firmware_update_page.check_push_notification_dialog_presence()
        time.sleep(3)
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()

    @pytest.mark.skip
    def test_firmware_update3(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(2)
        firmware_update_page.check_push_notification_dialog_presence()
        time.sleep(3)
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()

    @pytest.mark.skip
    def test_firmware_update4(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(2)
        firmware_update_page.check_push_notification_dialog_presence()
        time.sleep(3)
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()

# run with
# pytest -s -v --reruns 1 -m sebulba_smoke_test --html=/Users/rudiuk/PyCharmProjects/ios_appium_project/test_report/report.html --capture sys
