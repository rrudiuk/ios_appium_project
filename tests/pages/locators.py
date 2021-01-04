from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

APP_PACKAGE_NAME = ""
# Add your locators below


class BasePageLocators:
    BACK_ARROW = (By.CLASS_NAME, "android.widget.ImageButton")
    SCREEN_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_title")
    SCREEN_SUBTITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_subtitle")
    TOOL_BAR_TITLE = (By.CLASS_NAME, "android.widget.TextView")
    BUTTON_MAIN = (By.ID, f"{APP_PACKAGE_NAME}:id/button")
    PROGRESS_BAR = (By.ID, f"{APP_PACKAGE_NAME}:id/progress_bar")
    ACCEPT_BT_ALERT_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="OK"]')


class WelcomePageLocators:
    CODE_SCREEN_TITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="WELCOME"]')
    SEND_CODE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="GET STARTED"]')
    WELCOME_SCREEN_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Get Started"]')
    WELCOME_SCREEN_TITLE = (By.XPATH, '//XCUIElementTypeButton[@name="Welcome to Your Perfect Fit"]')
    WELCOME_SCREEN_SUBTITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="In just a few minutes, you’ll have a '
                                         'pair of perfectly fitting, incredibly comfortable earbuds."]')
    WELCOME_SCREEN_EDIT_TEXT_CODE = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                               'beta"]/XCUIElementTypeWindow['
                                               '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                               '/XCUIElementTypeTextField')
    # WELCOME_SCREEN_WHERE_IS_MY_CODE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_help")
    # # WELCOME_SETUP_CODE_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg")
    # WELCOME_SETUP_SCREEN_CLOSE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_close")
    WELCOME_SCREEN_WRAPPER = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                        'beta"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther')


class AnalyticsPageLocators:
    ANALYTICS_TITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="Help Us Improve Our Products"]')
    ANALYTICS_SUBTITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="Help Ultimate Ears improve its products and '
                                    'services by automatically sending diagnostic and usage data."]')
    ANALYTICS_SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Yes, Share Analytics Data"]')
    ANALYTICS_NOT_SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="NO THANKS"]')
    ANALYTICS_LEARN_MORE = (By.XPATH, 'This can be changed from the Main Menu under Support. Learn more about '
                                            'our Privacy Policy.')


class DemoPageLocators:
    DEMO_APP_VERSION = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_app_version")
    DEMO_LEFT_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/left_label")
    DEMO_RIGHT_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/right_label")
    DEMO_LEFT_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/left_status")
    DEMO_RIGHT_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/right_status")
    DEMO_IR_CALIBRATION = (By.ID, f"{APP_PACKAGE_NAME}:id/item_ir_calibration")
    DEMO_DEBUG_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/item_debug")
    DEMO_IR_SWITCHER_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_ir_switcher")
    DEMO_IR_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_ir")
    DEMO_BATTERY_MONITOR_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_battery_monitor")
    DEMO_BATTERY_MONITOR_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_battery_monitor")
    DEMO_TEST_DATA_MONITOR_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_test_data_monitor")
    DEMO_TEST_DATA_MONITOR_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_test_data_monitor")
    DEMO_LEFT_FW_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_firmware_title")
    DEMO_LEFT_FW_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_firmware_value")
    DEMO_RIGHT_FW_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_firmware_title")
    DEMO_RIGHT_FW_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_firmware_value")
    DEMO_START_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/start")
    DEMO_STATE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/state")
    DEMO_SHARE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/menu_share")
    DEMO_CLEAR_HISTORY_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/menu_clear_history")
    DEMO_VENDOR_ID_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/vendor_id_label")
    # DEMO_VENDOR_ID = (By.ID, f"{APP_PACKAGE_NAME}:id/vendor_id")
    DEMO_VENDOR_ID = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.widget.EditText[1]")
    DEMO_COMMAND_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/command_id_label")
    # DEMO_COMMAND = (By.ID, f"{APP_PACKAGE_NAME}:id/command_id")
    DEMO_COMMAND = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/android.widget.EditText[2]")
    DEMO_PAYLOAD_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/payload_label")
    # DEMO_PAYLOAD = (By.ID, f"{APP_PACKAGE_NAME}:id/payload")
    DEMO_PAYLOAD = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/android.widget.EditText[3]")
    DEMO_SEND_COMMAND_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/send")
    DEMO_LIST_OF_RESPONSES = (By.ID, f"{APP_PACKAGE_NAME}:id/toolbar")
    DEMO_FIRST_RESPONSE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                     ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                     "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget"
                                     ".RecyclerView/android.view.ViewGroup[1]")
    DEMO_SECOND_RESPONSE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                      ".widget.RecyclerView/android.view.ViewGroup[2]")
    DEMO_SENT_COMMAND_FIRST = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                         "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                         ".widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[4]")
    DEMO_SENT_COMMAND_FIRST_STATUS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                ".ViewGroup[1]/android.widget.TextView[7]")
    DEMO_SENT_COMMAND_FIRST_PAYLOAD = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                 ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                 ".ViewGroup[1]/android.widget.TextView[6]")
    DEMO_SENT_COMMAND_SECOND = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                          "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                          ".widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[4]")
    DEMO_SENT_COMMAND_SECOND_STATUS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                 ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                 ".ViewGroup[2]/android.widget.TextView[7]")
    DEMO_SENT_COMMAND_SECOND_PAYLOAD = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                  "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                  ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                  ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                  ".ViewGroup[2]/android.widget.TextView[6]")
    # DEMO_EL = (By.ID, "")


