import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import HomeScreenUpdateDialogPage
from .pages.email_entry_page import EmailEntryPage
from .pages.home_page import HomePage
from .pages.menu_page import MenuPage
from .pages.molding_page import MoldNewTipsPage
from .pages.welcome_page import WelcomePage

import time


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


class TestMoldNewTips:
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

    def test_mnt_how_to_pair_screen(self, driver):
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
        mold_new_tips_page.should_be_how_to_pair_title()
        mold_new_tips_page.should_be_how_to_pair_subtitle()
        mold_new_tips_page.should_be_how_to_pair_animation()
        mold_new_tips_page.should_be_got_it_button()
        mold_new_tips_page.should_be_back_arrow()
        mold_new_tips_page.tap_got_it_button()
        # Try them on screen
        time.sleep(10)
        mold_new_tips_page.should_be_try_them_page_title()
        mold_new_tips_page.should_be_correct_try_them_page_subtitle()
        mold_new_tips_page.should_be_try_them_animation()
        mold_new_tips_page.should_be_try_them_button()
        mold_new_tips_page.should_be_back_arrow()
        mold_new_tips_page.tap_back_arrow()
        mold_new_tips_page.tap_back_arrow()
        mold_new_tips_page.should_be_check_the_fit_title()

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
        home_page.should_be_hamburger_menu_icon()
