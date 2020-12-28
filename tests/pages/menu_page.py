from .base_page import BasePage
from .locators import MenuPageLocators


class MenuPage(BasePage):
    def should_be_header(self):
        assert self.is_element_present(*MenuPageLocators.HEADER_CONTAINER), "Header is missing"

    def should_be_app_logo(self):
        assert self.is_element_present(*MenuPageLocators.APPLICATION_LOGO), "App logog is missing"

    def should_be_exit_x_button(self):
        assert self.is_element_present(*MenuPageLocators.CLOSE_ICON)

    def tap_exit_x_button(self):
        self.click_element(*MenuPageLocators.CLOSE_ICON)

    def should_be_home_item(self):
        expected_result = "Home"
        actual_result = self.get_text(*MenuPageLocators.HOME_ITEM)
        assert actual_result == expected_result, f"Item text {actual_result}, should be {expected_result}"

    def should_be_mold_new_tips_item(self):
        expected_result = "Mold New Tips"
        actual_result = self.get_text(*MenuPageLocators.MOLD_NEW_TIPS_ITEM)
        assert actual_result == expected_result, f"Item text {actual_result}, should be {expected_result}"

    def should_be_test_your_fit_item(self):
        expected_result = "Test Your Fit"
        actual_result = self.get_text(*MenuPageLocators.TEST_YOUR_FIT_ITEM)
        assert actual_result == expected_result, f"Item text {actual_result}, should be {expected_result}"

    def should_be_learn_more_item(self):
        expected_result = "Learn More"
        actual_result = self.get_text(*MenuPageLocators.LEARN_MORE_ITEM)
        assert actual_result == expected_result, f"Item text {actual_result}, should be {expected_result}"

    def should_be_support_item(self):
        expected_result = "Support"
        actual_result = self.get_text(*MenuPageLocators.SUPPORT_ITEM)
        assert actual_result == expected_result, f"Item text {actual_result}, should be {expected_result}"

    def tap_support_item(self):
        self.click_element(*MenuPageLocators.SUPPORT_ITEM)
