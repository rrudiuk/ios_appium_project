from .base_page import BasePage
from .locators import SupportPageLocators


class SupportPage(BasePage):
    def should_be_firmware_item(self):
        assert self.is_element_present(*SupportPageLocators.FIRMWARE_ITEM), "Firmware item doesn't appear on " \
                                                                            "Support screen"

    def tap_firmware_item(self):
        self.click_element(*SupportPageLocators.FIRMWARE_ITEM)
