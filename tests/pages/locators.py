from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

APP_PACKAGE_NAME = ""


# Add your locators below


class BasePageLocators:
    # BACK_ARROW = (By.XPATH, '//XCUIElementTypeButton[@name="Back"]')
    BACK_ARROW = (MobileBy.ACCESSIBILITY_ID, 'Back')
    KEYBOARD_RETURN = (MobileBy.ACCESSIBILITY_ID, 'Return')
    SCREEN_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_title")
    SCREEN_SUBTITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_subtitle")
    TOOL_BAR_TITLE = (By.CLASS_NAME, "android.widget.TextView")
    BUTTON_MAIN = (By.ID, f"{APP_PACKAGE_NAME}:id/button")
    PROGRESS_BAR = (By.ID, f"{APP_PACKAGE_NAME}:id/progress_bar")
    ACCEPT_BT_ALERT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="OK"]')


class AnalyticsPageLocators:
    ANALYTICS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Help Us Improve Our Products')
    ANALYTICS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Help Ultimate Ears improve its products and services by '
                                                     'automatically sending diagnostic and usage data.')
    ANALYTICS_SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Yes, share analytics data"]')
    ANALYTICS_NOT_SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="No Thanks"]')
    ANALYTICS_LEARN_MORE = (MobileBy.ACCESSIBILITY_ID, 'This can be changed from the Main Menu under Support. Learn'
                                                       ' more about our Privacy Policy.')


class OhboyDemoPageLocators:
    CLOSE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Close"]')
    DEBUG_BUTTON = (By.XPATH, '//XCUIElementTypeNavigationBar['
                              '@name="UE_FITS_beta.ModlingDebugView"]/XCUIElementTypeButton[5]')
    START_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Start"]')
    STATE_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="IDLE"]')
    CLEAR_HISTORY_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Delete"]')
    # Vendor ID
    VENDOR_ID_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Vendor ID: 0x')
    VENDOR_ID = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                           '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                           '/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField[1]')
    # Command
    COMMAND_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Command ID: 0x')
    COMMAND = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                         '2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField[2]')
    # Payload
    PAYLOAD_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Payload: 0x')
    PAYLOAD = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                         '2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField[3]')
    # Send command
    SEND_COMMAND_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Send"]')
    # Check responses
    LIST_OF_RESPONSES = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                   '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeTable')
    FIRST_RESPONSE = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    SECOND_RESPONSE = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                 '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeTable/XCUIElementTypeCell[2]')
    SENT_COMMAND_FIRST = (By.XPATH, '(//XCUIElementTypeStaticText[@name="0x0422"])[1]')
    SENT_COMMAND_FIRST_STATUS = (By.XPATH, '(//XCUIElementTypeStaticText[@name="success"])[1]')
    SENT_COMMAND_FIRST_PAYLOAD = (By.XPATH, '(//XCUIElementTypeStaticText[@name="00"])[1]')
    SENT_COMMAND_SECOND = (By.XPATH, '(//XCUIElementTypeStaticText[@name="0x0422"])[2]')
    SENT_COMMAND_SECOND_STATUS = (By.XPATH, '(//XCUIElementTypeStaticText[@name="success"])[2]')
    SENT_COMMAND_SECOND_PAYLOAD = (By.XPATH, '(//XCUIElementTypeStaticText[@name="00"])[2]')


class DialogPageLocators:
    DIALOG_TITLE = (MobileBy.ACCESSIBILITY_ID, 'PopupTitle')
    DIALOG_MESSAGE = (MobileBy.ACCESSIBILITY_ID, 'PopupSubtitle')
    UPDATE_DIALOG_ACTION_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Update Earbuds"]')
    UPDATE_DIALOG_DISMISS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Dismiss"]')


class EqPresetsPageLocators:
    # Toolbar locators
    TOOLBAR = (By.ID, f"{APP_PACKAGE_NAME}:id/toolbar")
    LEFT_BATTERY_IMAGE_COLLAPSED = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_battery_collapsed")
    RIGHT_BATTERY_IMAGE_COLLAPSED = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_battery_collapsed")
    CASE_BATTERY_IMAGE_COLLAPSED = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_case_battery_collapsed")
    SAVE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/item_save")
    # Expandable EQ block locators
    EXPANDABLE_BLOCK = (By.ID, f"{APP_PACKAGE_NAME}:id/group_expandable_part")
    CUSTOMIZE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_customize")
    DIVIDER_LINE = (By.ID, f"{APP_PACKAGE_NAME}:id/separator")
    PRESETS_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_presets")
    EDIT_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_edit")
    ADD_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_add")
    PRESETS_RECYCLER_VIEW = (By.ID, f"{APP_PACKAGE_NAME}:id/recycler_view_presets")
    PRESET_NAME = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view")
    PRESET_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view")
    PRESET_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator")
    EXPAND_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_expand")
    CHOSEN_PRESET_NAME = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_chosen_preset")
    EQ_CURVE_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/equalizer_view")
    # Edit Presets screen locators
    REMOVE_PRESET_ICON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_remove")
    DRAG_PRESET_ICON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_drag")
    EDIT_PRESETS_LIST = (By.ID, f"{APP_PACKAGE_NAME}:id/recycler_view")
    # Preset configurator locators
    EQ_EDITOR = (By.ID, f"{APP_PACKAGE_NAME}:id/equalizer_view")
    HISTORY_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_history_title")
    BACKWARD_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_backward")
    FORWARD_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_forward")
    PROGRESS_HISTORY_BAR = (By.ID, f"{APP_PACKAGE_NAME}:id/seek_bar_history")


