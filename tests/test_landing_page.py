import pytest

from .pages.landing_page import LandingPage
from .pages.analytics_page import AnalyticsPage
from .pages.welcome_page import WelcomePage


@pytest.mark.no_ble
@pytest.mark.smoke_test_not_molded
class TestLandingPage:
    def test_should_be_landing_page_after_accepting_analytics(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_back_arrow()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        landing_page.should_be_correct_landing_page_subtitle()
        landing_page.should_be_progress_bar()

    def test_should_be_landing_page_after_discarding_analytics(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_back_arrow()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_not_share_analytics_button()
        landing_page.should_be_landing_page_title()
        landing_page.should_be_correct_landing_page_subtitle()
        landing_page.should_be_progress_bar()
