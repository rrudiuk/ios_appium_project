from .base_page import BasePage
from .locators import UGCPageLocators


class UGCPage(BasePage):
    def should_be_ugc_title(self):
        self.check_screen_title(*UGCPageLocators.TAKE_SELFIE_TITLE, "You Did It!")

    def should_be_ugc_title_menu(self):
        self.check_screen_title(*UGCPageLocators.TAKE_SELFIE_TITLE_MENU, "Take a Selfie")

    def should_be_correct_ugc_subtitle(self):
        self.check_screen_subtitle(*UGCPageLocators.TAKE_SELFIE_SUBTITLE, "Check out the Lightform technology up "
                                                                          "close and capture the experience to save "
                                                                          "and share.")

    def should_be_take_selfie_button_text(self):
        expected_result = "Take a Selfie"
        actual_result = self.get_text(*UGCPageLocators.TAKE_SELFIE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    def tap_take_selfie_button(self):
        self.click_element(*UGCPageLocators.TAKE_SELFIE_BUTTON)

    def should_be_skip_button_text(self):
        expected_result = "Skip For Now"
        actual_result = self.get_text(*UGCPageLocators.SKIP_FOR_NOW_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', " \
                                                 f"should be '{expected_result}'"

    def tap_skip_button(self):
        self.click_element(*UGCPageLocators.SKIP_FOR_NOW_BUTTON)

    def should_be_collage(self):
        self.is_element_present(*UGCPageLocators.IMAGE_COLLAGE), "Collage not found on UGC screen"

    def should_be_ugc_gif(self):
        self.is_element_present(*UGCPageLocators.UGC_GIF), "Gif not found on UGC screen"
