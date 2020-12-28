from appium.webdriver.common.touch_action import TouchAction

from .base_page import BasePage
from .locators import EqPresetsPageLocators

import time

# Presets variables
ue_signature = "UE Signature"
bass_boost = "Bass Boost"
bright = "Bright"
hi_lo_boost = "Hi / Lo Boost"
loudness = "Loudness"
spoken_word = "Spoken Word"

"""Main screen with presets selection"""


class EqPresetsPage(BasePage):
    # Toolbar elements
    def should_be_toolbar(self):
        assert self.is_element_present(*EqPresetsPageLocators.TOOLBAR), "Toolbar is not shown"

    def should_be_save_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.SAVE_BUTTON), "Save button doesn't appear"

    def should_be_save_button_text(self):
        expected_result = "SAVE"
        actual_result = self.get_text(*EqPresetsPageLocators.SAVE_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_save_button(self):
        self.click_element(*EqPresetsPageLocators.SAVE_BUTTON)

    # EQ card elements
    def should_be_eq_expand_icon(self):
        assert self.is_element_present(*EqPresetsPageLocators.EXPAND_IMAGE), "Expand arrow doesn't appear"

    def tap_eq_expand_icon(self):
        self.click_element(*EqPresetsPageLocators.EXPAND_IMAGE)

    def should_be_eq_name(self):
        assert self.is_element_present(*EqPresetsPageLocators.CHOSEN_PRESET_NAME), "EQ name doesn't appear on Home " \
                                                                                   "screen "

    def check_selected_eq_preset(self, preset_name):
        expected_result = preset_name
        actual_result = self.get_text(*EqPresetsPageLocators.CHOSEN_PRESET_NAME)
        assert actual_result == expected_result, f"Preset {actual_result} is selected, should be {expected_result}"

    def should_be_ue_signature_eq_selected(self):
        self.check_selected_eq_preset(ue_signature)

    def should_be_bass_boost_eq_selected(self):
        self.check_selected_eq_preset(bass_boost)

    def should_be_bright_eq_selected(self):
        self.check_selected_eq_preset(bright)

    def should_be_hi_lo_boost_eq_selected(self):
        self.check_selected_eq_preset(hi_lo_boost)

    def should_be_loudness_eq_selected(self):
        self.check_selected_eq_preset(loudness)

    def should_be_spoken_word_eq_selected(self):
        self.check_selected_eq_preset(spoken_word)

    def should_be_eq_curve_image(self):
        assert self.is_element_present(*EqPresetsPageLocators.EQ_CURVE_IMAGE), "EQ curve doesn't apper on Home screen"

    def should_be_customize_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.CUSTOMIZE_BUTTON), "Customize button doesn't appear"

    def should_be_customize_button_text(self):
        expected_result = "Customize"
        actual_result = self.get_text(*EqPresetsPageLocators.CUSTOMIZE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button '{actual_result}', should be '{expected_result}'"

    def tap_customize_button(self):
        self.click_element(*EqPresetsPageLocators.CUSTOMIZE_BUTTON)

    # Expandable part elements
    def should_be_expandable_part(self):
        assert self.is_element_present(*EqPresetsPageLocators.EXPANDABLE_BLOCK), "Expandable part doesn't appear"

    def should_not_be_expandable_part(self):
        assert self.is_not_element_present(*EqPresetsPageLocators.EXPANDABLE_BLOCK), "Expandable part still appears"

    def should_be_divider_line(self):
        assert self.is_element_present(*EqPresetsPageLocators.DIVIDER_LINE), "Divider line doesn't appear"

    def should_be_presets_title(self):
        expected_result = "PRESETS"
        actual_result = self.get_text(*EqPresetsPageLocators.PRESETS_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_edit_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.EDIT_BUTTON), "Customize button doesn't appear"

    def should_be_edit_button_text(self):
        expected_result = "Edit"
        actual_result = self.get_text(*EqPresetsPageLocators.EDIT_BUTTON)
        assert actual_result == expected_result, f"Incorrect button '{actual_result}', should be '{expected_result}'"

    def tap_edit_button(self):
        self.click_element(*EqPresetsPageLocators.EDIT_BUTTON)

    def should_be_add_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.ADD_BUTTON)

    def tap_add_button(self):
        self.click_element(*EqPresetsPageLocators.ADD_BUTTON)

    def should_be_presets_list(self):
        assert self.is_element_present(*EqPresetsPageLocators.PRESETS_RECYCLER_VIEW), "Presets recycler view doesn't " \
                                                                                      "appear "

    def tap_recycler_view_first_element(self):
        presets = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        first_element = presets[1]
        first_element.click()
        time.sleep(3)
        images = self.locate_elements(*EqPresetsPageLocators.PRESET_IMAGE)
        dividers = self.locate_elements(*EqPresetsPageLocators.PRESET_DIVIDER)
        print("number of presets: " + str(len(presets)) + "\n")
        print("number of images: " + str(len(images)) + "\n")
        print("number of dividers: " + str(len(dividers)) + "\n")
        print(first_element.text)

    def presets_list_view_length(self, number_of_preset):
        expected_result = number_of_preset
        presets = len(self.locate_elements(*EqPresetsPageLocators.PRESET_NAME))
        images = len(self.locate_elements(*EqPresetsPageLocators.PRESET_IMAGE))
        dividers = len(self.locate_elements(*EqPresetsPageLocators.PRESET_DIVIDER))
        assert presets == expected_result and images == expected_result \
               and dividers == expected_result, f"There are {presets} presets, {images} images and {dividers} " \
                                                f"dividers. Should be {expected_result}"

    def should_be_one_preset(self):
        self.presets_list_view_length(1)

    def should_be_two_presets(self):
        self.presets_list_view_length(2)

    def should_be_three_presets(self):
        self.presets_list_view_length(3)

    def should_be_four_presets(self):
        self.presets_list_view_length(4)

    def should_be_five_presets(self):
        self.presets_list_view_length(5)

    def should_be_six_presets(self):
        self.presets_list_view_length(6)

    def should_be_seven_presets(self):
        self.presets_list_view_length(7)

    def should_be_eight_presets(self):
        self.presets_list_view_length(8)

    def should_be_nine_presets(self):
        self.presets_list_view_length(9)

    def should_be_ten_presets(self):
        self.presets_list_view_length(10)

    def should_be_hundred_presets(self):
        self.presets_list_view_length(100)

    def should_be_initial_preset_order(self):
        self.check_preset_order(first_preset=ue_signature, second_preset=bass_boost, third_preset=bright,
                                fourth_preset=hi_lo_boost, fifth_preset=loudness, sixth_preset=spoken_word)

    def should_be_preset_order_after_moving_ue_signature_to_fourth(self):
        self.check_preset_order(first_preset=bass_boost, second_preset=bright, third_preset=hi_lo_boost,
                                fourth_preset=ue_signature, fifth_preset=loudness, sixth_preset=spoken_word)

    def check_preset_order(self, first_preset, second_preset, third_preset, fourth_preset, fifth_preset, sixth_preset):
        presets = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        assert presets[0].text == first_preset and presets[1].text == second_preset and \
               presets[2].text == third_preset and presets[3].text == fourth_preset and \
               presets[4].text == fifth_preset and presets[5].text == sixth_preset, \
            f"First preset {first_preset}, should be {presets[0].text}, " \
            f"second preset {second_preset}, should be {presets[1].text}, " \
            f"third preset {third_preset}, should be {presets[2].text}, " \
            f"fourth preset {fourth_preset}, should be {presets[3].text}, " \
            f"fifth preset {fifth_preset}, should be {presets[4].text}, " \
            f"fourth preset {sixth_preset}, should be {presets[5].text}, "

    def select_preset(self, preset_position):
        presets = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        eq_preset = presets[preset_position]
        eq_preset_name = eq_preset.text
        eq_preset.click()
        self.check_selected_eq_preset(eq_preset_name)

    def select_1_preset(self):
        self.select_preset(0)

    def select_2_preset(self):
        self.select_preset(1)

    def select_3_preset(self):
        self.select_preset(2)

    def select_4_preset(self):
        self.select_preset(3)

    def select_5_preset(self):
        self.select_preset(4)

    def select_6_preset(self):
        self.select_preset(5)