class EmailEntryPageLocators:
    EMAIL_ENTRY_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Never Miss A Beat')
    EMAIL_ENTRY_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Stay up to date on firmware updates, giveaways, beta '
                                                       'testing opportunities, and more.')
    SIGN_ME_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Sign Me Up"]')
    NO_THANKS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="No Thanks"]')
    EMAIL_ENTRY_REASON_DESCRIPTION = (MobileBy.ACCESSIBILITY_ID, 'This can be changed from the Main Menu under '
                                                                 'Support. Learn more about our Privacy Policy.')
    EMAIL_ENTRY_INPUT = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeTextField')


class FirmwareUpdatePageLocators:
    UPDATE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeButton[4]')
    TITLE_WRAPPER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther')
    FW_ACTIVATION_TITLE = (MobileBy.ACCESSIBILITY_ID, 'FwTitle')
    FW_UPDATE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'FwUpdateTitle')
    UP_TO_DATE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Up to Date')
    UPDATE_AVAILABLE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Update Available')
    UPDATE_EARBUDS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Update Earbuds"]')
    READY_TO_UPDATE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Ready to Update')
    ROLLBACK_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Rollback Earbuds"]')
    INSTALL_NOW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Install Now"]')
    CANCEL_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]')
    INSTALLING_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Installing')
    AN_ERROR_OCCURRED_TITLE = (MobileBy.ACCESSIBILITY_ID, 'An Error Occurred')
    RESTARTING_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Restarting')
    YOU_ARE_ALL_SET_TITLE = (MobileBy.ACCESSIBILITY_ID, 'You’re All Set!')
    RECONNECTING_DIALOG_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Reconnecting...')
    ERROR_DIALOG_TITLE = (MobileBy.ACCESSIBILITY_ID, 'PopupTitle')
    ERROR_MESSAGE_TEXT = (MobileBy.ACCESSIBILITY_ID, 'PopupSubtitle')
    # Enable push notifications
    ENABLE_PUSH_NOTIFICATIONS_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'mobile')
    ENABLE_PUSH_NOTIFICATIONS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Enable Push Notifications')
    ENABLE_PUSH_NOTIFICATIONS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Enabling push notifications allows you to stay '
                                                                     'up to date with the latest version of the UE FITS'
                                                                     ' firmware.')
    ENABLE_PUSH_NOTIFICATIONS_NOTICE = (MobileBy.ACCESSIBILITY_ID, 'This can be changed from your device Settings.')
    ENABLE_PUSH_NOTIFICATIONS_CLOSE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar['
                                                              '@name="UE_FITS_beta.PushNotificationRequestView'
                                                              '"]/XCUIElementTypeButton')
    PUSH_NOTIFICATIONS_ENABLE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Yes, Enable Push '
                                                        'Notifications"]')
    PUSH_NOTIFICATIONS_NO_THANKS_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="No Thanks"]')


class HomePageLocators:
    EARBUDS_NAME = (MobileBy.ACCESSIBILITY_ID, 'FITS BP4')
    EARBUDS_STATUS_CONNECTED = (MobileBy.ACCESSIBILITY_ID, 'Connected')
    EARBUDS_STATUS_SCANNING = (MobileBy.ACCESSIBILITY_ID, 'Scanning')
    CONNECT_EARBUDS_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_connect")
    HOME_SCREEN_LEFT_MENU = (MobileBy.ACCESSIBILITY_ID, 'menu')
    HOME_SCREEN_SETTINGS = (MobileBy.ACCESSIBILITY_ID, 'settings')
    LEFT_EARBUD_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeButton[3]')
    RIGHT_EARBUD_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeButton[4]')
    CASE_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                  '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                  '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                  '/XCUIElementTypeImage[4]')
    LEFT_BATTERY_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther[2]/XCUIElementTypeImage')
    RIGHT_BATTERY_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                           '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther[3]/XCUIElementTypeImage')
    CASE_BATTERY_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther[4]/XCUIElementTypeImage')
    LEFT_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_percents")
    RIGHT_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_percents")
    CASE_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_case_percents")


class LandingPageLocators:
    CASE_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'earpods_case_outline')
    LANDING_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Let’s Get Started')
    LANDING_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Place your earbuds in the case\nwith the lid open to get started.')
    LANDING_LOADER = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther[3]/XCUIElementTypeOther')


