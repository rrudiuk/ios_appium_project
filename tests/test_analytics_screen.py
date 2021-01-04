import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.welcome_page import WelcomePage


class TestAnalyticsPage:
    def test_should_be_analytics_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.should_be_correct_analytics_subtitle()
        analytics_page.should_be_correct_share_analytics_button_text()
        analytics_page.should_be_correct_not_share_analytics_button_text()
