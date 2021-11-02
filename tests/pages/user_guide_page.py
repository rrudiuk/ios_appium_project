from .base_page import BasePage
from .locators import UserGuidePageLocators


class UserGuidePage(BasePage):
    def should_be_back_arrow(self):
        self.is_element_present(*UserGuidePageLocators.USER_GUIDE_SCREEN_BACK_ARROW), "Back arrow not located"

    # Pairing
    def should_be_pairing_item(self):
        assert self.is_element_present(*UserGuidePageLocators.PAIRING_ARROW), "Pairing arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.PAIRING_DIVIDER), "Pairing divider not found"
        self.check_button(*UserGuidePageLocators.PAIRING_ITEM, "Pairing")

    def tap_pairing_item(self):
        self.click_element(*UserGuidePageLocators.PAIRING_ITEM)

    def should_be_pairing_ohboy_screen(self):
        self.check_screen_title(*UserGuidePageLocators.PAIRING_SCREEN_TITLE, "Pairing")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.PAIRING_TEXT1, 'To pair a new device, place the earbuds in the '
                                                                 'case with the lid open.')
        self.check_message(*UserGuidePageLocators.PAIRING_TEXT2, 'Press and hold the upper right button inside the '
                                                                 'case until the earbuds flash white—approximately'
                                                                 ' three seconds—then release the button.')
        assert self.is_element_present(*UserGuidePageLocators.PAIRING_CASE_IMAGE), "Case image not found"
        self.check_message(*UserGuidePageLocators.OHBOY_PAIRING_WATCH_VIDEO, 'Watch the video to learn how to pair '
                                                                             'your earbuds.')
        assert self.is_element_present(*UserGuidePageLocators.OHBOY_PAIRING_VIDEO), "Ohboy pairing video not found"
        self.swipe_up()
        self.check_message(*UserGuidePageLocators.OHBOY_PAIRING_ONE_NOT_CONNECTED, 'After pairing, one of the earbuds'
                                                                                   ' will be listed as Not Connected.'
                                                                                   ' This is normal.')

    def should_be_pairing_sebulba_screen(self):
        self.check_screen_title(*UserGuidePageLocators.PAIRING_SCREEN_TITLE, "Pairing")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.PAIRING_TEXT1, 'To pair a new device, place the earbuds in the '
                                                                 'case with the lid open.')
        self.check_message(*UserGuidePageLocators.PAIRING_TEXT2, 'Press and hold the upper right button inside the '
                                                                 'case until the earbuds flash white—approximately'
                                                                 ' three seconds—then release the button.')
        assert self.is_element_present(*UserGuidePageLocators.PAIRING_CASE_IMAGE), "Case image not found"
        self.swipe_up()
        self.check_message(*UserGuidePageLocators.SEBULBA_PAIRING_SELECT_UE_FITS, 'In your Bluetooth settings, select'
                                                                                  ' UE FITS to begin pairing.')
        assert self.is_element_present(*UserGuidePageLocators.SEBULBA_PAIRING_IMAGE), "Sebulba pairing image not found"

    # Molding
    def should_be_molding_item(self):
        assert self.is_element_present(*UserGuidePageLocators.MOLDING_ARROW), "Molding arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.MOLDING_DIVIDER), "Molding divider not found"
        self.check_button(*UserGuidePageLocators.MOLDING_ITEM, "Molding")

    def tap_molding_item(self):
        self.click_element(*UserGuidePageLocators.MOLDING_ITEM)

    def should_be_molding_screen(self):
        self.check_screen_title(*UserGuidePageLocators.MOLDING_SCREEN_TITLE, "Molding")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.MOLDING_A_FEW_THINGS, "A few things to know before molding your new"
                                                                        " ear tips.")
        self.check_message(*UserGuidePageLocators.MOLDING_SOUND_TEST, "Sound Test page")
        self.check_message(*UserGuidePageLocators.MOLDING_ADJUST_BOTH_EARBUDS, "Adjust both earbuds until you find "
                                                                               "the position that maximizes the bass.")
        self.check_message(*UserGuidePageLocators.MOLDING_APPLY_GENTLE_PRESSURE,
                           "Apply gentle pressure to both earbuds—just enough to get a good seal with the ear tip—and"
                           " maintain that pressure throughout the entire molding process.")
        self.check_message(*UserGuidePageLocators.MOLDING_AFTER_SOUND_TEST, "After the sound test, the app will show"
                                                                            " a short countdown and automatically "
                                                                            "start molding your tips.")
        self.check_message(*UserGuidePageLocators.MOLDING_MIX_AMD_MATCH, "Mix and match tips")
        self.check_message(*UserGuidePageLocators.MOLDING_SEVERAL_PAIRS,
                           "If you have several pairs of tips, feel free to mix and match the left and right tips"
                           " between sets to get the best fit for each ear.")
        self.check_message(*UserGuidePageLocators.MOLDING_CLICK_ON_APP_MENU, "Click on the app menu and select "
                                                                             "“Mold New Tips” to start molding your"
                                                                             " new tips.")

    # Controls
    def should_be_controls_item(self):
        assert self.is_element_present(*UserGuidePageLocators.CONTROLS_ARROW), "Controls arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.CONTROLS_DIVIDER), "Controls divider not found"
        self.check_button(*UserGuidePageLocators.CONTROLS_ITEM, "Controls")

    def tap_controls_item(self):
        self.click_element(*UserGuidePageLocators.CONTROLS_ITEM)

    def should_be_controls_screen(self):
        self.check_screen_title(*UserGuidePageLocators.CONTROLS_SCREEN_TITLE, "Controls")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.CONTROLS_DOUBLE_AND_SINGLE, 'Double and Single Tap Control')
        self.check_message(*UserGuidePageLocators.CONTROLS_EACH_FITS_EARBUD, 'Each FITS earbud has a double-tap control'
                                                                             ' that defaults to play/pause on both left'
                                                                             ' and right earbuds.')
        self.check_message(*UserGuidePageLocators.CONTROLS_PHONE_CALL, 'When a phone call is active, double-tap to '
                                                                       'accept or end the call.')
        self.check_message(*UserGuidePageLocators.CONTROLS_ENABLE_SINGLE_TAP, 'Enable single tap for even more control'
                                                                              ' options.')
        self.check_message(*UserGuidePageLocators.CONTROLS_TO_USE, 'To use the controls, tap directly on the '
                                                                   'earbud body.')
        assert self.is_element_present(*UserGuidePageLocators.CONTROLS_HOW_TO_USE_IMAGE), "How to use image not found"
        self.check_message(*UserGuidePageLocators.CONTROLS_CUSTOMIZATION, 'Control Customization')
        self.check_message(*UserGuidePageLocators.CONTROLS_EACH_EARBUD, 'Each earbud can be customized separately in '
                                                                        'the Settings menu.')
        assert self.is_element_present(*UserGuidePageLocators.CONTROLS_ACCESS_SETTINGS), 'How to access settings ' \
                                                                                         'image not found'

    # Connectivity and Switching Devices
    def should_be_connectivity_and_switching_item(self):
        assert self.is_element_present(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_ARROW), \
            "Connectivity and Switching Devices arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_DIVIDER), \
            "Connectivity and Switching Devices divider not found"
        self.check_button(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_ITEM, "Connectivity and Switching Devices")

    def tap_connectivity_and_switching_item(self):
        self.click_element(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_ITEM)

    def should_be_connectivity_and_switching_ohboy_screen(self):
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TITLE, "Switching Between Paired Devices")
        assert self.is_element_present(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_IMAGE), "Connectivity and " \
                                                                                                 "Switching image not" \
                                                                                                 " found "
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_FIRST_ENSURE,
                           "First, ensure you have the latest firmware. See the “Update your Firmware” section of the "
                           "user guide for more information.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_YOU_CAN_SWITCH_OHBOY,
                           "You can switch between multiple paired devices by selecting UE FITS L or UE FITS R in the "
                           "Bluetooth settings menu of the device you wish to connect to. In some cases, you may have "
                           "to select UE FITS a second time in order to complete the connection.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_CASE_INTERACTIONS, "Case Connectivity"
                                                                                                " Interactions")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_IN_CASE,
                           "When the earbuds are in the case, opening the case will auto-connect them to the last "
                           "paired device.")
        self.swipe_up()
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_AUTO_CONNECTION,
                           "Auto-connect may not occur if the case battery is empty. In this case, double tap the "
                           "earbuds to wake them from standby. It may take a few seconds for the earbuds to reconnect "
                           "after manually waking them from standby mode.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_USING_SINGLE_EARBUD,
                           "Using a single earbud for communication")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TO_USE_SINGLE,
                           "To use a single earbud for communication, place the earbud you are not using in the case. "
                           "This ensures that the mics on the earbud you are wearing are activated.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_STANDBY, "Standby")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_AFTER_60,
                           "After 60 minutes with no audio streaming, your earbuds will automatically go into standby"
                           " mode. A tone can be heard when the earbuds go into standby.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TO_WAKE,
                           "To wake your earbuds up from Standby mode, either take them in and out of the charged "
                           "case or double tap the earbuds. It may take a few seconds for the earbuds to power on and "
                           "reconnect after waking from standby.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TO_APP, "Connecting to the app")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_WILL_CONNECT,
                           "UE FITS will connect to the app when they are in the case with the lid open or they are "
                           "out of the case completely.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_SECOND_DEVICE,
                           "You may be connected to a second device and still use the app on the primary device. For "
                           "example, you can use your phone app to control the earbud EQ and settings even if you’re "
                           "currently connected to your computer.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_APP_WILL_DISPLAY,
                           "The app will display the currently connected device name on the home screen.")

    def should_be_connectivity_and_switching_sebulba_screen(self):
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TITLE, "Switching Between Paired Devices")
        assert self.is_element_present(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_IMAGE), \
            "Connectivity and Switching image not found "
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_FIRST_ENSURE,
                           "First, ensure you have the latest firmware. See the “Update your Firmware” section of the "
                           "user guide for more information.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_YOU_CAN_SWITCH_SEBULBA,
                           "You can switch between multiple paired devices by selecting UE FITS in the Bluetooth "
                           "settings menu of the device you wish to connect to. In some cases, you may have to select "
                           "UE FITS a second time in order to complete the connection")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_CASE_INTERACTIONS, "Case Connectivity"
                                                                                                " Interactions")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_IN_CASE,
                           "When the earbuds are in the case, opening the case will auto-connect them to the last "
                           "paired device.")
        self.swipe_up()
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_AUTO_CONNECTION,
                           "Auto-connect may not occur if the case battery is empty. In this case, double tap the "
                           "earbuds to wake them from standby. It may take a few seconds for the earbuds to reconnect "
                           "after manually waking them from standby mode.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_USING_SINGLE_EARBUD,
                           "Using a single earbud for communication")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TO_USE_SINGLE,
                           "To use a single earbud for communication, place the earbud you are not using in the case. "
                           "This ensures that the mics on the earbud you are wearing are activated.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_STANDBY, "Standby")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_AFTER_60,
                           "After 60 minutes with no audio streaming, your earbuds will automatically go into standby"
                           " mode. A tone can be heard when the earbuds go into standby.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TO_WAKE,
                           "To wake your earbuds up from Standby mode, either take them in and out of the charged "
                           "case or double tap the earbuds. It may take a few seconds for the earbuds to power on and "
                           "reconnect after waking from standby.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_TO_APP, "Connecting to the app")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_WILL_CONNECT,
                           "UE FITS will connect to the app when they are in the case with the lid open or they are "
                           "out of the case completely.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_SECOND_DEVICE,
                           "You may be connected to a second device and still use the app on the primary device. For "
                           "example, you can use your phone app to control the earbud EQ and settings even if you’re "
                           "currently connected to your computer.")
        self.check_message(*UserGuidePageLocators.CONNECTIVITY_AND_SWITCHING_APP_WILL_DISPLAY,
                           "The app will display the currently connected device name on the home screen.")

    # Charging
    def should_be_charging_item(self):
        assert self.is_element_present(*UserGuidePageLocators.CHARGING_ARROW), "Charging arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.CHARGING_DIVIDER), "Charging divider not found"
        self.check_button(*UserGuidePageLocators.CHARGING_ITEM, "Charging")

    def tap_charging_item(self):
        self.click_element(*UserGuidePageLocators.CHARGING_ITEM)

    def should_be_charging_screen(self):
        self.check_screen_title(*UserGuidePageLocators.CHARGING_SCREEN_TITLE, "Charging")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.CHARGING_YOUR_DEVICE_TITLE, 'Charging your Device')
        self.check_message(*UserGuidePageLocators.CHARGING_UE_FITS_WILL_SUPPORT,
                           'UE FITS will support an average of 8 hours of listening time outside of the case and a '
                           'total of 20 hours with the case included.')
        self.check_message(*UserGuidePageLocators.CHARGING_USB_C_CABLE,
                           "A USB-C cable is included for charging. Simply plug the case and cable into a standard"
                           " USB power source (5V 500mA).")
        self.check_message(*UserGuidePageLocators.CHARGING_LED_INTERACTIONS, 'Charging LED Interactions')
        assert self.is_element_present(*UserGuidePageLocators.CHARGING_INDICATION_TABLE), "Indication table not located"

    # Adjusting EQ
    def should_be_adjusting_eq_item(self):
        assert self.is_element_present(*UserGuidePageLocators.ADJUSTING_EQ_ARROW), "Adjusting EQ arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.ADJUSTING_EQ_DIVIDER), "Adjusting EQ divider not found"
        self.check_button(*UserGuidePageLocators.ADJUSTING_EQ_ITEM, "Adjusting EQ")

    def tap_adjusting_eq_item(self):
        self.click_element(*UserGuidePageLocators.ADJUSTING_EQ_ITEM)

    def should_be_adjusting_eq_screen(self):
        self.check_screen_title(*UserGuidePageLocators.ADJUSTING_EQ_SCREEN_TITLE, "Adjusting EQ")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.ADJUSTING_EQ_TO_ACCESS,
                           "To access the EQ menu, remove the earbuds from the case, open the UE FITS app and select"
                           " the curve at the bottom of the app home screen.")
        self.check_message(*UserGuidePageLocators.ADJUSTING_EQ_TO_CHANGE, "To change presets, select one of the "
                                                                          "available presets.")
        self.check_message(*UserGuidePageLocators.ADJUSTING_EQ_TO_CREATE,
                           "To create a custom preset, select “customize” and adjust the 5-band EQ to your liking, "
                           "then select “Save As” in the upper right hand corner.")
        self.check_message(*UserGuidePageLocators.ADJUSTING_EQ_CREATE_A_PRESET,
                           "Create a preset name, choose a color and icon to recall your preset more easily, and "
                           "select “Save” from the upper right hand corner.")
        assert self.is_element_present(*UserGuidePageLocators.ADJUSTING_EQ_IMAGE), "EQ image not located"

    # Testing your Fit
    def should_be_tyf_item(self):
        assert self.is_element_present(*UserGuidePageLocators.TYF_ARROW), "Testing your Fit arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.TYF_DIVIDER), "Testing your Fit divider not found"
        self.check_button(*UserGuidePageLocators.TYF_ITEM, "Testing Your Fit")

    def tap_tyf_item(self):
        self.click_element(*UserGuidePageLocators.TYF_ITEM)

    def should_be_tyf_screen(self):
        self.check_screen_title(*UserGuidePageLocators.TYF_SCREEN_TITLE, "Testing Your Fit")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.TYF_GREAT_FIT,
                           "A great fit makes for a comfortable and quality listening experience. If you feel your "
                           "eartips are not appropriately fitted, “Test Your Fit” will help you assess your fit.")
        self.check_message(*UserGuidePageLocators.TYF_BY_ANSWERING,
                           "By answering a few questions, Test Your Fit will offer suggestions to improve your fit or"
                           " provide your insights to our support team so they can solve your fit issue more quickly.")
        self.check_message(*UserGuidePageLocators.TYF_WHEN_USING, "When using the fit test, remember to touch each "
                                                                  "slider on the pages to proceed to the next page.")

    # Updating Firmware
    def should_be_updating_fw_item(self):
        assert self.is_element_present(*UserGuidePageLocators.UPDATING_FIRMWARE_ARROW), "Updating Firmware arrow " \
                                                                                        "not found"
        assert self.is_element_present(*UserGuidePageLocators.UPDATING_FIRMWARE_DIVIDER), "Updating Firmware divider " \
                                                                                          "not found "
        self.check_button(*UserGuidePageLocators.UPDATING_FIRMWARE_ITEM, "Updating Firmware")

    def tap_updating_fw_item(self):
        self.click_element(*UserGuidePageLocators.UPDATING_FIRMWARE_ITEM)

    def should_be_updating_fw_screen(self):
        self.check_screen_title(*UserGuidePageLocators.UPDATING_FIRMWARE_TITLE, "Updating Firmware")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.UPDATING_FIRMWARE_IF_FW_UPDATE,
                           "If a firmware update is available for your FITS, you’ll be shown a pop-up that prompts "
                           "you to install the new firmware as soon as you open the app.")
        self.check_message(*UserGuidePageLocators.UPDATING_FIRMWARE_UPDATES_CAN,
                           "Updates can also be accessed from the hamburger menu in the upper left corner of the app "
                           "under Support > Firmware. Here you can see if you have the latest version or access an "
                           "available update.")
        self.check_message(*UserGuidePageLocators.UPDATING_FIRMWARE_TO_COMPLETE,
                           "To complete the update, make sure your UE FITS are in the case with the lid open and"
                           " charging.")
        self.check_message(*UserGuidePageLocators.UPDATING_FIRMWARE_MOST_UPDATES,
                           "Most updates will take around 10 minutes to complete.")

    # Troubleshooting
    def should_be_troubleshooting_item(self):
        assert self.is_element_present(*UserGuidePageLocators.TROUBLESHOOTING_ARROW), "Troubleshooting arrow not found"
        assert self.is_element_present(*UserGuidePageLocators.TROUBLESHOOTING_DIVIDER), "Troubleshooting divider " \
                                                                                        "not found"
        self.check_button(*UserGuidePageLocators.TROUBLESHOOTING_ITEM, "Troubleshooting")

    def tap_troubleshooting_item(self):
        self.click_element(*UserGuidePageLocators.TROUBLESHOOTING_ITEM)

    def should_be_troubleshooting_screen(self):
        self.check_screen_title(*UserGuidePageLocators.TROUBLESHOOTING_TITLE, "Troubleshooting")
        self.should_be_back_arrow()
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_FIRST_ACTION,
                           "The first action you should take while troubleshooting is checking that your firmware is "
                           "up to date. Reference instructions to update in the “Updating Firmware” section of this "
                           "user guide.")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_CONNECTING_ISSUES, "Issues related to connecting")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_IF_YOU_HAVE_CONNECTING_ISSUES,
                           "If you are having issues connecting or with dropouts, a reset may solve the issue.")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_TO_RESET,
                           "To reset and clear pairing memory, place your FITS in their case and press and hold the "
                           "upper right button inside the case for 8 seconds, or until the earbuds flash amber. Then "
                           "release the button.")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_CONNECTING_ISSUES_NOTE,
                           "Note: Auto-connect may not occur if the case battery is empty. In this case, double tap "
                           "the earbuds to wake them from standby. It may take a few seconds for the earbuds to "
                           "reconnect after manually waking them from standby mode.")
        self.swipe_up()
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_CONNECTING_ISSUES_STANDBY,
                           "Your earbuds may go into standby mode if there is no audio streaming for 60 minutes. To "
                           "wake your earbuds up from Standby mode, either double tap the earbuds just as you would "
                           "to activate a control or place them in and then remove them from a charged case. It may "
                           "take a few seconds for the earbuds to power on and reconnect after waking from standby.")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_CHARGING_ISSUES, "Issues related to charging")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_NOT_CHARGING,
                           "If your earbuds are not charging properly, make sure they are properly seated on the "
                           "charging pins before closing the lid. Each earbud has a dedicated seat in the case—they "
                           "are not interchangeable.")
        self.check_message(*UserGuidePageLocators.TROUBLESHOOTING_IF_CONTINUE,
                           "If you continue to have trouble charging, plug the case in and factory reset the earbuds "
                           "in the case by pressing and holding the charge case button until the LEDs glow amber, "
                           "approximately 15 seconds.")
