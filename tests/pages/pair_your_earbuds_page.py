from .base_page import BasePage
from .locators import BasePageLocators
from .locators import PairYourEarbudsLocators


class PairYourEarbudsPage(BasePage):
    def should_be_pye_page_title(self):
        self.check_screen_title("Pair Your Earbuds")

    def should_be_correct_pye_page_subtitle1(self):
        assert self.is_element_present(*BasePageLocators.SCREEN_SUBTITLE), "No screen subtitle"

    def should_be_correct_pye_page_subtitle2(self):
        self.check_screen_subtitle("Wait a moment for the prompt to pair the other earbud. Select OK to continue.")

    def should_be_correct_pye_page_subtitle3(self):
        self.check_screen_subtitle("After pairing, only one of the earbuds will be shown as Connected. This is normal.")

    def should_be_open_bluetooth_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN), "Open Bluetooth button doesn't appear"

    def should_be_open_bluetooth_button_text(self):
        expected_result = "Open Bluetooth Settings"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_open_bluetooth_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def should_be_instructions_image(self):
        self.is_element_present(*PairYourEarbudsLocators.PAIR_YOUR_EARBUDS_IMAGE), "Image view doesn't appear"

    def should_be_bluetooth_settings_screen(self):
        expected_result = "Bluetooth"
        actual_result = self.get_text(*PairYourEarbudsLocators.BLUETOOTH_SETTINGS)
        assert actual_result == expected_result, f"Incorrect screen title '{actual_result}', should be '{expected_result}'"
