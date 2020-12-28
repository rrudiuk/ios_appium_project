from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LandingPageLocators


class LandingPage(BasePage):
    def should_be_landing_page_title(self):
        self.check_screen_title("Let’s Get Started")

    def should_be_correct_landing_page_subtitle(self):
        self.check_screen_subtitle("Place your earbuds in the case with the lid open to get started.")

    def should_be_next_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN), "No Next button on the screen"
        expected_result = "Next"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_next_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def should_be_progress_bar(self):
        assert self.is_element_present(*BasePageLocators.PROGRESS_BAR), "Progress bar doesn't appear"
