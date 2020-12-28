from .base_page import BasePage
from .locators import AnalyticsPageLocators
from .locators import BasePageLocators


class AnalyticsPage(BasePage):

    def should_be_analytics_title(self):
        self.check_screen_title("Help Us Improve Our Products")

    def should_be_correct_analytics_subtitle(self):
        self.check_screen_subtitle("Help Ultimate Ears improve its products and services by automatically sending "
                                   "diagnostic and usage data.")

    def should_be_correct_share_analytics_button_text(self):
        expected_result = "Yes, Share Analytics Data"
        actual_result = self.get_text(*AnalyticsPageLocators.ANALYTICS_SHARE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be '{expected_result}'"

    def tap_share_analytics_button(self):
        self.click_element(*AnalyticsPageLocators.ANALYTICS_SHARE_BUTTON)

    def should_be_correct_not_share_analytics_button_text(self):
        expected_result = "NO THANKS"
        actual_result = self.get_text(*AnalyticsPageLocators.ANALYTICS_NOT_SHARE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be '{expected_result}'"

    def tap_not_share_analytics_button(self):
        self.click_element(*AnalyticsPageLocators.ANALYTICS_NOT_SHARE_BUTTON)