class LearnMoreLocators:
    MENU_ICON = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar['
                                 '@name="UE_FITS_beta.LearnMoreView"]/XCUIElementTypeButton')
    PAGE_INDICATOR = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                      '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                      '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                      '/XCUIElementTypeOther/XCUIElementTypePageIndicator')
    # Double tap control
    DOUBLE_TAP_CONTROL_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Double Tap Control')
    DOUBLE_TAP_CONTROL_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Double-tap the left or right earbud to Play/Pause '
                                                              'audio or Answer/End calls.')

    DOUBLE_TAP_CONTROL_ANIMATION = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                    'beta"]/XCUIElementTypeWindow['
                                                    '1]/XCUIElementTypeOther/XCUIElementTypeOther'
                                                    '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                    '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                    '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                    '/XCUIElementTypeOther/XCUIElementTypeOther')
    # Custom Control
    CUSTOM_CONTROL_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Custom Control')
    CUSTOM_CONTROL_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Left and Right Double tap controls can be customized'
                                                          ' independently in the Settings menu.')
    CUSTOM_CONTROL_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'learn_more_custom_control')
    # Switching devices
    SWITCHING_DEVICES_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Switching Devices')
    SWITCHING_DEVICES_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'To connect to another device that has been previously '
                                                             'paired, go to the Bluetooth menu of the new device and '
                                                             'select UE FITS.')
    SWITCHING_DEVICES_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'learn_more_switch_devices')
    # EQ Customization
    EQ_CUSTOMIZATION_TITLE = (MobileBy.ACCESSIBILITY_ID, 'EQ Customization')
    EQ_CUSTOMIZATION_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Select from fine-tuned default UE presets or '
                                                            'tap Customize to create your own.')
    EQ_CUSTOMIZATION_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'learn_more_eq')
    # Test your fit
    TEST_YOUR_FIT_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Test Your Fit')
    TEST_YOUR_FIT_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Your fit is guaranteed for 30 days.\nFrom the main menu, '
                                                         'you can take a short quiz to confirm you have the perfect '
                                                         'fit.')
    TEST_YOUR_FIT_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'learn_more_tyf')
    # Pair a new device
    PAIR_NEW_DEVICE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Pair a New Device')
    PAIR_NEW_DEVICE_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'To pair with a new device, place your earbuds in the '
                                                           'case and press the case button until the earbuds flash '
                                                           'white.')
    PAIR_NEW_DEVICE_ANIMATION = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                 'beta"]/XCUIElementTypeWindow['
                                                 '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                 '/XCUIElementTypeOther/XCUIElementTypeOther')
    PAIR_NEW_DEVICE_NOTICE = (MobileBy.ACCESSIBILITY_ID, 'Note: You can only have one device connected at'
                                                         ' any given time.')
    # Status Indicators
    STATUS_INDICATORS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Status Indicators')
    STATUS_INDICATORS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Lighting indicators on the charging case and '
                                                             'the earbud indicate charging status of UE FITS.')
    STATUS_INDICATORS_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'learn_more_statuses')
    STATUS_INDICATORS_NOTICE = (MobileBy.ACCESSIBILITY_ID, '*To reset your earbuds, press and hold the case button'
                                                           ' until the earbuds blink amber.')


class MenuPageLocators:
    HEADER_CONTAINER = (MobileBy.ACCESSIBILITY_ID, 'UE_FITS_beta.LeftMenuView')
    APPLICATION_LOGO = (MobileBy.ACCESSIBILITY_ID, 'ue-fits-dark')
    CLOSE_ICON = (MobileBy.ACCESSIBILITY_ID, 'Close')
    EMAIL_ENTRY_ITEM = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Email Entry"]')
    HOME_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Home"]')
    MOLD_NEW_TIPS_ITEM = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Mold New Tips"]')
    TEST_YOUR_FIT_ITEM = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Test Your Fit"]')
    LEARN_MORE_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Learn More"]')
    SUPPORT_ITEM = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Support"]')
    TAKE_SELFIE_ITEM = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Take a Selfie"]')
    USER_GUIDE_ITEM = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="User Guide"])')


