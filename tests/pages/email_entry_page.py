from .base_page import BasePage
from .locators import EmailEntryPageLocators


class EmailEntryPage(BasePage):
    def should_be_email_entry_title(self):
        self.check_screen_title(*EmailEntryPageLocators.EMAIL_ENTRY_TITLE, "Never Miss A Beat")

    def should_be_correct_email_entry_subtitle(self):
        self.check_screen_subtitle(*EmailEntryPageLocators.EMAIL_ENTRY_SUBTITLE, "Stay up to date on firmware "
                                                                                 "updates, giveaways, beta testing "
                                                                                 "opportunities, and more.")

    def should_be_correct_sign_me_button(self):
        self.check_button(*EmailEntryPageLocators.SIGN_ME_BUTTON, "Sign Me Up")

    def tap_sign_me_button(self):
        self.click_element(*EmailEntryPageLocators.SIGN_ME_BUTTON)

    def should_be_correct_no_thanks_button(self):
        self.check_button(*EmailEntryPageLocators.NO_THANKS_BUTTON, "No Thanks")

    def tap_no_thanks_button(self):
        self.click_element(*EmailEntryPageLocators.NO_THANKS_BUTTON)

    def should_be_reason_description(self):
        self.check_message(*EmailEntryPageLocators.EMAIL_ENTRY_REASON_DESCRIPTION, "This can be changed from the Main "
                                                                                   "Menu under Support. Learn more "
                                                                                   "about our Privacy Policy.")

    def should_be_email_entry_input(self):
        self.is_element_present(*EmailEntryPageLocators.EMAIL_ENTRY_INPUT), "Email entry input not found"
