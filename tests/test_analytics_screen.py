import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.welcome_page import WelcomePage


@pytest.mark.no_ble
@pytest.mark.ble_connected
@pytest.mark.bt_connected
@pytest.mark.smoke_test_not_molded
class TestAnalyticsPage:
    def test_should_be_analytics_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_back_arrow()
        analytics_page.should_be_analytics_title()
        analytics_page.should_be_correct_analytics_subtitle()
        analytics_page.should_be_correct_share_analytics_button_text()
        analytics_page.should_be_correct_not_share_analytics_button_text()

    def test_return_to_welcome_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_back_arrow()
        analytics_page.tap_back_arrow()
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()