class MoldingPageLocators:
    # How to pair
    HOW_TO_PAIR_TITLE = (MobileBy.ACCESSIBILITY_ID, 'How to Pair')
    HOW_TO_PAIR_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Watch the video to learn how to pair your earbuds.')
    HOW_TO_PAIR_VIDEO = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther')
    HOW_TO_PAIR_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Got it!"]')
    # Try them on
    TRY_THEM_PAGE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Try Them On')
    TRY_THEM_PAGE_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Pop both earbuds into your ears. Gently adjust them until '
                                                         'they feel comfortable and secure. You will mold both sides '
                                                         'at the same time.')
    TRY_THEM_PAGE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    TRY_THEM_PAGE_ANIMATION = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther[2]')
    # Get ready screen
    GET_READY_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Let’s Do This"]')
    GET_READY_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Get Ready')
    MOLDING_TEXT_VIEW_TITLE1 = (MobileBy.ACCESSIBILITY_ID, '1')
    MOLDING_TEXT_VIEW_TITLE2 = (MobileBy.ACCESSIBILITY_ID, '2')
    MOLDING_TEXT_VIEW_TITLE3 = (MobileBy.ACCESSIBILITY_ID, '3')
    MOLDING_TEXT_VIEW_MSG1 = (MobileBy.ACCESSIBILITY_ID, 'We’ll do a quick sound test to ensure a sound-isolating '
                                                         'fit before we mold.')
    MOLDING_TEXT_VIEW_MSG2 = (MobileBy.ACCESSIBILITY_ID, 'We’ll share some quick tips for achieving the best mold.')
    MOLDING_TEXT_VIEW_MSG3 = (MobileBy.ACCESSIBILITY_ID, 'The 60 second molding magic starts.')
    MOLDING_SMILE_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'Union')
    MOLDING_STAND_BY_MIRROR = (MobileBy.ACCESSIBILITY_ID, 'Try standing in front of a mirror for this part')
    # How's the bass
    HOW_IS_THE_BASS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'How’s the Bass?')
    HOW_IS_THE_BASS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Gently adjust both earbuds until you find the position '
                                                           'that maximizes the bass. ')
    MOLDING_IMAGE_VOLUME = (MobileBy.ACCESSIBILITY_ID, 'soundOn')
    MOLDING_BAR_ADJUST_VOLUME = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                           '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther[2]/XCUIElementTypeSlider')
    MOLDING_CANCEL_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Cancel"]')
    # Starting soon
    MOLDING_START_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Starting Soon')
    MOLDING_START_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'During the molding process,\nthe tips will feel warm\nas '
                                                         'they mold to your ears.')
    MOLDING_START_SUBTITLE2 = (MobileBy.ACCESSIBILITY_ID, 'Gently hold your earbuds\nin place the entire time.')
    # Molding running
    MOLDING_PROGRESS_BAR = (By.XPATH, '//XCUIElementTypeProgressIndicator[@name="Progress"]')
    # Congratulations
    CONGRATULATIONS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Congratulations')
    CONGRATULATIONS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'You now have perfectly fitting earbuds.\n\nTake the tour '
                                                           'to learn about the features of the app and how to make '
                                                           'the most of your UE FITS.')
    CONGRATULATIONS_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'magic')
    TAKE_TOUR_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Take the Tour"]')
    SKIP_FOR_NOW_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Skip For Now"]')
    FINISH_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Finish"]')
    CONGRATULATIONS_SUBTITLE_FINISH = (MobileBy.ACCESSIBILITY_ID, 'You now have perfectly fitting earbuds. Throw on '
                                                                  'your favorite song and take them for a spin.')
    # Mold new tips
    MENU_ICON = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar['
                                 '@name="UE_FITS_beta.YourTipsView"]/XCUIElementTypeButton')
    SCROLL_ELEMENTS = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                       '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePageIndicator')
    NEXT_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    # CHANGE YOUR TIPS
    CHANGE_YOUR_TIPS_ANIMATION = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                  'beta"]/XCUIElementTypeWindow['
                                                  '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                  '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                  '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                  '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                  '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther')
    CHANGE_YOUR_TIPS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Change Your Tips')
    CHANGE_YOUR_TIPS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'To remove your current tips, position one finger at '
                                                            'the top of the tip and gently peel off.')
    # REMOVE INSERTS
    REMOVE_INSERTS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Remove Inserts')
    REMOVE_INSERTS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Remove the hard plastic inserts from your new tips by '
                                                          'pulling on the insert tab.')
    REMOVE_INSERTS_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'yt_2')
    # MATCH THEM UP
    MATCH_THEM_UP_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Match Them Up')
    MATCH_THEM_UP_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, "Match the tips to the correct earbud. You’ll\nsee an "
                                                         "‘R’ and ‘L’ on the inside of the tips.")
    MATCH_THEM_UP_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'yt_3')
    # Attach your tips
    ATTACH_YOUR_TIPS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Attach Your Tips')
    ATTACH_YOUR_TIPS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Insert each earbud into the tip.\nYou won’t have to press '
                                                            'too hard to attach them.')
    ATTACH_YOUR_TIPS_IMAGE = (MobileBy.XPATH,
                              '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                              '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther '
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther')
    # CHECK THE FIT
    CHECK_THE_FIT_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Check The Fit')
    CHECK_THE_FIT_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Make sure the tips are flush with the earbuds.')
    CHECK_THE_FIT_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'tips_attached_diagram')


class PairYourEarbudsLocators:
    PAIR_YOUR_EARBUDS_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view")
    BLUETOOTH_SETTINGS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                    ".TextView")


class SebulbaDemoPageLocators:
    CLOSE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Close')
    M_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'M')
    SEND_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Send"]')
    RESET_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Reset"]')
    # FEATURE SELECTOR
    FEATURE_ID_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Feature ID:')
    FEATURE_SELECTOR = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther['
                                        '2]/XCUIElementTypeTextField[1]')
    DONE_BUTTON = (MobileBy.ACCESSIBILITY_ID, 'Done')
    I_ROOT = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                              '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                              '/XCUIElementTypePickerWheel/XCUIElementTypeOther[1]')
    I_FEATURE_SET = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                     '/XCUIElementTypePickerWheel/XCUIElementTypeOther[2]')
    I_DEVICE_INFO = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                     '/XCUIElementTypePickerWheel/XCUIElementTypeOther[3]')
    I_DEVICE_NAME = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                     '/XCUIElementTypePickerWheel/XCUIElementTypeOther[4]')
    I_BT_HOST_INFO = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                      '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                      '/XCUIElementTypePickerWheel/XCUIElementTypeOther[5]')
    I_HEADSET_PARA_EQ = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                         '/XCUIElementTypePickerWheel/XCUIElementTypeOther[6]')
    I_FITS_MOLDING = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                      '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                      '/XCUIElementTypePickerWheel/XCUIElementTypeOther[7]')
    I_FITS_TAP_CONTROL = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                          '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                          '/XCUIElementTypePickerWheel/XCUIElementTypeOther[8]')
    I_FITS_PROXIMITY_DETECTION = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                  'beta"]/XCUIElementTypeWindow['
                                                  '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                                  '/XCUIElementTypePickerWheel/XCUIElementTypeOther[9]')
    I_FITS_MOTION_DETECTION = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                               'beta"]/XCUIElementTypeWindow['
                                               '3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypePicker'
                                               '/XCUIElementTypePickerWheel/XCUIElementTypeOther[10]')
    # FUNCTION SELECTOR
    FUNCTION_ID_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Function ID:')
    FUNCTION_SELECTOR = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther['
                                         '2]/XCUIElementTypeTextField[2]')
    GET_MOLDING_PREP_MODE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                       '.widget.ListView/android.widget.TextView[1]')
    SET_MOLDING_PREP_MODE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                       '.widget.ListView/android.widget.TextView[2]')
    # Payload
    PAYLOAD_INPUT = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther['
                                     '2]/XCUIElementTypeTextField[3]')
    PAYLOAD_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Payload: 0x')
    # Molding state check screen
    MOLDING_ENABLED_STATE = (MobileBy.ACCESSIBILITY_ID, 'Current state: bothBudsEnabled')
    MOLDING_DISABLED_STATE = (MobileBy.ACCESSIBILITY_ID, 'Current state: bothBudsDisabled')


