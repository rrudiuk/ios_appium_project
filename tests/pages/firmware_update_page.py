from .base_page import BasePage
from .locators import FirmwareUpdatePageLocators

import time


class FirmwareUpdatePage(BasePage):
    def activate_fw_update(self):
        # self.two_finger_tap_element_10_times(*FirmwareUpdatePageLocators.UP_TO_DATE_TITLE)
        tries = 10
        while tries > 0:
            if self.locate_element(*FirmwareUpdatePageLocators.UP_TO_DATE_TITLE):
                print("Start fw update activation")
                self.two_finger_tap_element_10_times(*FirmwareUpdatePageLocators.UP_TO_DATE_TITLE)
                tries = tries - 1
                time.sleep(3)
            else:
                print("Quit fw update activation")
                break

    def tap_page_title_10_times(self):
        self.click_element_10_times(*FirmwareUpdatePageLocators.TITLE_WRAPPER)

    def should_up_to_date_title(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.UP_TO_DATE_TITLE), "No"

    def is_update_available_title(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.UPDATE_AVAILABLE_TITLE), "Update available screen " \
                                                                                            "is not shown"

    def is_ready_to_update_title(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.READY_TO_UPDATE_TITLE), "Ready to update screen " \
                                                                                           "is not shown"

    def is_installing_title(self):
        self.locate_element(*FirmwareUpdatePageLocators.INSTALLING_TITLE)

    def is_an_error_occurred_title(self):
        self.locate_element(*FirmwareUpdatePageLocators.AN_ERROR_OCCURRED_TITLE)

    def is_restarting_title(self):
        self.locate_element(*FirmwareUpdatePageLocators.RESTARTING_TITLE)

    def is_all_set_title(self):
        self.locate_element(*FirmwareUpdatePageLocators.YOU_ARE_ALL_SET_TITLE)

    def tap_update_earbuds_button(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.UPDATE_EARBUDS_BUTTON), "Update earbuds button " \
                                                                                           "not found"
        self.click_element(*FirmwareUpdatePageLocators.UPDATE_EARBUDS_BUTTON)

    def tap_install_now_button(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.INSTALL_NOW_BUTTON), "Install now button not found"
        self.click_element(*FirmwareUpdatePageLocators.INSTALL_NOW_BUTTON)

    def check_active_update(self):
        tries = 45
        duration = 0
        check_period = 20
        while tries > 0:
            if self.locate_element(*FirmwareUpdatePageLocators.INSTALLING_TITLE):
                tries = tries - 1
                time.sleep(check_period)
                duration = duration + check_period
            else:
                break

        if self.locate_element(*FirmwareUpdatePageLocators.RECONNECTING_DIALOG_TITLE):
            print("Earbuds disconnected. Reconnecting is shown")
            ts = time.strftime("%Y_%m_%d_%H%M%S")
            self.driver.save_screenshot("/Users/rudiuk/PyCharmProjects/ios_appium_project/Screenshots/"
                                        + ts + ".png")
        elif self.locate_element(*FirmwareUpdatePageLocators.AN_ERROR_OCCURRED_TITLE):
            checks = 3
            print("Error occurred. Checking...")
            while checks > 0:
                print(f"Check {checks}")
                self.two_finger_tap_element_10_times(*FirmwareUpdatePageLocators.AN_ERROR_OCCURRED_TITLE)
                if self.locate_element(*FirmwareUpdatePageLocators.ERROR_DIALOG_TITLE):
                    ts = time.strftime("%Y_%m_%d_%H%M%S")
                    self.driver.save_screenshot("/Users/rudiuk/PyCharmProjects/ios_appium_project/Screenshots/"
                                                + ts + ".png")
                    # screenshotBase64 = self.driver.get_screenshot_as_base64()
                    # self.driver.push_file('/path/to/device/foo.bar', screenshotBase64)
                    # print(self.get_text(*FirmwareUpdatePageLocators.ERROR_MESSAGE_TEXT))
                    break
                checks = checks - 1

        if self.locate_element(*FirmwareUpdatePageLocators.RESTARTING_TITLE):
            time.sleep(30)
            duration = duration + 30

        print(duration)

        assert self.locate_element(*FirmwareUpdatePageLocators.UPDATE_BUTTON) or \
               self.locate_element(*FirmwareUpdatePageLocators.RESTARTING_TITLE), "Update failed"
