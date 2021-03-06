from .base_page import BasePage
from .locators import WelcomePageLocators


class WelcomePage(BasePage):
    def should_be_correct_welcome_title(self):
        self.check_screen_title(*WelcomePageLocators.WELCOME_SCREEN_TITLE, "Welcome to Your Perfect Fit")

    def should_be_correct_welcome_subtitle(self):
        self.check_screen_subtitle(*WelcomePageLocators.WELCOME_SCREEN_SUBTITLE, "In just a few minutes, you’ll have "
                                                                                 "a pair of perfectly fitting, "
                                                                                 "incredibly comfortable earbuds. ")

    def should_be_welcome_get_started_button(self):
        self.check_button(*WelcomePageLocators.WELCOME_SCREEN_BUTTON, "Get Started")

    def tap_welcome_screen_get_started(self):
        self.click_element(*WelcomePageLocators.WELCOME_SCREEN_BUTTON), "Get started button not found"

    def tap_welcome_screen_10_times(self):
        self.click_element_10_times(*WelcomePageLocators.WELCOME_SCREEN_TITLE)

    def should_be_centurion_button(self):
        self.check_button(*WelcomePageLocators.CENTURION_BUTTON, "Centurion++")

    def tap_centurion_button(self):
        self.click_element(*WelcomePageLocators.CENTURION_BUTTON)

    def should_be_demo_flow_button(self):
        self.check_button(*WelcomePageLocators.DEMO_FLOW_BUTTON, "Demo Flow")

    def tap_demo_flow_button(self):
        self.click_element(*WelcomePageLocators.DEMO_FLOW_BUTTON)

    # Outdated method
    def should_be_welcome_code_screen_title(self):
        self.check_screen_title(*WelcomePageLocators.CODE_SCREEN_TITLE, "WELCOME")

    # Outdated method
    def should_be_welcome_edit_text_input(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE), "Input field not found"

    # Outdated method
    def should_be_welcome_edit_text_input_text(self):
        expected_result = "ENTER YOUR CODE"
        actual_result = self.get_text(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        assert actual_result == expected_result, f"Incorrect input text '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    # Outdated method
    def should_be_welcome_code_get_started_button(self):
        self.check_button(*WelcomePageLocators.SEND_CODE_BUTTON, "GET STARTED")

    # Outdated method
    def tap_screen_code_get_started(self):
        self.click_element(*WelcomePageLocators.SEND_CODE_BUTTON)

    # Outdated method
    def go_to_demo_screen_code(self):
        text_input = self.locate_element(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        text_input.send_keys("001")

    # Outdated method
    def go_to_home_screen_code(self):
        text_input = self.locate_element(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        text_input.send_keys("002")