class SupportPageLocators:
    FIRMWARE_ITEM = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[4]')


class TutorialHomePageLocators:
    pass


class UserGuidePageLocators:
    NAVIGATION_BAR = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="User Guide"]')
    NAV_BAR_HAMBURGER_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="User '
                                                'Guide"]/XCUIElementTypeButton')
    NAV_BAR_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="User Guide"]')
    USER_GUIDE_SCREEN_BACK_ARROW = (MobileBy.ACCESSIBILITY_ID, 'User Guide')
    # PAIRING
    PAIRING_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Pairing')
    PAIRING_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[1]')
    PAIRING_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                       '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[2]')
    PAIRING_SCREEN_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Pairing"]')
    PAIRING_TEXT1 = (MobileBy.ACCESSIBILITY_ID, 'To pair a new device, place the earbuds in the case with '
                                                'the lid open.')
    PAIRING_TEXT2 = (MobileBy.ACCESSIBILITY_ID, 'Press and hold the upper right button inside the case until'
                                                ' the earbuds flash white—approximately three seconds—then'
                                                ' release the button.')
    PAIRING_CASE_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeImage')
    OHBOY_PAIRING_WATCH_VIDEO = (MobileBy.ACCESSIBILITY_ID, 'Watch the video to learn how to pair your earbuds.')
    # OHBOY_PAIRING_VIDEO = (MobileBy.ACCESSIBILITY_ID, '//XCUIElementTypeApplication[@name="UE FITS '
    #                                                   'beta"]/XCUIElementTypeWindow['
    #                                                   '1]/XCUIElementTypeOther/XCUIElementTypeOther'
    #                                                   '/XCUIElementTypeOther/XCUIElementTypeOther'
    #                                                   '/XCUIElementTypeOther/XCUIElementTypeOther'
    #                                                   '/XCUIElementTypeScrollView/XCUIElementTypeOther'
    #                                                   '/XCUIElementTypeOther')
    OHBOY_PAIRING_VIDEO = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                           '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther')
    OHBOY_PAIRING_ONE_NOT_CONNECTED = (MobileBy.ACCESSIBILITY_ID, 'After pairing, one of the earbuds will be listed'
                                                                  ' as Not Connected. This is normal.')
    SEBULBA_PAIRING_SELECT_UE_FITS = (MobileBy.ACCESSIBILITY_ID, 'In your Bluetooth settings, select UE FITS to '
                                                                 'begin pairing.')
    SEBULBA_PAIRING_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                             'beta"]/XCUIElementTypeWindow['
                                             '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                             '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                             '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeImage[2]')
    # MOLDING
    MOLDING_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Molding')
    MOLDING_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[2]')
    MOLDING_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                       '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                       '/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeOther[2]')
    MOLDING_SCREEN_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Molding"]')
    MOLDING_A_FEW_THINGS = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="A few things to know before '
                                            'molding your new ear tips."])[1]')

    MOLDING_SOUND_TEST = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Sound Test page"])[1]')
    MOLDING_ADJUST_BOTH_EARBUDS = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Adjust both earbuds until '
                                                   'you find the position that maximizes the bass."])[1]')
    MOLDING_APPLY_GENTLE_PRESSURE = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Apply gentle pressure to'
                                                     ' both earbuds—just enough to get a good seal with the ear '
                                                     'tip—and maintain that pressure throughout the entire molding'
                                                     ' process."])[1]')
    MOLDING_AFTER_SOUND_TEST = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="After the sound test, the app'
                                                ' will show a short countdown and automatically start molding your'
                                                ' tips."])[1]')
    MOLDING_MIX_AMD_MATCH = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Mix and match tips"])[1]')
    MOLDING_SEVERAL_PAIRS = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="If you have several pairs of tips,'
                                             ' feel free to mix and match the left and right tips between sets to get'
                                             ' the best fit for each ear."])[1]')
    MOLDING_CLICK_ON_APP_MENU = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Click on the app menu and '
                                                 'select “Mold New Tips” to start molding your new tips."])[1]')
    # CONTROLS
    CONTROLS_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Controls')
    CONTROLS_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[3]')
    CONTROLS_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeTable/XCUIElementTypeCell[3]/XCUIElementTypeOther[2]')
    CONTROLS_SCREEN_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Controls"]')
    CONTROLS_DOUBLE_AND_SINGLE = (MobileBy.ACCESSIBILITY_ID, 'Double and Single Tap Control')
    CONTROLS_EACH_FITS_EARBUD = (MobileBy.ACCESSIBILITY_ID, 'Each FITS earbud has a double-tap control that defaults'
                                                            ' to play/pause on both left and right earbuds.')
    CONTROLS_PHONE_CALL = (MobileBy.ACCESSIBILITY_ID, 'When a phone call is active, double-tap to accept or '
                                                      'end the call.')
    CONTROLS_ENABLE_SINGLE_TAP = (MobileBy.ACCESSIBILITY_ID, 'Enable single tap for even more control options.')
    CONTROLS_TO_USE = (MobileBy.ACCESSIBILITY_ID, 'To use the controls, tap directly on the earbud body.')
    CONTROLS_HOW_TO_USE_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                 'beta"]/XCUIElementTypeWindow['
                                                 '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                 '/XCUIElementTypeImage[1]')
    CONTROLS_CUSTOMIZATION = (MobileBy.ACCESSIBILITY_ID, 'Control Customization')
    CONTROLS_EACH_EARBUD = (MobileBy.ACCESSIBILITY_ID, 'Each earbud can be customized separately in the Settings menu.')
    CONTROLS_ACCESS_SETTINGS = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                'beta"]/XCUIElementTypeWindow['
                                                '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                '/XCUIElementTypeImage[2]')
    # CONNECTIVITY AND SWITCHING DEVICES
    CONNECTIVITY_AND_SWITCHING_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Connectivity and Switching Devices')
    CONNECTIVITY_AND_SWITCHING_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[4]')
    CONNECTIVITY_AND_SWITCHING_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                          'beta"]/XCUIElementTypeWindow['
                                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther'
                                                          '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                          '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                          '/XCUIElementTypeTable/XCUIElementTypeCell['
                                                          '4]/XCUIElementTypeOther[2]')
    CONNECTIVITY_AND_SWITCHING_SCREEN_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Connectivity and '
                                                               'Switching Devices"]')
    CONNECTIVITY_AND_SWITCHING_TITLE = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Switching Between Paired '
                                                        'Devices"])[1]')
    CONNECTIVITY_AND_SWITCHING_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                        'beta"]/XCUIElementTypeWindow['
                                                        '1]/XCUIElementTypeOther/XCUIElementTypeOther'
                                                        '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                        '/XCUIElementTypeOther/XCUIElementTypeOther'
                                                        '/XCUIElementTypeScrollView/XCUIElementTypeOther'
                                                        '/XCUIElementTypeImage[1]')
    CONNECTIVITY_AND_SWITCHING_FIRST_ENSURE = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="First, ensure you '
                                                               'have the latest firmware. See the “Update your '
                                                               'Firmware” section of the user guide for more '
                                                               'information."])[1]')
    CONNECTIVITY_AND_SWITCHING_YOU_CAN_SWITCH_OHBOY = (MobileBy.XPATH,
                                                       '//XCUIElementTypeStaticText[@name="You can switch between '
                                                       'multiple paired devices by selecting UE FITS L or UE FITS R '
                                                       'in the Bluetooth settings menu of the device you wish to '
                                                       'connect to. In some cases, you may have to select UE FITS a '
                                                       'second time in order to complete the connection."]')
    CONNECTIVITY_AND_SWITCHING_YOU_CAN_SWITCH_SEBULBA = (MobileBy.ACCESSIBILITY_ID,
                                                         'You can switch between multiple paired devices by selecting '
                                                         'UE FITS in the Bluetooth settings menu of the device you '
                                                         'wish to connect to. In some cases, you may have to select '
                                                         'UE FITS a second time in order to complete the connection')
    CONNECTIVITY_AND_SWITCHING_CASE_INTERACTIONS = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Case '
                                                                    'Connectivity Interactions"])[1]')
    CONNECTIVITY_AND_SWITCHING_IN_CASE = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="When the earbuds are '
                                                          'in the case, opening the case will auto-connect them to '
                                                          'the last paired device."])[1]')
    CONNECTIVITY_AND_SWITCHING_AUTO_CONNECTION = (MobileBy.XPATH,
                                                  '(//XCUIElementTypeStaticText[@name="Auto-connect may not occur if '
                                                  'the case battery is empty. In this case, double tap the earbuds to '
                                                  'wake them from standby. It may take a few seconds for the earbuds '
                                                  'to reconnect after manually waking them from standby mode."])[1]')
    CONNECTIVITY_AND_SWITCHING_USING_SINGLE_EARBUD = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Using a '
                                                                      'single earbud for communication"])[1]')
    CONNECTIVITY_AND_SWITCHING_TO_USE_SINGLE = (MobileBy.XPATH,
                                                '(//XCUIElementTypeStaticText[@name="To use a single earbud for '
                                                'communication, place the earbud you are not using in the case. This '
                                                'ensures that the mics on the earbud you are wearing are '
                                                'activated."])[1]')
    CONNECTIVITY_AND_SWITCHING_STANDBY = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Standby"])[1]')
    CONNECTIVITY_AND_SWITCHING_AFTER_60 = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="After 60 minutes with '
                                                           'no audio streaming, your earbuds will automatically go '
                                                           'into standby mode. A tone can be heard when the earbuds '
                                                           'go into standby."])[1]')
    CONNECTIVITY_AND_SWITCHING_TO_WAKE = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="To wake your earbuds '
                                                          'up from Standby mode, either take them in and out of the '
                                                          'charged case or double tap the earbuds. It may take a few '
                                                          'seconds for the earbuds to power on and reconnect after '
                                                          'waking from standby."])[1]')
    CONNECTIVITY_AND_SWITCHING_TO_APP = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Connecting to the '
                                                         'app"])[1]')
    CONNECTIVITY_AND_SWITCHING_WILL_CONNECT = (MobileBy.XPATH,
                                               '(//XCUIElementTypeStaticText[@name="UE FITS will connect to the app '
                                               'when they are in the case with the lid open or they are out of the '
                                               'case completely."])[1]')
    CONNECTIVITY_AND_SWITCHING_SECOND_DEVICE = (MobileBy.XPATH,
                                                '(//XCUIElementTypeStaticText[@name="You may be connected to a second '
                                                'device and still use the app on the primary device. For example, '
                                                'you can use your phone app to control the earbud EQ and settings '
                                                'even if you’re currently connected to your computer."])[1]')
    CONNECTIVITY_AND_SWITCHING_APP_WILL_DISPLAY = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="The app will '
                                                                   'display the currently connected device name on '
                                                                   'the home screen."])[1]')
    # CHARGING
    CHARGING_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Charging')
    CHARGING_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[5]')
    CHARGING_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeTable/XCUIElementTypeCell[5]/XCUIElementTypeOther[2]')
    CHARGING_SCREEN_TITLE = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Charging"])[1]')
    CHARGING_YOUR_DEVICE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Charging your Device')
    CHARGING_UE_FITS_WILL_SUPPORT = (MobileBy.ACCESSIBILITY_ID,
                                     'UE FITS will support an average of 8 hours of listening time outside of the '
                                     'case and a total of 20 hours with the case included.')
    CHARGING_USB_C_CABLE = (MobileBy.ACCESSIBILITY_ID, 'A USB-C cable is included for charging. Simply plug the case'
                                                       ' and cable into a standard USB power source (5V 500mA).')
    CHARGING_LED_INTERACTIONS = (MobileBy.ACCESSIBILITY_ID, 'Charging LED Interactions')
    CHARGING_INDICATION_TABLE = (MobileBy.XPATH,
                                 '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                 '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                 '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther')
    # ADJUSTING_EQ
    ADJUSTING_EQ_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Adjusting EQ')
    ADJUSTING_EQ_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[6]')
    ADJUSTING_EQ_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                            'beta"]/XCUIElementTypeWindow['
                                            '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                            '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                            '/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeOther[2]')
    ADJUSTING_EQ_SCREEN_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Adjusting EQ"]')
    ADJUSTING_EQ_TO_ACCESS = (MobileBy.ACCESSIBILITY_ID, 'To access the EQ menu, remove the earbuds from the case, '
                                                         'open the UE FITS app and select the curve at the bottom of '
                                                         'the app home screen.')
    ADJUSTING_EQ_TO_CHANGE = (MobileBy.ACCESSIBILITY_ID, 'To change presets, select one of the available presets.')
    ADJUSTING_EQ_TO_CREATE = (MobileBy.ACCESSIBILITY_ID, 'To create a custom preset, select “customize” and adjust the'
                                                         ' 5-band EQ to your liking, then select “Save As” in the '
                                                         'upper right hand corner.')
    ADJUSTING_EQ_CREATE_A_PRESET = (MobileBy.ACCESSIBILITY_ID,
                                    'Create a preset name, choose a color and icon to recall your preset more easily,'
                                    ' and select “Save” from the upper right hand corner.')
    ADJUSTING_EQ_IMAGE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                          '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                          '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeImage')
    # TYF
    TYF_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Testing Your Fit')
    TYF_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[7]')
    TYF_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                   '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                   '/XCUIElementTypeTable/XCUIElementTypeCell[7]/XCUIElementTypeOther[2]')
    TYF_SCREEN_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Testing Your Fit"]')
    TYF_GREAT_FIT = (MobileBy.ACCESSIBILITY_ID, 'A great fit makes for a comfortable and quality listening '
                                                'experience. If you feel your eartips are not appropriately fitted, '
                                                '“Test Your Fit” will help you assess your fit.')
    TYF_BY_ANSWERING = (MobileBy.ACCESSIBILITY_ID,
                        'By answering a few questions, Test Your Fit will offer suggestions to improve your fit or '
                        'provide your insights to our support team so they can solve your fit issue more quickly.')
    TYF_WHEN_USING = (MobileBy.ACCESSIBILITY_ID, 'When using the fit test, remember to touch each slider on the '
                                                 'pages to proceed to the next page.')
    # UPDATING FIRMWARE
    UPDATING_FIRMWARE_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Updating Firmware')
    UPDATING_FIRMWARE_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[8]')
    UPDATING_FIRMWARE_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                 'beta"]/XCUIElementTypeWindow['
                                                 '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                 '/XCUIElementTypeTable/XCUIElementTypeCell[8]/XCUIElementTypeOther['
                                                 '2]')
    UPDATING_FIRMWARE_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Updating Firmware"]')
    UPDATING_FIRMWARE_IF_FW_UPDATE = (MobileBy.ACCESSIBILITY_ID,
                                      'If a firmware update is available for your FITS, you’ll be shown a pop-up that '
                                      'prompts you to install the new firmware as soon as you open the app.')
    UPDATING_FIRMWARE_UPDATES_CAN = (MobileBy.ACCESSIBILITY_ID,
                                     'Updates can also be accessed from the hamburger menu in the upper left corner '
                                     'of the app under Support > Firmware. Here you can see if you have the latest'
                                     ' version or access an available update.')
    UPDATING_FIRMWARE_TO_COMPLETE = (MobileBy.ACCESSIBILITY_ID, 'To complete the update, make sure your UE FITS are '
                                                                'in the case with the lid open and charging.')
    UPDATING_FIRMWARE_MOST_UPDATES = (MobileBy.ACCESSIBILITY_ID, 'Most updates will take around 10 minutes to '
                                                                 'complete.')
    # TROUBLESHOOTING
    TROUBLESHOOTING_ITEM = (MobileBy.ACCESSIBILITY_ID, 'Troubleshooting')
    TROUBLESHOOTING_ARROW = (MobileBy.XPATH, '(//XCUIElementTypeImage[@name="back_arrow"])[9]')
    TROUBLESHOOTING_DIVIDER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                               'beta"]/XCUIElementTypeWindow['
                                               '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeOther[2]')
    TROUBLESHOOTING_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Troubleshooting"]')
    TROUBLESHOOTING_FIRST_ACTION = (MobileBy.ACCESSIBILITY_ID,
                                    'The first action you should take while troubleshooting is checking that your '
                                    'firmware is up to date. Reference instructions to update in the “Updating '
                                    'Firmware” section of this user guide.')
    TROUBLESHOOTING_CONNECTING_ISSUES = (MobileBy.ACCESSIBILITY_ID, 'Issues related to connecting')
    TROUBLESHOOTING_IF_YOU_HAVE_CONNECTING_ISSUES = (MobileBy.ACCESSIBILITY_ID, 'If you are having issues connecting '
                                                                                'or with dropouts, a reset may solve '
                                                                                'the issue.')
    TROUBLESHOOTING_TO_RESET = (MobileBy.ACCESSIBILITY_ID,
                                'To reset and clear pairing memory, place your FITS in their case and press and hold '
                                'the upper right button inside the case for 8 seconds, or until the earbuds flash '
                                'amber. Then release the button.')
    TROUBLESHOOTING_CONNECTING_ISSUES_NOTE = (MobileBy.ACCESSIBILITY_ID,
                                              'Note: Auto-connect may not occur if the case battery is empty. In this '
                                              'case, double tap the earbuds to wake them from standby. It may take a '
                                              'few seconds for the earbuds to reconnect after manually waking them '
                                              'from standby mode.')
    TROUBLESHOOTING_CONNECTING_ISSUES_STANDBY = (MobileBy.ACCESSIBILITY_ID,
                                                 'Your earbuds may go into standby mode if there is no audio '
                                                 'streaming for 60 minutes. To wake your earbuds up from Standby '
                                                 'mode, either double tap the earbuds just as you would to activate a '
                                                 'control or place them in and then remove them from a charged case. '
                                                 'It may take a few seconds for the earbuds to power on and reconnect '
                                                 'after waking from standby.')
    TROUBLESHOOTING_CHARGING_ISSUES = (MobileBy.ACCESSIBILITY_ID, 'Issues related to charging')
    TROUBLESHOOTING_NOT_CHARGING = (MobileBy.ACCESSIBILITY_ID,
                                    'If your earbuds are not charging properly, make sure they are properly seated on '
                                    'the charging pins before closing the lid. Each earbud has a dedicated seat in '
                                    'the case—they are not interchangeable.')
    TROUBLESHOOTING_IF_CONTINUE = (MobileBy.ACCESSIBILITY_ID,
                                   'If you continue to have trouble charging, plug the case in and factory reset the '
                                   'earbuds in the case by pressing and holding the charge case button until the LEDs '
                                   'glow amber, approximately 15 seconds.')


