from .base_page import BasePage
from .locators import BasePageLocators
from .locators import DemoPageLocators

from selenium.webdriver.common.by import By
import time


class DemoPage(BasePage):

    def should_be_app_version(self):
        assert self.is_element_present(*DemoPageLocators.DEMO_APP_VERSION)

    def should_be_left_label(self):
        actual_result = self.get_text(*DemoPageLocators.DEMO_LEFT_LABEL)
        expected_result = "Left:"
        assert actual_result == expected_result, f"Incorrect label '{actual_result}', should be '{expected_result}'"

    def should_be_right_label(self):
        actual_result = self.get_text(*DemoPageLocators.DEMO_RIGHT_LABEL)
        expected_result = "Right:"
        assert actual_result == expected_result, f"Incorrect label '{actual_result}', should be '{expected_result}'"

    def should_be_left_status(self):
        assert self.is_element_present(*DemoPageLocators.DEMO_LEFT_STATUS)

    def should_be_right_status(self):
        assert self.is_element_present(*DemoPageLocators.DEMO_RIGHT_STATUS)


class DemoSendCommandsPage(BasePage):
    def tap_debug_button(self):
        self.click_element(*DemoPageLocators.DEMO_DEBUG_BUTTON)

    def should_be_demo_molding_screen(self):
        actual_result = self.get_text(*BasePageLocators.TOOL_BAR_TITLE)
        expected_result = "Molding"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_demo_debug_screen(self):
        actual_result = self.get_text(*BasePageLocators.TOOL_BAR_TITLE)
        expected_result = "Debug"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def tap_first_commands_list_item(self):
        self.click_element(*DemoPageLocators.DEMO_FIRST_RESPONSE)

    def tap_second_commands_list_item(self):
        self.click_element(*DemoPageLocators.DEMO_SECOND_RESPONSE)

    def set_vendor_id(self):
        vendor_id = self.locate_element(*DemoPageLocators.DEMO_VENDOR_ID)
        vendor_id.send_keys("01DA")

    def enter_enable_curring_mode_command(self):
        command = self.locate_element(*DemoPageLocators.DEMO_COMMAND)
        command.send_keys("0422")

    def set_curring_mode_payload(self):
        payload = self.locate_element(*DemoPageLocators.DEMO_PAYLOAD)
        payload.send_keys("01")

    def tap_send_command_button(self):
        self.click_element(*DemoPageLocators.DEMO_SEND_COMMAND_BUTTON)

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
        expected_status = "Success"

        vendor_id = self.locate_element(*DemoPageLocators.DEMO_VENDOR_ID)
        vendor_id.clear()
        vendor_id.send_keys(set_vendor)
        command = self.locate_element(*DemoPageLocators.DEMO_COMMAND)
        command.clear()
        command.send_keys(set_command)
        payload = self.locate_element(*DemoPageLocators.DEMO_PAYLOAD)
        payload.clear()
        payload.send_keys(set_payload)

        self.tap_send_command_button()

        time.sleep(3)

        self.click_element(*DemoPageLocators.DEMO_FIRST_RESPONSE)
        self.click_element(*DemoPageLocators.DEMO_SECOND_RESPONSE)

        first_earbud_code = self.get_text(*DemoPageLocators.DEMO_SENT_COMMAND_FIRST)
        first_earbud_status = self.get_text(*DemoPageLocators.DEMO_SENT_COMMAND_FIRST_STATUS)
        first_earbud_payload = self.get_text(*DemoPageLocators.DEMO_SENT_COMMAND_FIRST_PAYLOAD)
        second_earbud_code = self.get_text(*DemoPageLocators.DEMO_SENT_COMMAND_SECOND)
        second_earbud_status = self.get_text(*DemoPageLocators.DEMO_SENT_COMMAND_SECOND_STATUS)
        second_earbud_payload = self.get_text(*DemoPageLocators.DEMO_SENT_COMMAND_SECOND_PAYLOAD)

        assert first_earbud_code == "0x" + set_command, f"Code `{first_earbud_code}` appears, should be \
                                                          `'0x' + {set_command}` "
        assert second_earbud_code == "0x" + set_command, f"Code `{second_earbud_code}` appears, should be \
                                                                  `'0x' + {set_command}` "
        assert first_earbud_status == expected_status, f"Status `{first_earbud_status}`, should be `{expected_status}`"
        assert second_earbud_status == expected_status, f"Status `{second_earbud_status}`, should be `{expected_status}`"
        assert first_earbud_payload == expected_payload, f"Payload {first_earbud_payload}, should be {expected_payload}"
        assert second_earbud_payload == expected_payload, f"Payload {second_earbud_payload}, should be {expected_payload}"
