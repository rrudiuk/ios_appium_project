from .base_page import BasePage
from .locators import FirmwareUpdatePageLocators

from ..utilities import logger

import time


class FirmwareUpdatePage(BasePage):
    def activate_fw_update(self):
        tries = 10
        while tries > 0:
            title = self.get_text(*FirmwareUpdatePageLocators.FW_ACTIVATION_TITLE)
            if title == 'Up to Date':
                logger.LOGGER.info("Start fw update activation")
                self.two_finger_tap_element_10_times(*FirmwareUpdatePageLocators.FW_ACTIVATION_TITLE)
                tries = tries - 1
                time.sleep(3)
            elif title == 'Update Available':
                logger.LOGGER.info("Update activated")
                break
            else:
                logger.LOGGER.error("Update activation error")
                break

    def tap_page_title_10_times(self):
        self.click_element_10_times(*FirmwareUpdatePageLocators.TITLE_WRAPPER)

    def should_up_to_date_title(self):
        self.check_screen_title(*FirmwareUpdatePageLocators.FW_ACTIVATION_TITLE, 'Up to Date')

    def should_be_update_available_title(self):
        self.check_screen_title(*FirmwareUpdatePageLocators.FW_ACTIVATION_TITLE, 'Update Available')

    def should_be_ready_to_update_title(self):
        self.check_screen_title(*FirmwareUpdatePageLocators.READY_TO_UPDATE_TITLE, 'Ready to Update')

    def tap_update_earbuds_button(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.UPDATE_EARBUDS_BUTTON), "Update earbuds button " \
                                                                                           "not found"
        self.click_element(*FirmwareUpdatePageLocators.UPDATE_EARBUDS_BUTTON)

    def tap_install_now_button(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.INSTALL_NOW_BUTTON), "Install now button not found"
        self.click_element(*FirmwareUpdatePageLocators.INSTALL_NOW_BUTTON)
        logger.LOGGER.info("FW update started")

    def check_active_update(self):
        tries = 45
        duration = 0
        check_period = 20
        installing_title = "Installing"
        error_occurred_title = "An Error Occurred"
        while tries > 0:
            if self.get_text(*FirmwareUpdatePageLocators.FW_UPDATE_TITLE) == installing_title:
                tries = tries - 1
                time.sleep(check_period)
                duration = duration + check_period
            else:
                logger.LOGGER.info("Exit installing screen")
                break

        if self.locate_element(*FirmwareUpdatePageLocators.RECONNECTING_DIALOG_TITLE):
            logger.LOGGER.error("Earbuds disconnected. Reconnecting is shown")
        elif self.get_text(*FirmwareUpdatePageLocators.FW_UPDATE_TITLE) == error_occurred_title:
            checks = 3
            logger.LOGGER.info("Error occurred. Checking...")
            while checks > 0:
                logger.LOGGER.info(f"Checks left: {checks}")
                self.two_finger_tap_element_10_times(*FirmwareUpdatePageLocators.FW_UPDATE_TITLE)
                if self.locate_element(*FirmwareUpdatePageLocators.ERROR_DIALOG_TITLE):
                    logger.LOGGER.error(self.get_text(*FirmwareUpdatePageLocators.ERROR_MESSAGE_TEXT))
                    break
                checks = checks - 1

        if self.get_text(*FirmwareUpdatePageLocators.FW_UPDATE_TITLE) == "Restarting":
            logger.LOGGER.info("Restarting")
            time.sleep(30)
            duration = duration + 30

        logger.LOGGER.info(f"FW update duration: {duration}")

        self.take_screenshot()
        logger.LOGGER.info("Screenshot captured")

        assert self.locate_element(*FirmwareUpdatePageLocators.YOU_ARE_ALL_SET_TITLE), "Update failed"
