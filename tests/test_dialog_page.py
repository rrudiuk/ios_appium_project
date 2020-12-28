import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import HomeScreenWelcomeDialogPage
from .pages.landing_page import LandingPage
from .pages.welcome_page import WelcomePage

import time


@pytest.mark.molded_earbuds
class TestDialogPage:
    def test_welcome_dialog_pops_up(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        dialog_page = HomeScreenWelcomeDialogPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        dialog_page.should_be_welcome_dialog_title()
        dialog_page.should_be_welcome_dialog_message()
        dialog_page.should_be_take_tour_button()
        dialog_page.should_be_take_tour_button_text()
        dialog_page.should_be_no_thanks_button()
        dialog_page.should_be_no_thanks_button_text()