"""Screen that allows managing presets order and delete them"""


class EditPresetsPage(EqPresetsPage):
    def presets_list_view_length(self, number_of_preset):
        expected_result = number_of_preset
        presets = len(self.locate_elements(*EqPresetsPageLocators.PRESET_NAME))
        images = len(self.locate_elements(*EqPresetsPageLocators.PRESET_IMAGE))
        dividers = len(self.locate_elements(*EqPresetsPageLocators.PRESET_DIVIDER))
        remove_icons = len(self.locate_elements(*EqPresetsPageLocators.REMOVE_PRESET_ICON))
        drag_icons = len(self.locate_elements(*EqPresetsPageLocators.DRAG_PRESET_ICON))
        assert presets == expected_result and images == expected_result \
               and dividers == expected_result and remove_icons == expected_result - 1 \
               and drag_icons == expected_result, f"There are {presets} presets, {images} images, {dividers} " \
                                                  f"dividers, drag icons {drag_icons}. Should be {expected_result}. " \
                                                  f"And there is {remove_icons} remove icons. Should be " \
                                                  f"{expected_result - 1}"

    def should_be_edit_preset_title(self):
        self.check_screen_title("EDIT PRESETS")

    def should_be_presets_list(self):
        assert self.is_element_present(*EqPresetsPageLocators.EDIT_PRESETS_LIST), "Presets recycler view doesn't " \
                                                                                  "appear "

    def reorder_preset_up(self, initial_position, drag_to):
        names_before = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        name_moved_preset = names_before[initial_position].text
        drag_icons = self.locate_elements(*EqPresetsPageLocators.DRAG_PRESET_ICON)
        start = drag_icons[initial_position]
        end = drag_icons[drag_to]
        TouchAction(self.driver).long_press(start).move_to(end).release().perform()
        names_after = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        current_preset = names_after[initial_position].text
        expected_preset = names_after[drag_to - 1].text

        assert name_moved_preset != current_preset and name_moved_preset == expected_preset, \
            f"Preset under the test {name_moved_preset}. On its position now {current_preset}, on expected " \
            f"position now {expected_preset}"

    def reorder_preset_down(self, initial_position, drag_to):
        names_before = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        name_moved_preset = names_before[initial_position].text
        drag_icons = self.locate_elements(*EqPresetsPageLocators.DRAG_PRESET_ICON)
        start = drag_icons[initial_position]
        end = drag_icons[drag_to]
        TouchAction(self.driver).long_press(start).move_to(end).release().perform()
        names_after = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        current_preset = names_after[initial_position].text
        expected_preset = names_after[drag_to + 1].text

        assert name_moved_preset != current_preset and name_moved_preset == expected_preset, \
            f"Preset under the test {name_moved_preset}. On its position now {current_preset}, on expected " \
            f"position now {expected_preset}"

    def move_first_preset_to_fourth_position(self):
        self.reorder_preset_up(0, 4)

    def move_second_preset_to_fourth_position(self):
        self.reorder_preset_up(1, 4)

    def move_six_preset_to_second_position(self):
        self.reorder_preset_down(5, 0)

    def move_three_to_four_position(self):
        self.reorder_preset_up(2, 4)

    def tap_to_delete_preset(self, index):
        presets = self.locate_elements(*EqPresetsPageLocators.REMOVE_PRESET_ICON)
        preset_to_delete = presets[index]
        preset_to_delete.click()

    def delete_top_preset(self):
        self.tap_to_delete_preset(0)

    def delete_third_preset(self):
        self.tap_to_delete_preset(1)

    def delete_fourth_preset(self):
        self.tap_to_delete_preset(2)

    def delete_fifth_preset(self):
        self.tap_to_delete_preset(3)

    def delete_sixth_preset(self):
        self.tap_to_delete_preset(4)


"""Screen that allows to configure preset values"""


class EqPresetSetupPage(EqPresetsPage):
    def should_be_new_preset_setup_title(self):
        self.check_screen_title("New preset")

    def should_be_eq_editor(self):
        assert self.is_element_present(*EqPresetsPageLocators.EQ_EDITOR), "EQ editor is missing"

    def should_be_history_title(self):
        expected_result = "HISTORY"
        actual_result = self.get_text(*EqPresetsPageLocators.HISTORY_TITLE)
        assert actual_result == expected_result, f"Title {actual_result}, should be {expected_result}"

    def should_be_backward_arrow(self):
        assert self.is_element_present(*EqPresetsPageLocators.BACKWARD_ARROW), "Backwards arrow is missing"

    def should_be_forward_arrow(self):
        assert self.is_element_present(*EqPresetsPageLocators.FORWARD_ARROW), "Forward arrow is missing"

    def should_be_history_progress_bar(self):
        assert self.is_element_present(*EqPresetsPageLocators.PROGRESS_HISTORY_BAR), "History progress bar is " \
                                                                                     "missing"