class UGCPageLocators:
    IMAGE_COLLAGE = (MobileBy.ACCESSIBILITY_ID, 'ugc_gotit_images')
    MENU_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeNavigationBar['
                                   '@name="UE_FITS_beta.YouDidItView"]/XCUIElementTypeButton')
    SKIP_FOR_NOW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Skip For Now"]')
    TAKE_SELFIE_BUTTON = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Take a Selfie"])[2]')
    # TAKE_SELFIE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'You Did It!')
    TAKE_SELFIE_TITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="You Did It!"]')
    TAKE_SELFIE_TITLE_MENU = (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="Take a Selfie"])[1]')
    # TAKE_SELFIE_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Check out the tech that molds your earbuds and capture the '
    #                                                    'experience to save and share. Activating tech will not alter'
    #                                                    ' earbud tip.')
    TAKE_SELFIE_SUBTITLE = (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="Check out the Lightform technology up '
                                            'close and capture the experience to save and share."]')
    UGC_GIF = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                               '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                               '/XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]')


class WelcomePageLocators:
    CODE_SCREEN_TITLE = (MobileBy.ACCESSIBILITY_ID, 'WELCOME')
    CENTURION_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Centurion++"]')
    DEMO_FLOW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Demo Flow"]')
    SEND_CODE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="GET STARTED"]')
    WELCOME_SCREEN_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Get Started"]')
    WELCOME_SCREEN_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Welcome to Your Perfect Fit')
    WELCOME_SCREEN_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'In just a few minutes, you’ll have a pair of perfectly '
                                                          'fitting, incredibly comfortable earbuds. ')
    WELCOME_SCREEN_EDIT_TEXT_CODE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                     'beta"]/XCUIElementTypeWindow['
                                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                     '/XCUIElementTypeTextField')
    WELCOME_SCREEN_WRAPPER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                              'beta"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther')
