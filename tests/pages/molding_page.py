from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MoldingPageLocators


class MoldingPage(BasePage):
    # Try them on screen
    def should_be_try_them_page_title(self):
        self.check_screen_title(*MoldingPageLocators.TRY_THEM_PAGE_TITLE, "Try Them On")

    def should_be_correct_try_them_page_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.TRY_THEM_PAGE_SUBTITLE, "Pop your earbuds into your ears. "
                                                                                "Gently adjust\nthem until they feel "
                                                                                "comfortable and secure. ")

    def should_be_try_them_animation(self):
        assert self.is_element_present(*MoldingPageLocators.TRY_THEM_PAGE_ANIMATION), "Animation doesn't appear on " \
                                                                                      "Try them on screen"

    def should_be_try_them_button(self):
        assert self.is_element_present(*MoldingPageLocators.TRY_THEM_PAGE_BUTTON), "Next button on try them on screen" \
                                                                                   " not found"

    def tap_try_them_button(self):
        self.click_element(*MoldingPageLocators.TRY_THEM_PAGE_BUTTON)

    # Get ready screen
    def should_be_get_ready_page_title(self):
        self.check_screen_title(*MoldingPageLocators.GET_READY_TITLE, "Get Ready")

    def should_be_message_title1(self):
        self.check_screen_title(*MoldingPageLocators.MOLDING_TEXT_VIEW_TITLE1, "1")

    def should_be_message_title2(self):
        self.check_screen_title(*MoldingPageLocators.MOLDING_TEXT_VIEW_TITLE2, "2")

    def should_be_message_title3(self):
        self.check_screen_title(*MoldingPageLocators.MOLDING_TEXT_VIEW_TITLE3, "3")

    def should_be_message1(self):
        self.check_message(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG1, "We’ll do a quick sound test to ensure "
                                                                        "a\nsound-isolating fit before we mold.")

    def should_be_message2(self):
        self.check_message(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG2, "We’ll share some quick tips for\nachieving "
                                                                        "the best mold.")

    def should_be_message3(self):
        self.check_message(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG3, "The 60 second molding magic starts.")

    def should_be_smile(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_SMILE_IMAGE), "No smile icon on Get Ready screen"

    def should_be_stand_by_mirror_text(self):
        self.check_message(*MoldingPageLocators.MOLDING_STAND_BY_MIRROR, "Try standing by a mirror for this part")

    def should_be_do_this_button(self):
        assert self.is_element_present(*MoldingPageLocators.GET_READY_BUTTON), "Let's do this button not found"

    def should_be_do_this_button_text(self):
        self.check_button_text(*MoldingPageLocators.GET_READY_BUTTON, "Let’s Do This")

    def tap_do_this_button(self):
        self.click_element(*MoldingPageLocators.GET_READY_BUTTON)

    # How is the bass
    def should_be_how_is_bass_title(self):
        self.check_screen_title(*MoldingPageLocators.HOW_IS_THE_BASS_TITLE, "How’s the Bass?")

    def should_be_correct_how_is_bass_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.HOW_IS_THE_BASS_SUBTITLE, "Gently adjust your earbuds until "
                                                                                  "you find the\nposition that "
                                                                                  "maximizes the bass.")

    def should_be_cancel_button(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_CANCEL_BUTTON), "No Cancel button on How is the " \
                                                                                    "bass screen"

    def should_be_cancel_button_text(self):
        self.check_button_text(*MoldingPageLocators.MOLDING_CANCEL_BUTTON, "CANCEL")

    def tap_cancel_button(self):
        self.click_element(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)

    def should_be_image_volume(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_IMAGE_VOLUME)

    def should_be_adjust_volume_bar(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_BAR_ADJUST_VOLUME)

    def should_be_starting_soon_title(self):
        self.check_screen_title(*MoldingPageLocators.MOLDING_START_TITLE, "Starting Soon")

    def should_be_starting_soon_subtitle1(self):
        self.check_screen_subtitle(*MoldingPageLocators.MOLDING_START_SUBTITLE, "During the molding process,\nthe "
                                                                                "tips will feel warm\nas they mold to"
                                                                                " your ears.")

    def should_be_starting_soon_subtitle2(self):
        self.check_screen_subtitle(*MoldingPageLocators.MOLDING_START_SUBTITLE2, "Gently hold your earbuds\nin place "
                                                                                 "the entire time.")

    def should_be_progress_bar(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_PROGRESS_BAR), "Progress bar is missing"

    # Molding complete
    def should_be_congratulations_title(self):
        assert self.is_element_present(*MoldingPageLocators.CONGRATULATIONS_TITLE), "No title"
        self.check_screen_title(*MoldingPageLocators.CONGRATULATIONS_TITLE, "Congratulations!")

    def should_be_congratulations_subtitle(self):
        assert self.is_element_present(*MoldingPageLocators.CONGRATULATIONS_SUBTITLE), "No subtitle"
        self.check_screen_subtitle(*MoldingPageLocators.CONGRATULATIONS_SUBTITLE,
                                   'You now have perfectly fitting earbuds.\n\nTake the tour '
                                   'to learn about the features\nof the app and how to make '
                                   'the most of\nyour UE FITS.')

    def should_be_congratulations_image(self):
        assert self.is_element_present(*MoldingPageLocators.CONGRATULATIONS_IMAGE), "No image on Congrats screen"

    def should_be_take_the_tour_button(self):
        assert self.is_element_present(*MoldingPageLocators.TAKE_TOUR_BUTTON), "Take tour button not found"

    def should_be_take_the_tour_button_text(self):
        self.check_button_text(*MoldingPageLocators.TAKE_TOUR_BUTTON, "Take the Tour")

    def tap_take_the_tour_button(self):
        self.click_element(*MoldingPageLocators.TAKE_TOUR_BUTTON)

    def should_skip_for_now_button(self):
        assert self.is_element_present(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON), "Skip for now button not found"

    def should_skip_for_now_button_text(self):
        self.check_button_text(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON, "Skip For Now")

    def tap_skip_for_now_button(self):
        self.click_element(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON)


