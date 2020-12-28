from .base_page import BasePage
from .locators import BasePageLocators
from .locators import FirmwareUpdatePageLocators

import time


class FirmwareUpdatePage(BasePage):
    def should_be_page_title(self):
        assert self.is_element_present(*BasePageLocators.SCREEN_TITLE)

    def activate_fw_update(self):
        tries = 10
        while tries > 0:
            title = self.get_text(*BasePageLocators.SCREEN_TITLE)
            if title == 'Up to Date':
                self.click_element_10_times(*BasePageLocators.SCREEN_TITLE)
                tries = tries - 1
            else:
                break

    def tap_page_title_10_times(self):
        self.click_element_10_times(*BasePageLocators.SCREEN_TITLE)

    def should_be_update_available_title(self):
        self.check_screen_title("Update Available")

    def tap_update_earbuds_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def should_be_ready_to_update_title(self):
        self.check_screen_title("Ready to Update")

    def tap_install_now_button(self):
        self.click_element(*FirmwareUpdatePageLocators.UPDATE_BUTTON)

    def check_active_update(self):
        tries = 45
        duration = 0
        check_period = 20
        installing_title = "Installing"
        while tries > 0:
            if self.get_text(*BasePageLocators.SCREEN_TITLE) == installing_title:
                tries = tries - 1
                time.sleep(check_period)
                duration = duration + check_period
            else:
                break

        if self.get_text(*BasePageLocators.SCREEN_TITLE) == "Restarting":
            time.sleep(30)
            duration = duration + 30

        final_screen_title = self.get_text(*BasePageLocators.SCREEN_TITLE)
        expected_result = 'Firmware Update Available'
        expected_result2 = 'Support'

        print(duration)

        assert final_screen_title == expected_result or final_screen_title == expected_result2, \
            f"Screen title {final_screen_title}, update failed!"
