from .base_page import BasePage
from .locators import DialogPageLocators


class HomeScreenWelcomeDialogPage(BasePage):

    def should_be_welcome_dialog_title(self):
        self.check_screen_title("Welcome!")

    def should_be_welcome_dialog_message(self):
        expected_result = "If you've got a sec, we have some pretty cool features we'd like to share with you."
        actual_result = self.get_text(*DialogPageLocators.DIALOG_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_take_tour_button(self):
        assert self.is_element_present(*DialogPageLocators.DIALOG_ACTION_BUTTON), "Take the tour button doesn't appear"

    def should_be_take_tour_button_text(self):
        expected_result = "Take the Tour"
        actual_result = self.get_text(*DialogPageLocators.DIALOG_ACTION_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_take_tour_button(self):
        self.click_element(*DialogPageLocators.DIALOG_ACTION_BUTTON)

    def should_be_no_thanks_button(self):
        assert self.is_element_present(*DialogPageLocators.DIALOG_ADDITIONAL_ACTION_BUTTON), "No thanks button " \
                                                                                             "doesn't appear "

    def should_be_no_thanks_button_text(self):
        expected_result = "No thanks, I got this"
        actual_result = self.get_text(*DialogPageLocators.DIALOG_ADDITIONAL_ACTION_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_no_thanks_button(self):
        self.click_element(*DialogPageLocators.DIALOG_ADDITIONAL_ACTION_BUTTON)


class EditPresetsDialogPage(BasePage):
    def should_be_dialog_title(self):
        self.check_screen_title("Whoa There…")

    def should_be_dialog_message(self):
        assert self.is_element_present(*DialogPageLocators.DIALOG_MESSAGE), "Dialog message not found"

    def should_be_delete_button(self):
        assert self.is_element_present(*DialogPageLocators.DIALOG_ACTION_BUTTON), "Delete button doesn't appear"

    def should_be_delete_button_text(self):
        expected_result = "Delete"
        actual_result = self.get_text(*DialogPageLocators.DIALOG_ACTION_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_delete_button(self):
        self.click_element(*DialogPageLocators.DIALOG_ACTION_BUTTON)

    def should_be_cancel_button(self):
        assert self.is_element_present(*DialogPageLocators.DIALOG_ADDITIONAL_ACTION_BUTTON), "Cancel button " \
                                                                                             "doesn't appear "

    def should_be_cancel_button_text(self):
        expected_result = "Cancel"
        actual_result = self.get_text(*DialogPageLocators.DIALOG_ADDITIONAL_ACTION_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_cancel_button(self):
        self.click_element(*DialogPageLocators.DIALOG_ADDITIONAL_ACTION_BUTTON)
