from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MoldingPageLocators


class MoldingPage(BasePage):
    def should_be_try_them_page_title(self):
        self.check_screen_title("Try Them On")

    def should_be_correct_try_them_page_subtitle(self):
        self.check_screen_subtitle("Pop your earbuds into your ears. Gently adjust them until they feel comfortable "
                                   "and secure.")

    def should_be_main_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def tap_main_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def should_be_get_ready_page_title(self):
        self.check_screen_title("Get Ready")

    def should_be_message_title1(self):
        expected_result = "1"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG_TITLE1)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message_title2(self):
        expected_result = "2"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG_TITLE2)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message_title3(self):
        expected_result = "3"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG_TITLE3)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message1(self):
        expected_result = "We'll do a quick sound test to ensure a sound-isolating fit before we mold."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG1)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_message2(self):
        expected_result = "We'll share some quick tips for achieving the best mold."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG2)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_message3(self):
        expected_result = "The 60 second molding magic starts."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG3)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_smile(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_SMILE_IMAGE)

    def should_be_stand_by_mirror_text(self):
        self.check_screen_subtitle("Try standing by a mirror for this part")

    def should_be_how_is_bass_title(self):
        self.check_screen_title("How’s the Bass?")

    def should_be_correct_how_is_bass_subtitle(self):
        self.check_screen_subtitle("Gently adjust your earbuds until you find the position that maximizes the bass.")

    def should_be_cancel_button(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)

    def should_be_cancel_button_text(self):
        expected_result = "CANCEL"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_cancel_button(self):
        self.click_element(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)

    def should_be_image_volume(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_IMAGE_VOLUME)

    def should_be_adjust_volume_bar(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_BAR_ADJUST_VOLUME)

    def should_be_starting_soon_title(self):
        expected_result = "Starting Soon"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_START_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_starting_soon_subtitle1(self):
        expected_result = "During the molding process,\n" \
                          " the tips will feel warm\n" \
                          " as they mold to your ears."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_START_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_starting_soon_subtitle2(self):
        expected_result = "Gently hold your earbuds in place the entire time."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_START_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_congratulations_title(self):
        self.check_screen_title("Congratulations!")

    def should_congratulations_subtitle(self):
        self.check_screen_subtitle("You now have perfectly fitting earbuds. Throw on your favorite song and take them "
                                   "for a spin.")

    def should_finish_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def should_finish_button_text(self):
        expected_result = "Finish"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_finish_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def should_be_progress_bar(self):
        self.is_element_present(*BasePageLocators.PROGRESS_BAR)