class LandingPageLocators:
    CASE_IMAGE = (By.XPATH, '//XCUIElementTypeImage[@name="earpods_case_outline"]')
    LANDING_TITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="Let’s Get Started"]')
    LANDING_SUBTITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="Place your earbuds in the case with the lid '
                                  'open to get started."]')
    LANDING_LOADER = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther[3]/XCUIElementTypeOther')


class MoldingPageLocators:
    MOLDING_TEXT_VIEW_MSG_TITLE1 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_title_1")
    MOLDING_TEXT_VIEW_MSG_TITLE2 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_title_2")
    MOLDING_TEXT_VIEW_MSG_TITLE3 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_title_3")
    MOLDING_TEXT_VIEW_MSG1 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_1")
    MOLDING_TEXT_VIEW_MSG2 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_2")
    MOLDING_TEXT_VIEW_MSG3 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_3")
    MOLDING_SMILE_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_smile")
    MOLDING_IMAGE_VOLUME = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_volume")
    MOLDING_BAR_ADJUST_VOLUME = (By.ID, f"{APP_PACKAGE_NAME}:id/seek_bar_adjust_volume")
    MOLDING_CANCEL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_cancel")
    MOLDING_START_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_start_title")
    MOLDING_START_SUBTITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_start_subtitle")


class PairYourEarbudsLocators:
    PAIR_YOUR_EARBUDS_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view")
    BLUETOOTH_SETTINGS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                    ".TextView")


class DialogPageLocators:
    DIALOG_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_message")
    DIALOG_ACTION_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_action")
    DIALOG_ADDITIONAL_ACTION_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_additional_action")


class HomePageLocators:
    EARBUDS_NAME = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_name")
    EARBUDS_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_status")
    CONNECT_EARBUDS_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_connect")
    HOME_SCREEN_LEFT_MENU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout"
                                       "/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android"
                                       ".view.ViewGroup[1]/android.widget.ImageButton")
    HOME_SCREEN_SETTINGS = (By.ID, f"{APP_PACKAGE_NAME}:id/item_settings")
    LEFT_EARBUD_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_earphone")
    RIGHT_EARBUD_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_earphone")
    CASE_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_case")
    LEFT_BATTERY_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_battery")
    RIGHT_BATTERY_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_battery")
    CASE_BATTERY_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_case_battery")
    LEFT_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_percents")
    RIGHT_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_percents")
    CASE_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_case_percents")


class TutorialHomePageLocators:
    ARROW_TUTORIAL = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_skip_tutorial")
    CUSTOM_EQ_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_custom_eq_title")
    CUSTOM_EQ_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_custom_eq_message")
    GOT_IT_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_got_it")
    TUTORIAL_CONTAINER = (By.ID, f"{APP_PACKAGE_NAME}:id/container")
    TUTORIAL_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_message")
    TUTORIAL_NEXT_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_next")
    SKIP_TUTORIAL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_skip_tutorial")


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


class MenuPageLocators:
    HEADER_CONTAINER = (By.ID, f"{APP_PACKAGE_NAME}:id/navigation_header_container")
    APPLICATION_LOGO = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_logo")
    CLOSE_ICON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_close")
    HOME_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.drawerlayout"
                           ".widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView"
                           "/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.CheckedTextView")
    MOLD_NEW_TIPS_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx"
                                    ".drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx"
                                    ".recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat["
                                    "2]/android.widget.CheckedTextView")
    TEST_YOUR_FIT_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx"
                                    ".drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx"
                                    ".recyclerview.widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat["
                                    "3]/android.widget.CheckedTextView")
    LEARN_MORE_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx"
                                 ".drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/androidx.recyclerview"
                                 ".widget.RecyclerView/androidx.appcompat.widget.LinearLayoutCompat["
                                 "4]/android.widget.CheckedTextView")
    SUPPORT_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_title")


class SupportPageLocators:
    FIRMWARE_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_firmware_clickable")


class FirmwareUpdatePageLocators:
    UPDATE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_update")
