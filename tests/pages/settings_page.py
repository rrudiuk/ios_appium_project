import time

from .base_page import BasePage
from .locators import SettingsPageLocators


class SettingsPage(BasePage):
    def should_be_back_arrow(self):
        self.is_element_present(*SettingsPageLocators.SETTINGS_BACK_BUTTON), "Back arrow not located"

    def should_be_settings_title(self):
        self.check_screen_title(*SettingsPageLocators.SETTINGS_TITLE, "Settings")

    def should_be_save_button(self):
        self.is_element_present(*SettingsPageLocators.SAVE_BUTTON), "Save button not located"

    def save_selection(self):
        assert self.is_element_present(*SettingsPageLocators.SAVE_BUTTON), "Save button not found"
        self.click_element(*SettingsPageLocators.SAVE_BUTTON)
        time.sleep(2)

    def tap_back_arrow(self):
        self.is_element_present(*SettingsPageLocators.SETTINGS_BACK_BUTTON), "Back arrow not located"
        self.click_element(*SettingsPageLocators.SETTINGS_BACK_BUTTON)

    # Name
    def should_be_name_item(self):
        assert self.is_element_present(*SettingsPageLocators.NAME_ITEM), "Name item not found"
        self.check_message(*SettingsPageLocators.NAME_TITLE, "NAME")
        assert self.is_element_present(*SettingsPageLocators.NAME_VALUE), "Name of earbuds not found"
        assert self.is_element_present(*SettingsPageLocators.NAME_ACTION_ARROW), "Name action arrow not found"
        assert self.is_element_present(*SettingsPageLocators.NAME_DIVIDER), "Name divider not found"

    def tap_name_item(self):
        assert self.is_element_present(*SettingsPageLocators.NAME_ITEM), "Name item not found"
        self.click_element(*SettingsPageLocators.NAME_ITEM)

    # Edit name screen
    def should_be_edit_name_title(self):
        self.check_screen_title(*SettingsPageLocators.EDIT_NAME_TITLE, "Edit Name")

    def should_be_name_title(self):
        self.check_message(*SettingsPageLocators.NAME_TITLE, "NAME")

    def should_be_name_input(self):
        self.is_element_present(*SettingsPageLocators.EDIT_NAME_INPUT), "Name input not found"

    def should_be_name_input_clear(self):
        self.is_element_present(*SettingsPageLocators.EDIT_NAME_INPUT_CLEAR), "Clear X button in name input not found"

    def clear_name_input_field(self):
        self.click_element(*SettingsPageLocators.EDIT_NAME_INPUT_CLEAR)
        time.sleep(2)

    def should_be_edit_name_hint(self):
        self.check_message(*SettingsPageLocators.EDIT_NAME_HINT, "Your earbuds will disconnect and restart\nto finish "
                                                                 "the renaming process.\n\nOnce restarted, "
                                                                 "un-pair and re-pair your earbuds for the changes to "
                                                                 "take effect.")

    def should_be_update_name_button(self):
        self.check_button(*SettingsPageLocators.EDIT_NAME_BUTTON_TEXT, "Update Name")

    def should_be_disabled_update_button(self):
        assert not self.is_element_enabled(*SettingsPageLocators.EDIT_NAME_BUTTON), "Update Name button is enabled," \
                                                                                    " should be disabled"

    def should_be_enabled_update_button(self):
        assert self.is_element_enabled(*SettingsPageLocators.EDIT_NAME_BUTTON), "Update Name button is disabled, " \
                                                                                "should be enabled"

    # Test names on edit name screen
    def should_be_empty_input_field(self):
        expected_result = ""
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_0_letters_shown_for_empty_input_field(self):
        expected_result = "0 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_4_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "NAME")

    def should_be_4_letter_name(self):
        expected_result = "NAME"
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_4_letters_shown_for_4_letters_name(self):
        expected_result = "4 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_11_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "hello world")

    def should_be_11_letter_name(self):
        expected_result = "hello world"
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_11_letters_shown_for_4_letters_name(self):
        expected_result = "11 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_16_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "hello world! hey")

    def should_be_16_letter_name(self):
        expected_result = "hello world! hey"
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_16_letters_shown_for_4_letters_name(self):
        expected_result = "16 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_over_max_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "hello world! hey hey hey!")

    # ------SINGLE TAP SWITCHER-------
    def should_be_single_tap_switcher(self):
        self.check_message(*SettingsPageLocators.SINGLE_TAP_TITLE, "SINGLE TAP")
        self.check_message(*SettingsPageLocators.SINGLE_TAP_STATUS_TITLE, "Off / On")
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_STATUS_DIVIDER), "Single tap divider not found"

    def single_tap_enabled_check(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        expected_state = "1"
        actual_state = self.get_text(*SettingsPageLocators.SINGLE_TAP_SWITCHER)
        assert actual_state == expected_state, f"Incorrect state '{actual_state}', should be '{expected_state}'"

    def single_tap_disabled_check(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        expected_state = "0"
        actual_state = self.get_text(*SettingsPageLocators.SINGLE_TAP_SWITCHER)
        assert actual_state == expected_state, f"Incorrect state '{actual_state}', should be '{expected_state}'"

    def toggle_on_single_tap(self):
        if self.get_text(*SettingsPageLocators.SINGLE_TAP_SWITCHER) == '0':
            self.toggle_single_tap_state()
            time.sleep(2)

    def toggle_single_tap_state(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_SWITCHER)
        time.sleep(2)

    # Left single tap
    def should_be_left_single_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item not found"
        self.check_message(*SettingsPageLocators.SINGLE_TAP_LEFT_TITLE, "LEFT")
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE), "Left single tap selection " \
                                                                                     "not found"
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ACTION_ARROW), "Left single tap arrow " \
                                                                                            "not found"
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_DIVIDER), "Left single tap divider " \
                                                                                       "not found"

    def should_not_be_left_single_tap_item(self):
        assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item found " \
                                                                                        "but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE), "Left single tap selection " \
                                                                                         "found but shouldn't be"
        # assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ACTION_ARROW), \
        #     "Left single tap arrow found but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_DIVIDER), "Left single tap divider" \
                                                                                           " found but shouldn't be"

    def tap_left_single_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM)

    # Right single tap
    def should_be_right_single_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item not found"
        self.check_message(*SettingsPageLocators.SINGLE_TAP_RIGHT_TITLE, "RIGHT")
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE), "Right single tap selection" \
                                                                                      " not found"
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ACTION_ARROW), "Right single tap arrow" \
                                                                                             " not found"
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_DIVIDER), "Right single tap divider" \
                                                                                        " not found"

    def should_not_be_right_single_tap_item(self):
        assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item " \
                                                                                         "found but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE), "Right single tap selection" \
                                                                                          " found but shouldn't be"
        # assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ACTION_ARROW), \
        #     "Right single tap arrow found but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_DIVIDER), "Right single tap divider" \
                                                                                            " found but shouldn't be"

    def tap_right_single_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM)

    # Single tap screen
    def should_be_single_tap_left_screen_title(self):
        self.check_screen_title(*SettingsPageLocators.SINGLE_TAP_LEFT_SCREEN_TITLE, "Single Tap - Left")

    def should_be_single_tap_right_screen_title(self):
        self.check_screen_title(*SettingsPageLocators.SINGLE_TAP_RIGHT_SCREEN_TITLE, "Single Tap - Right")

    def should_be_single_tap_items_screen(self):
        self.check_button(*SettingsPageLocators.PLAY_PAUSE, "Play / Pause")
        self.check_button(*SettingsPageLocators.NEXT_TRACK, "Next Track")
        self.check_button(*SettingsPageLocators.PREVIOUS_TRACK, "Previous Track")
        self.check_button(*SettingsPageLocators.VOLUME_UP, "Volume Up")
        self.check_button(*SettingsPageLocators.VOLUME_DOWN, "Volume Down")

    # Select each single tap item
    def select_single_tap_play_pause(self):
        self.check_button(*SettingsPageLocators.PLAY_PAUSE, "Play / Pause")
        self.click_element(*SettingsPageLocators.PLAY_PAUSE)

    def select_single_tap_next_track(self):
        self.check_button(*SettingsPageLocators.NEXT_TRACK, "Next Track")
        self.click_element(*SettingsPageLocators.NEXT_TRACK)

    def select_single_tap_previous_track(self):
        self.check_button(*SettingsPageLocators.PREVIOUS_TRACK, "Previous Track")
        self.click_element(*SettingsPageLocators.PREVIOUS_TRACK)

    def select_single_tap_volume_up(self):
        self.check_button(*SettingsPageLocators.VOLUME_UP, "Volume Up")
        self.click_element(*SettingsPageLocators.VOLUME_UP)

    def select_single_tap_volume_down(self):
        self.check_button(*SettingsPageLocators.VOLUME_DOWN, "Volume Down")
        self.click_element(*SettingsPageLocators.VOLUME_DOWN)

    # Check if single tap left was selected correctly
    def should_be_play_pause_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Play / Pause")

    def should_be_next_track_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Next Track")

    def should_be_previous_track_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Previous Track")

    def should_be_volume_up_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Volume Up")

    def should_be_volume_down_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Volume Down")

    # Check if single tap right was selected correctly
    def should_be_play_pause_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Play / Pause")

    def should_be_next_track_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Next Track")

    def should_be_previous_track_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Previous Track")

    def should_be_volume_up_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Volume Up")

    def should_be_volume_down_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Volume Down")

    # ------DOUBLE TAP SWITCHER-----
    def should_be_double_tap_switcher(self):
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_TITLE, "DOUBLE TAP")
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_STATUS_TITLE, "Off / On")
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_SWITCHER), "Double tap switcher not found"
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_STATUS_DIVIDER), "Double tap divider not found"

    def double_tap_enabled_check(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_SWITCHER), "Double tap switcher not found"
        expected_state = "1"
        actual_state = self.get_text(*SettingsPageLocators.DOUBLE_TAP_SWITCHER)
        assert actual_state == expected_state, f"Incorrect state '{actual_state}', should be '{expected_state}'"

    def double_tap_disabled_check(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_SWITCHER), "Double tap switcher not found"
        expected_state = "0"
        actual_state = self.get_text(*SettingsPageLocators.DOUBLE_TAP_SWITCHER)
        assert actual_state == expected_state, f"Incorrect state '{actual_state}', should be '{expected_state}'"

    def double_single_tap_state(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_SWITCHER), "Double tap switcher not found"
        self.click_element(*SettingsPageLocators.DOUBLE_TAP_SWITCHER)

    def toggle_on_double_tap(self):
        if self.get_text(*SettingsPageLocators.DOUBLE_TAP_SWITCHER) == '0':
            self.toggle_double_tap_state()
            time.sleep(2)

    def toggle_double_tap_state(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_SWITCHER), "Double tap switcher not found"
        self.click_element(*SettingsPageLocators.DOUBLE_TAP_SWITCHER)

    # Left double tap
    def should_be_left_double_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM), "Left double tap item not found"
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_LEFT_TITLE, "LEFT")
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE), "Left double tap selection " \
                                                                                     "not found"
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ACTION_ARROW), "Left double tap arrow " \
                                                                                            "not found"
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_DIVIDER), "Left double tap divider " \
                                                                                       "not found"

    def should_not_be_left_double_tap_item(self):
        assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM), "Left double tap item found" \
                                                                                        " but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE), "Left double tap selection " \
                                                                                         "found but shouldn't be"
        # assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ACTION_ARROW), \
        #     "Left double tap arrow found but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_DIVIDER), "Left double tap divider" \
                                                                                           " found but shouldn't be"

    def tap_left_double_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM), "Left double tap item not found"
        self.click_element(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM)

    # Right double tap
    def should_be_right_double_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM), "Right double tap item not found"
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_RIGHT_TITLE, "RIGHT")
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE), "Right double tap selection " \
                                                                                      "not found"
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ACTION_ARROW), "Right double tap arrow" \
                                                                                             " not found"
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_DIVIDER), "Right double tap divider " \
                                                                                        "not found"

    def should_not_be_right_double_tap_item(self):
        assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM), "Right double tap item" \
                                                                                         " found but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE), "Right double tap selection" \
                                                                                          " found but shouldn't be"
        # assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ACTION_ARROW), \
        #     "Right double tap arrow found  but shouldn't be"
        assert self.is_not_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_DIVIDER), "Right double tap divider" \
                                                                                            " found but shouldn't be"

    def tap_right_double_tap_item(self):
        assert self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM), "Right double tap item not found"
        self.click_element(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM)

    # Double tap screen
    def should_be_double_tap_left_screen_title(self):
        self.check_screen_title(*SettingsPageLocators.DOUBLE_TAP_LEFT_SCREEN_TITLE, "Double Tap - Left")

    def should_be_double_tap_right_screen_title(self):
        self.check_screen_title(*SettingsPageLocators.DOUBLE_TAP_RIGHT_SCREEN_TITLE, "Double Tap - Right")

    def should_be_double_tap_items_screen(self):
        self.check_button(*SettingsPageLocators.SIRI, "Siri")
        self.check_button(*SettingsPageLocators.PLAY_PAUSE, "Play / Pause")
        self.check_button(*SettingsPageLocators.NEXT_TRACK, "Next Track")
        self.check_button(*SettingsPageLocators.PREVIOUS_TRACK, "Previous Track")
        self.check_button(*SettingsPageLocators.VOLUME_UP, "Volume Up")
        self.check_button(*SettingsPageLocators.VOLUME_DOWN, "Volume Down")

    # Select each double tap item
    def select_double_tap_siri(self):
        self.check_button(*SettingsPageLocators.SIRI, "Siri")
        self.click_element(*SettingsPageLocators.SIRI)

    def select_double_tap_play_pause(self):
        self.check_button(*SettingsPageLocators.PLAY_PAUSE, "Play / Pause")
        self.click_element(*SettingsPageLocators.PLAY_PAUSE)

    def select_double_tap_next_track(self):
        self.check_button(*SettingsPageLocators.NEXT_TRACK, "Next Track")
        self.click_element(*SettingsPageLocators.NEXT_TRACK)

    def select_double_tap_previous_track(self):
        self.check_button(*SettingsPageLocators.PREVIOUS_TRACK, "Previous Track")
        self.click_element(*SettingsPageLocators.PREVIOUS_TRACK)

    def select_double_tap_volume_up(self):
        self.check_button(*SettingsPageLocators.VOLUME_UP, "Volume Up")
        self.click_element(*SettingsPageLocators.VOLUME_UP)

    def select_double_tap_volume_down(self):
        self.check_button(*SettingsPageLocators.VOLUME_DOWN, "Volume Down")
        self.click_element(*SettingsPageLocators.VOLUME_DOWN)

    # Check if double tap left was selected correctly
    def should_be_siri_selected_double_tap_left(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE, "Siri")

    def should_be_play_pause_selected_double_tap_left(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE, "Play / Pause")

    def should_be_next_track_selected_double_tap_left(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE, "Next Track")

    def should_be_previous_track_selected_double_tap_left(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE, "Previous Track")

    def should_be_volume_up_selected_double_tap_left(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE, "Volume Up")

    def should_be_volume_down_selected_double_tap_left(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE, "Volume Down")

    # Check if double tap right was selected correctly
    def should_be_siri_selected_double_tap_right(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE, "Siri")

    def should_be_play_pause_selected_double_tap_right(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE, "Play / Pause")

    def should_be_next_track_selected_double_tap_right(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE, "Next Track")

    def should_be_previous_track_selected_double_tap_right(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE, "Previous Track")

    def should_be_volume_up_selected_double_tap_right(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE, "Volume Up")

    def should_be_volume_down_selected_double_tap_right(self):
        self.check_button(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE, "Volume Down")

    # -------DARK MODE-------
    def should_be_dark_mode_item(self):
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_ITEM), "Dark mode item not found"
        self.check_message(*SettingsPageLocators.DARK_MODE_TITLE, "DARK MODE")
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_VALUE), "Dark mode value not found"
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_ACTION_ARROW), "Dark mode action arrow not found"
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_DIVIDER), "Dark mode divider not found"

    def should_be_dark_mode_on(self):
        expected_result = "On"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_VALUE)
        assert actual_result == expected_result, f"Dark mode is set to '{actual_result}', should be '{expected_result}'"

    def should_be_dark_mode_off(self):
        expected_result = "Off"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_VALUE)
        assert actual_result == expected_result, f"Dark mode is set to '{actual_result}', should be '{expected_result}'"

    def should_be_dark_mode_use_device_settings(self):
        expected_result = "Use System Setting"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_VALUE)
        assert actual_result == expected_result, f"Dark mode is set to '{actual_result}', should be '{expected_result}'"

    def tap_dark_mode_item(self):
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_ITEM), "Dark mode item not found"
        self.click_element(*SettingsPageLocators.DARK_MODE_ITEM)

    # Dark mode screen
    def should_be_dark_mode_screen_title(self):
        self.check_screen_title(*SettingsPageLocators.DARK_MODE_SCREEN_TITLE, "Dark Mode")

    def should_be_dark_mode_switcher_item(self):
        self.check_button(*SettingsPageLocators.DARK_MODE_SWITCHER_TITLE, "Dark Mode")
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_SWITCHER), "Dark mode switcher not found"
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_SWITCHER_DIVIDER), "Dark mode switcher " \
                                                                                          "divider not found"

    def should_be_dark_mode_switcher_on(self):
        expected_result = "1"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_SWITCHER)
        assert actual_result == expected_result, f"Switcher is {actual_result}, should be {expected_result}"

    def should_be_dark_mode_switcher_off(self):
        expected_result = "0"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_SWITCHER)
        assert actual_result == expected_result, f"Switcher is {actual_result}, should be {expected_result}"

    def tap_dark_mode_switcher(self):
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_SWITCHER), "Dark mode switcher not found"
        self.click_element(*SettingsPageLocators.DARK_MODE_SWITCHER)

    def should_be_dark_mode_device_default_switcher_item(self):
        self.check_button(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_SWITCHER_TITLE, "Use Device Settings")
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_SWITCHER), "Device default " \
                                                                                                 "switcher not found"
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_DIVIDER), "Dark mode switcher" \
                                                                                                " divider not found"

    def should_be_dark_mode_device_default_switcher_on(self):
        expected_result = "1"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_SWITCHER)
        assert actual_result == expected_result, f"Switcher is {actual_result}, should be {expected_result}"

    def should_be_dark_mode_device_default_switcher_off(self):
        expected_result = "0"
        actual_result = self.get_text(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_SWITCHER)
        assert actual_result == expected_result, f"Switcher is {actual_result}, should be {expected_result}"

    def tap_dark_mode_device_default_switcher(self):
        assert self.is_element_present(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_SWITCHER), \
            "Devices default switcher not found"
        self.click_element(*SettingsPageLocators.DARK_MODE_DEVICE_DEFAULT_SWITCHER)

    def should_be_dark_mode_hint(self):
        self.check_message(*SettingsPageLocators.DARK_MODE_HINT, "Set Dark mode to use the Light or Dark selection"
                                                                 " located in your device Display settings.")

    # -----LANGUAGE------
    def should_be_language_item(self):
        assert self.is_element_present(*SettingsPageLocators.LANGUAGE_ITEM), "Language item not found"
        self.check_message(*SettingsPageLocators.LANGUAGE_TITLE, "LANGUAGE")
        assert self.is_element_present(*SettingsPageLocators.LANGUAGE_VALUE), "Language value not found"
        assert self.is_element_present(*SettingsPageLocators.LANGUAGE_ACTION_ARROW), "Language action arrow not found"
        assert self.is_element_present(*SettingsPageLocators.LANGUAGE_DIVIDER), "Language divider not found"

    def tap_language_item(self):
        assert self.is_element_present(*SettingsPageLocators.LANGUAGE_ITEM), "Language item not found"
        self.click_element(*SettingsPageLocators.LANGUAGE_ITEM)

    # Language screen
    def should_be_language_title(self):
        self.check_screen_title(*SettingsPageLocators.LANGUAGE_SCREEN_TITLE, "Language")

    def should_be_language_screen(self):
        self.should_be_language_title()
        self.should_be_back_arrow()
        self.should_be_save_button()
        self.check_button(*SettingsPageLocators.SYSTEM_DEFAULT, "System default")
        self.check_button(*SettingsPageLocators.DEUTSCH, "Deutsch")
        self.check_button(*SettingsPageLocators.ENGLISH, "English")
        self.check_button(*SettingsPageLocators.SPANISH, "Español")
        self.check_button(*SettingsPageLocators.FRENCH, "Français")
        self.check_button(*SettingsPageLocators.ITALIAN, "Italiano")

    # Select each language item
    def select_system_default_language(self):
        assert self.is_element_present(*SettingsPageLocators.SYSTEM_DEFAULT), "System default item not located"
        self.click_element(*SettingsPageLocators.SYSTEM_DEFAULT)

    def select_deutsch_language(self):
        self.check_button(*SettingsPageLocators.DEUTSCH, "Deutsch")
        self.click_element(*SettingsPageLocators.DEUTSCH)

    def select_english_language(self):
        self.check_button(*SettingsPageLocators.ENGLISH, "English")
        self.click_element(*SettingsPageLocators.ENGLISH)

    def select_spanish_language(self):
        self.check_button(*SettingsPageLocators.SPANISH, "Español")
        self.click_element(*SettingsPageLocators.SPANISH)

    def select_french_language(self):
        self.check_button(*SettingsPageLocators.FRENCH, "Français")
        self.click_element(*SettingsPageLocators.FRENCH)

    def select_italian_language(self):
        self.check_button(*SettingsPageLocators.ITALIAN, "Italiano")
        self.click_element(*SettingsPageLocators.ITALIAN)

    # Check if language was selected correctly
    def should_be_system_default_language(self):
        self.check_button(*SettingsPageLocators.LANGUAGE_VALUE, "System default")

    def should_be_deutsch_language(self):
        self.check_button(*SettingsPageLocators.LANGUAGE_VALUE, "Deutsch")

    def should_be_english_language(self):
        self.check_button(*SettingsPageLocators.LANGUAGE_VALUE, "English")

    def should_be_spanish_language(self):
        self.check_button(*SettingsPageLocators.LANGUAGE_VALUE, "Español")

    def should_be_french_language(self):
        self.check_button(*SettingsPageLocators.LANGUAGE_VALUE, "Français")

    def should_be_italian_language(self):
        self.check_button(*SettingsPageLocators.LANGUAGE_VALUE, "Italiano")
