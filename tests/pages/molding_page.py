from .base_page import BasePage
from .locators import MoldingPageLocators


class MoldingPage(BasePage):
    # How to Pair
    def should_be_how_to_pair_title(self):
        self.check_screen_title(*MoldingPageLocators.HOW_TO_PAIR_TITLE, 'How to Pair')

    def should_be_how_to_pair_subtitle(self):
        self.check_screen_title(*MoldingPageLocators.HOW_TO_PAIR_SUBTITLE, 'Watch the video to learn how to pair '
                                                                           'your earbuds.')

    def should_be_how_to_pair_animation(self):
        assert self.is_element_present(*MoldingPageLocators.HOW_TO_PAIR_VIDEO), 'How to pair video animation not found'

    def should_be_got_it_button(self):
        self.check_button(*MoldingPageLocators.HOW_TO_PAIR_BUTTON, 'Got it!')

    def tap_got_it_button(self):
        self.click_element(*MoldingPageLocators.HOW_TO_PAIR_BUTTON)

    # Try them on screen
    def should_be_try_them_page_title(self):
        self.check_screen_title(*MoldingPageLocators.TRY_THEM_PAGE_TITLE, "Try Them On")

    def should_be_correct_try_them_page_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.TRY_THEM_PAGE_SUBTITLE,
                                   'Pop both earbuds into your ears. Gently adjust them until '
                                   'they feel comfortable and secure. You will mold both sides '
                                   'at the same time.')

    def should_be_try_them_animation(self):
        assert self.is_element_present(*MoldingPageLocators.TRY_THEM_PAGE_ANIMATION), "Animation doesn't appear on " \
                                                                                      "Try them on screen"

    def should_be_try_them_button(self):
        self.check_button(*MoldingPageLocators.TRY_THEM_PAGE_BUTTON, "Next")

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
        self.check_message(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG1, "We???ll do a quick sound test to ensure "
                                                                        "a sound-isolating fit before we mold.")

    def should_be_message2(self):
        self.check_message(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG2, "We???ll share some quick tips for achieving "
                                                                        "the best mold.")

    def should_be_message3(self):
        self.check_message(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG3, "The 60 second molding magic starts.")

    def should_be_smile(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_SMILE_IMAGE), "No smile icon on Get Ready screen"

    def should_be_stand_by_mirror_text(self):
        self.check_message(*MoldingPageLocators.MOLDING_STAND_BY_MIRROR, "Try standing in front of a mirror for "
                                                                         "this part")

    def should_be_do_this_button(self):
        self.check_button(*MoldingPageLocators.GET_READY_BUTTON, "Let???s Do This")

    def tap_do_this_button(self):
        self.click_element(*MoldingPageLocators.GET_READY_BUTTON)

    # How is the bass
    def should_be_how_is_bass_title(self):
        self.check_screen_title(*MoldingPageLocators.HOW_IS_THE_BASS_TITLE, "How???s the Bass?")

    def should_be_correct_how_is_bass_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.HOW_IS_THE_BASS_SUBTITLE,
                                   'Gently adjust both earbuds until you find the position that maximizes the bass. ')

    def should_be_cancel_button(self):
        self.check_button(*MoldingPageLocators.MOLDING_CANCEL_BUTTON, "Cancel")

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
        self.check_screen_subtitle(*MoldingPageLocators.MOLDING_START_SUBTITLE2, "Gently hold your earbuds\nin"
                                                                                 " place the entire time.")

    def should_be_progress_bar(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_PROGRESS_BAR), "Progress bar is missing"

    # Molding complete
    def should_be_congratulations_title(self):
        assert self.is_element_present(*MoldingPageLocators.CONGRATULATIONS_TITLE), "No title"
        self.check_screen_title(*MoldingPageLocators.CONGRATULATIONS_TITLE, "Congratulations")

    def should_be_congratulations_subtitle(self):
        assert self.is_element_present(*MoldingPageLocators.CONGRATULATIONS_SUBTITLE), "No subtitle"
        self.check_screen_subtitle(*MoldingPageLocators.CONGRATULATIONS_SUBTITLE,
                                   'You now have perfectly fitting earbuds.\n\nTake the tour '
                                   'to learn about the features of the app and how to make '
                                   'the most of your UE FITS.')

    def should_be_congratulations_image(self):
        assert self.is_element_present(*MoldingPageLocators.CONGRATULATIONS_IMAGE), "No image on Congrats screen"

    def should_be_take_the_tour_button(self):
        self.check_button(*MoldingPageLocators.TAKE_TOUR_BUTTON, "Take the Tour")

    def tap_take_the_tour_button(self):
        self.click_element(*MoldingPageLocators.TAKE_TOUR_BUTTON)

    def should_skip_for_now_button(self):
        self.check_button(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON, "Skip For Now")

    def tap_skip_for_now_button(self):
        self.click_element(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON)


