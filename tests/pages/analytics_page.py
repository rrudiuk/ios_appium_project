import time

from .base_page import BasePage
from .locators import AnalyticsPageLocators


class AnalyticsPage(BasePage):

    def should_be_analytics_title(self):
        self.check_screen_title(*AnalyticsPageLocators.ANALYTICS_TITLE, "Help Us Improve\nOur Products")

    def should_be_correct_analytics_subtitle(self):
        self.check_screen_subtitle(*AnalyticsPageLocators.ANALYTICS_SUBTITLE, "Help Ultimate Ears improve its "
                                                                              "products\nand services by "
                                                                              "automatically sending\ndiagnostic and "
                                                                              "usage data.")

    def should_be_correct_share_analytics_button_text(self):
        self.check_button(*AnalyticsPageLocators.ANALYTICS_SHARE_BUTTON, "Yes, Share Analytics Data")

    def should_be_privacy_notice(self):
        self.check_message(*AnalyticsPageLocators.ANALYTICS_LEARN_MORE, 'This can be changed from the Main Menu under '
                                                                        'Support.\nLearn more about our Privacy '
                                                                        'Policy.')

    def tap_share_analytics_button(self):
        time.sleep(1)
        self.click_element(*AnalyticsPageLocators.ANALYTICS_SHARE_BUTTON)

    def should_be_correct_not_share_analytics_button_text(self):
        self.check_button(*AnalyticsPageLocators.ANALYTICS_NOT_SHARE_BUTTON, "NO THANKS")

    def tap_not_share_analytics_button(self):
        time.sleep(1)
        self.click_element(*AnalyticsPageLocators.ANALYTICS_NOT_SHARE_BUTTON)
