import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.email_entry_page import EmailEntryPage
from .pages.home_page import HomePage
from .pages.dialogs_page import HomeScreenUpdateDialogPage
from .pages.menu_page import MenuPage
from .pages.user_guide_page import UserGuidePage
from .pages.welcome_page import WelcomePage


def initial_setup_non_molding(driver):
    analytics_page = AnalyticsPage(driver)
    email_entry_page = EmailEntryPage(driver)
    dialog_page = HomeScreenUpdateDialogPage(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.should_be_correct_welcome_title()
    welcome_page.tap_welcome_screen_get_started()
    email_entry_page.should_be_email_entry_title()
    email_entry_page.should_be_correct_email_entry_subtitle()
    email_entry_page.tap_no_thanks_button()
    analytics_page.tap_share_analytics_button()
    analytics_page.check_bt_dialog_presence_and_accept_it()
    dialog_page.wait_for_connection()
    dialog_page.check_and_close_fw_update_dialog()


class TestMenuPage:
    def test_all_user_guide_items_appear(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_pairing_item()
        user_guide_page.should_be_molding_item()
        user_guide_page.should_be_controls_item()
        user_guide_page.should_be_connectivity_and_switching_item()
        user_guide_page.should_be_charging_item()
        user_guide_page.should_be_adjusting_eq_item()
        user_guide_page.should_be_tyf_item()
        user_guide_page.should_be_updating_fw_item()
        user_guide_page.should_be_troubleshooting_item()

    def test_user_guide_pairing_ohboy(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_pairing_item()
        user_guide_page.tap_pairing_item()
        user_guide_page.should_be_pairing_ohboy_screen()

    @pytest.mark.test
    def test_user_guide_pairing_sebulba(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_pairing_item()
        user_guide_page.tap_pairing_item()
        user_guide_page.should_be_pairing_sebulba_screen()

    def test_user_guide_molding(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_molding_item()
        user_guide_page.tap_molding_item()
        user_guide_page.should_be_molding_screen()

    def test_user_guide_controls(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_controls_item()
        user_guide_page.tap_controls_item()
        user_guide_page.should_be_controls_screen()

    def test_user_guide_connectivity_and_switching_ohboy(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_connectivity_and_switching_item()
        user_guide_page.tap_connectivity_and_switching_item()
        user_guide_page.should_be_connectivity_and_switching_ohboy_screen()

    @pytest.mark.test
    def test_user_guide_connectivity_and_switching_sebulba(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_connectivity_and_switching_item()
        user_guide_page.tap_connectivity_and_switching_item()
        user_guide_page.should_be_connectivity_and_switching_sebulba_screen()

    def test_user_guide_charging(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_charging_item()
        user_guide_page.tap_charging_item()
        user_guide_page.should_be_charging_screen()

    def test_user_guide_adjusting_eq(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_adjusting_eq_item()
        user_guide_page.tap_adjusting_eq_item()
        user_guide_page.should_be_adjusting_eq_screen()

    def test_user_guide_tyf(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_tyf_item()
        user_guide_page.tap_tyf_item()
        user_guide_page.should_be_tyf_screen()

    def test_user_guide_updating_fw(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_updating_fw_item()
        user_guide_page.tap_updating_fw_item()
        user_guide_page.should_be_updating_fw_screen()

    def test_user_guide_troubleshooting(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        user_guide_page = UserGuidePage(driver)
        home_page.should_be_hamburger_menu()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_user_guide_item()
        menu_page.tap_user_guide_item()
        user_guide_page.should_be_troubleshooting_item()
        user_guide_page.tap_troubleshooting_item()
        user_guide_page.should_be_troubleshooting_screen()
