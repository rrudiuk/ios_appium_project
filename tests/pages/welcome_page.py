from .base_page import BasePage
from .locators import WelcomePageLocators


class WelcomePage(BasePage):
    def should_be_correct_welcome_title(self):
        self.check_screen_title(*WelcomePageLocators.WELCOME_SCREEN_TITLE, "Welcome to Your\nPerfect Fit")

    # def should_be_correct_welcome_title_x(self):
    #     self.driver.execute_script("mobile: source", {'format': 'description'})
    #     assert self.driver.find_elements_by_xpath('//XCUIElementTypeButton[@name="Welcome to Your Perfect Fit"]'),\
    #         "Title not found with xpath"
    #
    # def should_be_correct_welcome_title_a(self):
    #     self.driver.execute_script("mobile: source", {'format': 'description'})
    #     assert self.driver.find_elements_by_accessibility_id('Welcome to Your\nPerfect Fit'), "Title not found with " \
    #                                                                                           "accessibility id "

    def should_be_correct_welcome_subtitle(self):
        self.check_screen_subtitle(*WelcomePageLocators.WELCOME_SCREEN_SUBTITLE, "In just a few minutes, you’ll have "
                                                                                 "a pair\nof perfectly fitting, "
                                                                                 "incredibly\ncomfortable earbuds.")

    def should_be_welcome_screen_button(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_SCREEN_BUTTON), "Get started button doesn't appear"

    def should_be_welcome_get_started_button_text(self):
        self.check_button_text(*WelcomePageLocators.WELCOME_SCREEN_BUTTON, "Get Started")

    def tap_welcome_screen_get_started(self):
        self.click_element(*WelcomePageLocators.WELCOME_SCREEN_BUTTON), "Get started button not found"

    def tap_welcome_screen_10_times(self):
        self.click_element_10_times(*WelcomePageLocators.WELCOME_SCREEN_TITLE)

    def should_be_welcome_code_screen_title(self):
        self.check_screen_title(*WelcomePageLocators.CODE_SCREEN_TITLE, "WELCOME")

    def should_be_welcome_edit_text_input(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE), "Input field not found"

    def should_be_welcome_edit_text_input_text(self):
        expected_result = "ENTER YOUR CODE"
        actual_result = self.get_text(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        assert actual_result == expected_result, f"Incorrect input text '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    def should_be_welcome_send_code_button(self):
        assert self.is_element_present(*WelcomePageLocators.SEND_CODE_BUTTON), "Get started button not found"

    def should_be_welcome_code_get_started_button_text(self):
        self.check_button_text(*WelcomePageLocators.SEND_CODE_BUTTON, "GET STARTED")

    def tap_screen_code_get_started(self):
        self.click_element(*WelcomePageLocators.SEND_CODE_BUTTON)

    def go_to_demo_screen_code(self):
        text_input = self.locate_element(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        text_input.send_keys("001")

    def go_to_home_screen_code(self):
        text_input = self.locate_element(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        text_input.send_keys("002")
