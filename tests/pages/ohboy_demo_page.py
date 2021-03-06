from .base_page import BasePage
from .locators import OhboyDemoPageLocators

import time


class OhboyDemoPage(BasePage):
    def should_be_debug_button(self):
        assert self.is_element_present(*OhboyDemoPageLocators.DEBUG_BUTTON), "Debug button not located"

    def tap_debug_button(self):
        self.click_element(*OhboyDemoPageLocators.DEBUG_BUTTON)

    def should_be_demo_debug_screen(self):
        assert self.is_element_present(*OhboyDemoPageLocators.LIST_OF_RESPONSES), "No list of responses. Debug screen" \
                                                                                  " is not shown"

    def tap_first_commands_list_item(self):
        self.click_element(*OhboyDemoPageLocators.FIRST_RESPONSE)

    def tap_second_commands_list_item(self):
        self.click_element(*OhboyDemoPageLocators.SECOND_RESPONSE)

    def set_vendor_id(self):
        vendor_id = self.locate_element(*OhboyDemoPageLocators.VENDOR_ID)
        vendor_id.send_keys("01DA")

    def enter_enable_curring_mode_command(self):
        command = self.locate_element(*OhboyDemoPageLocators.COMMAND)
        command.send_keys("0422")

    def set_curring_mode_payload(self):
        payload = self.locate_element(*OhboyDemoPageLocators.PAYLOAD)
        payload.send_keys("01")

    def tap_send_command_button(self):
        assert self.is_element_present(*OhboyDemoPageLocators.SEND_COMMAND_BUTTON), "Send button not found"
        self.click_element(*OhboyDemoPageLocators.SEND_COMMAND_BUTTON)

    def activate_curring_mode(self):
        vendor_id = "01DA"
        command_id = "0422"
        payload_id = "01"
        expected_payload = "00"

        self.send_command(vendor_id, command_id, payload_id, expected_payload)

    def disable_tap_feature(self):
        vendor_id = "01DA"
        command_id = "0418"
        payload_id = "00"
        expected_payload = "00"

        self.send_command(vendor_id, command_id, payload_id, expected_payload)

    def enable_tap_feature(self):
        vendor_id = "01DA"
        command_id = "0418"
        payload_id = "01"
        expected_payload = "00"

        self.send_command(vendor_id, command_id, payload_id, expected_payload)

    def get_tap_feature_status_enabled(self):
        vendor_id = "01DA"
        command_id = "0419"
        payload_id = ""
        expected_payload = "0001"

        self.send_command(vendor_id, command_id, payload_id, expected_payload)

    def get_tap_feature_status_disabled(self):
        vendor_id = "01DA"
        command_id = "0419"
        payload_id = ""
        expected_payload = "0000"

        self.send_command(vendor_id, command_id, payload_id, expected_payload)

    def send_command(self, set_vendor, set_command, set_payload, expected_payload):
        expected_status = "success"
        # Enter necessary values
        vendor_id = self.locate_element(*OhboyDemoPageLocators.VENDOR_ID)
        vendor_id.clear()
        vendor_id.send_keys(set_vendor)
        command = self.locate_element(*OhboyDemoPageLocators.COMMAND)
        command.clear()
        command.send_keys(set_command)
        payload = self.locate_element(*OhboyDemoPageLocators.PAYLOAD)
        payload.clear()
        payload.send_keys(set_payload)
        # Send values
        self.tap_keyboard_return_key()
        self.tap_send_command_button()

        time.sleep(3)
        # Open two top elements
        self.click_element(*OhboyDemoPageLocators.FIRST_RESPONSE)
        self.click_element(*OhboyDemoPageLocators.SECOND_RESPONSE)
        # Get the results
        first_earbud_code = self.get_text(*OhboyDemoPageLocators.SENT_COMMAND_FIRST)
        first_earbud_status = self.get_text(*OhboyDemoPageLocators.SENT_COMMAND_FIRST_STATUS)
        first_earbud_payload = self.get_text(*OhboyDemoPageLocators.SENT_COMMAND_FIRST_PAYLOAD)
        second_earbud_code = self.get_text(*OhboyDemoPageLocators.SENT_COMMAND_SECOND)
        second_earbud_status = self.get_text(*OhboyDemoPageLocators.SENT_COMMAND_SECOND_STATUS)
        second_earbud_payload = self.get_text(*OhboyDemoPageLocators.SENT_COMMAND_SECOND_PAYLOAD)
        # Compare result to expectations
        assert first_earbud_code == "0x" + set_command, f"Code {first_earbud_code} appears, should be \
                                                          '0x' + {set_command} "
        assert second_earbud_code == "0x" + set_command, f"Code {second_earbud_code} appears, should be \
                                                                  '0x' + {set_command} "
        assert first_earbud_status == expected_status, f"Status {first_earbud_status}, should be {expected_status}"
        assert second_earbud_status == expected_status, f"Status {second_earbud_status}, should be {expected_status}"
        assert first_earbud_payload == expected_payload, f"Payload {first_earbud_payload}, should be " \
                                                         f"{expected_payload}"
        assert second_earbud_payload == expected_payload, f"Payload {second_earbud_payload}, should be " \
                                                          f"{expected_payload}"
