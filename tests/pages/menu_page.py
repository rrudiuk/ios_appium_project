from .base_page import BasePage
from .locators import MenuPageLocators


class MenuPage(BasePage):
    def should_be_header(self):
        assert self.is_element_present(*MenuPageLocators.HEADER_CONTAINER), "Header is missing"

    def should_be_app_logo(self):
        assert self.is_element_present(*MenuPageLocators.APPLICATION_LOGO), "App logo is missing"

    def should_be_exit_x_button(self):
        assert self.is_element_present(*MenuPageLocators.CLOSE_ICON), "No exit button in Menu"

    def tap_exit_x_button(self):
        self.click_element(*MenuPageLocators.CLOSE_ICON)

    # Email Entry
    def should_be_email_entry_item(self):
        self.check_button(*MenuPageLocators.EMAIL_ENTRY_ITEM, "Email Entry")

    def tap_email_entry_item(self):
        self.click_element(*MenuPageLocators.EMAIL_ENTRY_ITEM)

    # Home
    def should_be_home_item(self):
        self.check_button(*MenuPageLocators.HOME_ITEM, "Home")

    def tap_home_item(self):
        self.click_element(*MenuPageLocators.HOME_ITEM)

    # Mold new tips
    def should_be_mold_new_tips_item(self):
        self.check_button(*MenuPageLocators.MOLD_NEW_TIPS_ITEM, "Mold New Tips")

    def tap_mold_new_tips_item(self):
        self.click_element(*MenuPageLocators.MOLD_NEW_TIPS_ITEM)

    # Test your fit
    def should_be_test_your_fit_item(self):
        self.check_button(*MenuPageLocators.TEST_YOUR_FIT_ITEM, "Test Your Fit")

    def tap_test_your_fit_item(self):
        self.click_element(*MenuPageLocators.TEST_YOUR_FIT_ITEM)

    # Learn more (outdated)
    def should_be_learn_more_item(self):
        self.check_button(*MenuPageLocators.LEARN_MORE_ITEM, "Learn More")

    def tap_learn_more_item(self):
        self.click_element(*MenuPageLocators.LEARN_MORE_ITEM)

    # Support
    def should_be_support_item(self):
        self.check_message(*MenuPageLocators.SUPPORT_ITEM, "Support")

    def tap_support_item(self):
        self.click_element(*MenuPageLocators.SUPPORT_ITEM)

    # Take a Selfie
    def should_be_take_selfie_item(self):
        self.check_button(*MenuPageLocators.TAKE_SELFIE_ITEM, "Take a Selfie")

    def tap_take_selfie_item(self):
        self.click_element(*MenuPageLocators.TAKE_SELFIE_ITEM)

    # User guide
    def should_be_user_guide_item(self):
        self.check_button(*MenuPageLocators.USER_GUIDE_ITEM, "User Guide")

    def tap_user_guide_item(self):
        self.click_element(*MenuPageLocators.USER_GUIDE_ITEM)
