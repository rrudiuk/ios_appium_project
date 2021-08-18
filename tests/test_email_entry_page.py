import pytest

from .pages.email_entry_page import EmailEntryPage
from .pages.welcome_page import WelcomePage


class TestEmailEntryPage:
    def test_should_be_email_entry_screen(self, driver):
        email_entry_page = EmailEntryPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        email_entry_page.should_be_back_arrow()
        email_entry_page.should_be_email_entry_title()
        email_entry_page.should_be_correct_email_entry_subtitle()
        email_entry_page.should_be_email_entry_input()
        email_entry_page.should_be_correct_sign_me_button()
        email_entry_page.should_be_correct_no_thanks_button()

    def test_return_to_welcome_screen(self, driver):
        email_entry_page = EmailEntryPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        email_entry_page.should_be_back_arrow()
        email_entry_page.tap_back_arrow()
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_get_started_button()
