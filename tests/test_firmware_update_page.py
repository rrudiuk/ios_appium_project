import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import HomeScreenUpdateDialogPage
from .pages.firmware_update_page import FirmwareUpdatePage
from .pages.home_page import HomePage
from .pages.menu_page import MenuPage
from .pages.support_page import SupportPage
from .pages.welcome_page import WelcomePage

import time


class TestFirmwareUpdatePage:
    def test_firmware_update(self, driver):
        analytics_page = AnalyticsPage(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        dialog_page = HomeScreenUpdateDialogPage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.tap_share_analytics_button()
        analytics_page.check_bt_dialog_presence_and_accept_it()
        time.sleep(10)
        dialog_page.check_and_close_fw_update_dialog()
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        # firmware_update_page.should_up_to_date_title()
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_update_available_title()
        firmware_update_page.tap_update_earbuds_button()
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()

    @pytest.mark.skip
    def test_firmware_update_no_installation(self, driver):
        firmware_update_page = FirmwareUpdatePage(driver)
        dialog_page = HomeScreenUpdateDialogPage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        time.sleep(10)
        dialog_page.check_and_close_fw_update_dialog()
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        # firmware_update_page.should_up_to_date_title()
        firmware_update_page.activate_fw_update()
        time.sleep(5)
        firmware_update_page.should_be_update_available_title()
        firmware_update_page.tap_update_earbuds_button()
        firmware_update_page.should_be_ready_to_update_title()
        firmware_update_page.tap_install_now_button()
        time.sleep(15)
        firmware_update_page.check_active_update()
