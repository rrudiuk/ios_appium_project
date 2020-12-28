from .base_page import BasePage
from .locators import TutorialHomePageLocators


class TutorialHomeScreenPage(BasePage):
    # First tutorial screen
    def should_be_tutorial_container(self):
        self.is_element_present(*TutorialHomePageLocators.TUTORIAL_CONTAINER), "Tutorial container is not present"

    def should_be_tutorial_arrow(self):
        self.is_element_present(*TutorialHomePageLocators.ARROW_TUTORIAL), "Tutorial arrow is not present"

    def should_be_main_menu_title(self):
        self.check_screen_title("Main Menu")

    def should_be_main_menu_tutorial_message(self):
        expected_result = "Learn how to use your UE FITS or take a quiz to test your fit"
        actual_result = self.get_text(*TutorialHomePageLocators.TUTORIAL_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message {actual_result}, should be {expected_result}"

    def should_be_next_button(self):
        assert self.is_element_present(*TutorialHomePageLocators.TUTORIAL_NEXT_BUTTON), "Next button doesn't appear"

    def should_be_next_button_text(self):
        expected_result = "Next"
        actual_result = self.get_text(*TutorialHomePageLocators.TUTORIAL_NEXT_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_next_button(self):
        self.click_element(*TutorialHomePageLocators.TUTORIAL_NEXT_BUTTON)

    def should_be_skip_tutorial_button(self):
        assert self.is_element_present(*TutorialHomePageLocators.SKIP_TUTORIAL_BUTTON), "Next button doesn't appear"

    def should_be_skip_tutorial_button_text(self):
        expected_result = "Skip Tutorial"
        actual_result = self.get_text(*TutorialHomePageLocators.SKIP_TUTORIAL_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_skip_tutorial_button(self):
        self.click_element(*TutorialHomePageLocators.SKIP_TUTORIAL_BUTTON)

    # Second tutorial screen
    def should_be_settings_title(self):
        self.check_screen_title("Settings")

    def should_be_settings_tutorial_message(self):
        expected_result = "Customize the double tap controls or change your FITS name"
        actual_result = self.get_text(*TutorialHomePageLocators.TUTORIAL_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message {actual_result}, should be {expected_result}"

    def should_be_thanks_next_button(self):
        assert self.is_element_present(*TutorialHomePageLocators.TUTORIAL_NEXT_BUTTON), "Thanks next button doesn't" \
                                                                                        " appear"

    def should_be_thanks_next_button_text(self):
        expected_result = "Thanks, Next!"
        actual_result = self.get_text(*TutorialHomePageLocators.TUTORIAL_NEXT_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    # Third tutorial screen
    def should_be_custom_eq_title(self):
        expected_result = "Custom EQ"
        actual_result = self.get_text(*TutorialHomePageLocators.CUSTOM_EQ_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_custom_eq_message(self):
        expected_result = "Choose one of our sound profiles or customize your own"
        actual_result = self.get_text(*TutorialHomePageLocators.CUSTOM_EQ_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_got_it_button(self):
        assert self.is_element_present(*TutorialHomePageLocators.GOT_IT_BUTTON), "Got it button doesn't appear"

    def should_be_got_it_button_text(self):
        expected_result = "Got it!"
        actual_result = self.get_text(*TutorialHomePageLocators.GOT_IT_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_got_it_button(self):
        self.click_element(*TutorialHomePageLocators.GOT_IT_BUTTON)