class MoldNewTipsPage(MoldingPage):
    def should_be_close_button(self):
        self.is_element_present(*BasePageLocators.CLOSE_BUTTON), "Close button not found"

    def tap_close_button(self):
        self.click_element(*BasePageLocators.CLOSE_BUTTON)

    def should_be_scroll_dots(self):
        self.is_element_present(*MoldingPageLocators.SCROLL_ELEMENTS), "Scrolling dots do not appear"

    def should_be_next_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def should_be_next_button_text(self):
        expected_result = "Next"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_next_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def next_button_enabled(self):
        assert self.is_element_enabled(*BasePageLocators.BUTTON_MAIN), "Next button is not enabled, but it should"

    def next_button_not_enabled(self):
        assert not self.is_element_enabled(*BasePageLocators.BUTTON_MAIN), "Next button is enabled, but it shouldn't"

    def should_be_image_item(self):
        self.is_element_present(*MoldingPageLocators.IMAGE_VIEW), "Image / Animation not located"

    # Change your tips screen
    def should_be_change_tips_title(self):
        self.check_screen_title("Change Your Tips")

    def should_be_change_tips_subtitle(self):
        self.check_screen_subtitle("To remove your current tips, position one finger at the top of the tip and gently "
                                   "peel off.")

    # Remove inserts screen
    def should_be_remove_inserts_title(self):
        self.check_screen_title("Remove Inserts")

    def should_be_remove_inserts_subtitle(self):
        self.check_screen_subtitle("Remove the hard plastic inserts from your new tips by pulling on the insert tab.")

    # Match them up screen
    def should_be_match_them_up_title(self):
        self.check_screen_title("Match Them Up")

    def should_be_match_them_up_subtitle(self):
        self.check_screen_subtitle("Match the tips to the correct earbud. You’ll see an ‘R’ and ‘L’ on the inside of "
                                   "the tips.")

    # Attach your tips screen
    def should_be_attach_your_tips_title(self):
        self.check_screen_title("Attach Your Tips")

    def should_be_attach_your_tips_subtitle(self):
        self.check_screen_subtitle("Insert each earbud into the tip. You won't have to press too hard to attach them.")

    # Check the fit screen
    def should_be_check_the_fit_title(self):
        self.check_screen_title("Check The Fit")

    def should_be_check_the_fit_subtitle(self):
        self.check_screen_subtitle("Make sure the tips are flush with the earbuds.")
