from .base_page import BasePage
from .locators import DialogPageLocators

from ..utilities import logger


class HomeScreenUpdateDialogPage(BasePage):
    def check_and_close_fw_update_dialog(self):
        if self.is_element_present(*DialogPageLocators.DIALOG_TITLE):
            self.click_element(*DialogPageLocators.UPDATE_DIALOG_DISMISS_BUTTON)
            logger.LOGGER.info("Dialog dismissed")


class EditPresetsDialogPage(BasePage):
    def should_be_dialog_title(self):
        self.check_screen_title("Whoa There…")

    def should_be_dialog_message(self):
        assert self.is_element_present(*DialogPageLocators.DIALOG_MESSAGE), "Dialog message not found"

    def should_be_delete_button(self):
        assert self.is_element_present(*DialogPageLocators.UPDATE_DIALOG_ACTION_BUTTON), "Delete button doesn't appear"

    def should_be_delete_button_text(self):
        expected_result = "Delete"
        actual_result = self.get_text(*DialogPageLocators.UPDATE_DIALOG_ACTION_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_delete_button(self):
        self.click_element(*DialogPageLocators.UPDATE_DIALOG_ACTION_BUTTON)

    def should_be_cancel_button(self):
        assert self.is_element_present(*DialogPageLocators.UPDATE_DIALOG_DISMISS_BUTTON), "Cancel button " \
                                                                                             "doesn't appear "

    def should_be_cancel_button_text(self):
        expected_result = "Cancel"
        actual_result = self.get_text(*DialogPageLocators.UPDATE_DIALOG_DISMISS_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_cancel_button(self):
        self.click_element(*DialogPageLocators.UPDATE_DIALOG_DISMISS_BUTTON)
