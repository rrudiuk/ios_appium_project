from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):
    def should_be_earbuds_name(self):
        self.is_element_present(*HomePageLocators.EARBUDS_NAME)

    def should_be_connected_state(self):
        expected_result = "Connected"
        actual_result = self.get_text(*HomePageLocators.EARBUDS_STATUS)
        assert actual_result == expected_result, f"State {actual_result} is shown, should be {expected_result}"

    def should_be_scanning_state(self):
        expected_result = "Scanning"
        actual_result = self.get_text(*HomePageLocators.EARBUDS_STATUS)
        assert actual_result == expected_result, f"State {actual_result} is shown, should be {expected_result}"

    def should_be_button_connect_earbuds(self):
        self.is_element_present(*HomePageLocators.CONNECT_EARBUDS_BUTTON), "Button doesn't appear"
        expected_result = "Connect Earbuds"
        actual_result = self.get_text(*HomePageLocators.CONNECT_EARBUDS_BUTTON)
        assert actual_result == expected_result, f"Text {actual_result} is shown, should be {expected_result}"

    def tap_button_connect_earbuds(self):
        self.click_element(*HomePageLocators.CONNECT_EARBUDS_BUTTON)

    def should_be_hamburger_menu(self):
        assert self.is_element_present(*HomePageLocators.HOME_SCREEN_LEFT_MENU), "Left menu doesn't appear on Home " \
                                                                                 "screen"

    def tap_hamburger_menu_icon(self):
        self.click_element(*HomePageLocators.HOME_SCREEN_LEFT_MENU)

    def should_be_settings_icon(self):
        assert self.is_element_present(*HomePageLocators.HOME_SCREEN_SETTINGS), "Settings icon doesn't appear"

    def tap_settings_icon(self):
        self.click_element(*HomePageLocators.HOME_SCREEN_SETTINGS)

    def should_be_left_earbud_image(self):
        assert self.is_element_present(*HomePageLocators.LEFT_EARBUD_IMAGE), "Left earbud image doesn't appear"

    def should_be_right_earbud_image(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_EARBUD_IMAGE), "Right earbud image doesn't appear"

    def should_be_case_image(self):
        assert self.is_element_present(*HomePageLocators.CASE_IMAGE), "Case image doesn't appear"

    def should_be_left_battery_image(self):
        assert self.is_element_present(*HomePageLocators.LEFT_BATTERY_IMAGE), "Left earbud battery image doesn't appear"

    def should_be_right_battery_image(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_BATTERY_IMAGE), "Right earbud battery image doesn't " \
                                                                               "appear"

    def should_be_case_battery_image(self):
        assert self.is_element_present(*HomePageLocators.CASE_BATTERY_IMAGE), "Case battery image doesn't appear"

    def should_be_left_battery_percents(self):
        assert self.is_element_present(*HomePageLocators.LEFT_BATTERY_PERCENTS), "Left earbud battery percentage " \
                                                                                 "doesn't appear"

    def should_be_right_battery_percents(self):
        assert self.is_element_present(*HomePageLocators.RIGHT_BATTERY_PERCENTS), "Right earbud battery percentage " \
                                                                                  "doesn't appear"

    def should_be_case_battery_percents(self):
        assert self.is_element_present(*HomePageLocators.CASE_BATTERY_PERCENTS), "Case battery percentage doesn't " \
                                                                                 "appear"
