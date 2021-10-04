from .base_page import BasePage
from .locators import SebulbaDemoPageLocators

import time


class SebulbaDemoPage(BasePage):
    def should_be_close_button(self):
        self.check_button(*SebulbaDemoPageLocators.CLOSE_BUTTON, "Close")

    def tap_close_button(self):
        self.click_element(*SebulbaDemoPageLocators.CLOSE_BUTTON)

    def should_be_send_button(self):
        self.check_button(*SebulbaDemoPageLocators.SEND_BUTTON, "Send")

    def tap_send_button(self):
        self.click_element(*SebulbaDemoPageLocators.SEND_BUTTON)

    # Feature selector
    def should_be_feature_id_title(self):
        self.check_screen_title(*SebulbaDemoPageLocators.FEATURE_ID_TITLE, 'Feature ID:')

    def should_feature_selector(self):
        assert self.locate_element(*SebulbaDemoPageLocators.FEATURE_SELECTOR), "Feature selector not found"

    def tap_feature_selector(self):
        self.click_element(*SebulbaDemoPageLocators.FEATURE_SELECTOR)

    # Function selector
    def should_be_function_id_title(self):
        self.check_screen_title(*SebulbaDemoPageLocators.FUNCTION_ID_TITLE, 'Function ID:')

    def should_function_selector(self):
        assert self.locate_element(*SebulbaDemoPageLocators.FUNCTION_SELECTOR), "Function selector not found"

    def tap_function_selector(self):
        self.click_element(*SebulbaDemoPageLocators.FUNCTION_SELECTOR)

    # Payload input
    def should_be_payload_title(self):
        self.check_screen_title(*SebulbaDemoPageLocators.PAYLOAD_TITLE, 'Payload: 0x')

    def should_payload_input(self):
        assert self.locate_element(*SebulbaDemoPageLocators.PAYLOAD_INPUT), "Payload input not found"

    def set_payload_to_enable_molding(self):
        payload = self.locate_element(*SebulbaDemoPageLocators.PAYLOAD_INPUT)
        payload.clear()
        payload.send_keys("03")

    # Molding activation
    def should_be_m_button(self):
        self.check_button(*SebulbaDemoPageLocators.M_BUTTON, "M")

    def tap_m_button(self):
        self.click_element(*SebulbaDemoPageLocators.M_BUTTON)

    def should_be_reset_button(self):
        self.check_button(*SebulbaDemoPageLocators.RESET_BUTTON, "Reset")

    def tap_reset_button(self):
        self.click_element(*SebulbaDemoPageLocators.RESET_BUTTON)