class MoldNewTipsPage(MoldingPage):
    def should_be_mnt_menu_icon(self):
        assert self.is_element_present(*MoldingPageLocators.MENU_ICON), "Menu icon not found"

    def tap_mnt_menu_icon(self):
        self.click_element(*MoldingPageLocators.MENU_ICON)

    def should_be_scroll_dots(self):
        self.is_element_present(*MoldingPageLocators.SCROLL_ELEMENTS), "Scrolling dots do not appear"

    def should_be_next_button(self):
        self.check_button(*MoldingPageLocators.NEXT_BUTTON, 'Next')

    def tap_next_button(self):
        self.click_element(*MoldingPageLocators.NEXT_BUTTON)

    def next_button_enabled(self):
        assert self.is_element_enabled(*MoldingPageLocators.NEXT_BUTTON), "Next button is not enabled, but it should"

    def next_button_not_enabled(self):
        assert not self.is_element_enabled(*MoldingPageLocators.NEXT_BUTTON), "Next button is enabled, but it shouldn't"

    # Change your tips screen
    def should_be_change_tips_title(self):
        self.check_screen_title(*MoldingPageLocators.CHANGE_YOUR_TIPS_TITLE, "Change Your Tips")

    def should_be_change_tips_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.CHANGE_YOUR_TIPS_SUBTITLE,
                                   'To remove your current tips, position one finger at the top of the tip '
                                   'and gently peel off.')

    def should_be_change_tips_animation(self):
        self.is_element_present(*MoldingPageLocators.CHANGE_YOUR_TIPS_ANIMATION), "Image / Animation not located"

    # Remove inserts screen
    def should_be_remove_inserts_title(self):
        self.check_screen_title(*MoldingPageLocators.REMOVE_INSERTS_TITLE, "Remove Inserts")

    def should_be_remove_inserts_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.REMOVE_INSERTS_SUBTITLE, 'Remove the hard plastic inserts '
                                                                                 'from your new tips by pulling on '
                                                                                 'the insert tab.')

    def should_be_remove_inserts_image(self):
        assert self.is_element_present(*MoldingPageLocators.REMOVE_INSERTS_IMAGE), 'Remove inserts image not found'

    # Match them up screen
    def should_be_match_them_up_title(self):
        self.check_screen_title(*MoldingPageLocators.MATCH_THEM_UP_TITLE, "Match Them Up")

    def should_be_match_them_up_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.MATCH_THEM_UP_SUBTITLE,
                                   'Match the tips to the correct earbud. You???ll see an ???R??? and ???L??? on the '
                                   'inside of the tips.')

    def should_be_match_them_image(self):
        assert self.is_element_present(*MoldingPageLocators.MATCH_THEM_UP_IMAGE), 'Match them image not found'

    # Attach your tips screen
    def should_be_attach_your_tips_title(self):
        self.check_screen_title(*MoldingPageLocators.ATTACH_YOUR_TIPS_TITLE, "Attach Your Tips")

    def should_be_attach_your_tips_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.ATTACH_YOUR_TIPS_SUBTITLE,
                                   'Insert each earbud into the tip.\nYou won???t have to press '
                                   'too hard to attach them.')

    def should_be_attach_tips_image(self):
        assert self.is_element_present(*MoldingPageLocators.ATTACH_YOUR_TIPS_IMAGE), 'Attach tips image not found'

    # Check the fit screen
    def should_be_check_the_fit_title(self):
        self.check_screen_title(*MoldingPageLocators.CHECK_THE_FIT_TITLE, "Check The Fit")

    def should_be_check_the_fit_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.CHECK_THE_FIT_SUBTITLE, 'Make sure the tips are flush with '
                                                                                'the earbuds.')

    def should_be_check_the_fit_image(self):
        assert self.is_element_present(*MoldingPageLocators.CHECK_THE_FIT_IMAGE), 'Check the fit image not found'

    # Congratulations
    def should_be_congratulations_subtitle(self):
        self.check_screen_subtitle(*MoldingPageLocators.CONGRATULATIONS_SUBTITLE_FINISH,
                                   'You now have perfectly fitting earbuds. Throw on your favorite song and '
                                   'take them for a spin.')

    def should_be_finish_button(self):
        self.check_button(*MoldingPageLocators.FINISH_BUTTON, 'Finish')

    def tap_finish_button(self):
        self.click_element(*MoldingPageLocators.FINISH_BUTTON)
