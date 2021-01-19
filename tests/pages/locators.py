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


class WelcomePageLocators:
    CODE_SCREEN_TITLE = (MobileBy.ACCESSIBILITY_ID, 'WELCOME')
    DEMO_FLOW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Demo Flow"]')
    SEND_CODE_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="GET STARTED"]')
    WELCOME_SCREEN_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Get Started"]')
    # WELCOME_SCREEN_TITLE = (By.XPATH, '//XCUIElementTypeButton[@name="Welcome to Your Perfect Fit"]')
    WELCOME_SCREEN_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Welcome to Your\nPerfect Fit')
    # WELCOME_SCREEN_SUBTITLE = (By.XPATH, '//XCUIElementTypeStaticText[@name="In just a few minutes, you’ll have a '
    #                                      'pair of perfectly fitting, incredibly comfortable earbuds."]')
    WELCOME_SCREEN_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'In just a few minutes, you’ll have a pair\nof perfectly '
                                                          'fitting, incredibly\ncomfortable earbuds.')
    WELCOME_SCREEN_EDIT_TEXT_CODE = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                                     'beta"]/XCUIElementTypeWindow['
                                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                                     '/XCUIElementTypeTextField')
    WELCOME_SCREEN_WRAPPER = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS '
                                              'beta"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                              '/XCUIElementTypeOther')


class AnalyticsPageLocators:
    ANALYTICS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Help Us Improve\nOur Products')
    ANALYTICS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Help Ultimate Ears improve its products\nand services by '
                                                     'automatically sending\ndiagnostic and usage data.')
    ANALYTICS_SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Yes, Share Analytics Data"]')
    ANALYTICS_NOT_SHARE_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="NO THANKS"]')
    ANALYTICS_LEARN_MORE = (MobileBy.ACCESSIBILITY_ID, 'This can be changed from the Main Menu under Support.\nLearn'
                                                       ' more about our Privacy Policy.')


class DemoPageLocators:
    DEMO_CLOSE_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Close"]')
    DEMO_DEBUG_BUTTON = (By.XPATH, '//XCUIElementTypeNavigationBar['
                                   '@name="UE_FITS_beta.ModlingDebugView"]/XCUIElementTypeButton[5]')
    DEMO_START_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Start"]')
    DEMO_STATE_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="IDLE"]')
    DEMO_CLEAR_HISTORY_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Delete"]')
    # Vendor ID
    DEMO_VENDOR_ID_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Vendor ID: 0x')
    DEMO_VENDOR_ID = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField[1]')
    # Command
    DEMO_COMMAND_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Command ID: 0x')
    DEMO_COMMAND = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                              '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                              '2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField[2]')
    # Payload
    DEMO_PAYLOAD_LABEL = (MobileBy.ACCESSIBILITY_ID, 'Payload: 0x')
    DEMO_PAYLOAD = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                              '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther['
                              '2]/XCUIElementTypeOther[2]/XCUIElementTypeTextField[3]')
    # Send command
    DEMO_SEND_COMMAND_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Send"]')
    # Check responses
    DEMO_LIST_OF_RESPONSES = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                        '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                        '/XCUIElementTypeTable')
    DEMO_FIRST_RESPONSE = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeTable/XCUIElementTypeCell[1]')
    DEMO_SECOND_RESPONSE = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                      '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                      '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                      '/XCUIElementTypeTable/XCUIElementTypeCell[2]')
    DEMO_SENT_COMMAND_FIRST = (By.XPATH, '(//XCUIElementTypeStaticText[@name="0x0422"])[1]')
    DEMO_SENT_COMMAND_FIRST_STATUS = (By.XPATH, '(//XCUIElementTypeStaticText[@name="success"])[1]')
    DEMO_SENT_COMMAND_FIRST_PAYLOAD = (By.XPATH, '(//XCUIElementTypeStaticText[@name="00"])[1]')
    DEMO_SENT_COMMAND_SECOND = (By.XPATH, '(//XCUIElementTypeStaticText[@name="0x0422"])[2]')
    DEMO_SENT_COMMAND_SECOND_STATUS = (By.XPATH, '(//XCUIElementTypeStaticText[@name="success"])[2]')
    DEMO_SENT_COMMAND_SECOND_PAYLOAD = (By.XPATH, '(//XCUIElementTypeStaticText[@name="00"])[2]')


class LandingPageLocators:
    CASE_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'earpods_case_outline')
    LANDING_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Let’s Get Started')
    LANDING_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Place your earbuds in the case\nwith the lid open to get started.')
    LANDING_LOADER = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                '/XCUIElementTypeOther[3]/XCUIElementTypeOther')


class MoldingPageLocators:
    # How to pair
    HOW_TO_PAIR_TITLE = (MobileBy.ACCESSIBILITY_ID, 'How To Pair')
    HOW_TO_PAIR_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Each of your earbuds must be connected to\nseparately. They '
                                                       'are listed as UE FITS L and R.\nWatch the video below to '
                                                       'learn how to pair them.')
    HOW_TO_PAIR_VIDEO = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                         '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                         '/XCUIElementTypeOther')
    HOW_TO_PAIR_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Got it!"]')
    # Try them on
    TRY_THEM_PAGE_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Try Them On')
    TRY_THEM_PAGE_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Pop both earbuds into your ears. Gently adjust\nthem until '
                                                         'they feel comfortable and secure.\nYou will mold both sides '
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
    MOLDING_TEXT_VIEW_MSG1 = (MobileBy.ACCESSIBILITY_ID, 'We’ll do a quick sound test to ensure a\nsound-isolating '
                                                         'fit before we mold.')
    MOLDING_TEXT_VIEW_MSG2 = (MobileBy.ACCESSIBILITY_ID, 'We’ll share some quick tips for\nachieving the best mold.')
    MOLDING_TEXT_VIEW_MSG3 = (MobileBy.ACCESSIBILITY_ID, 'The 60 second molding magic starts.')
    MOLDING_SMILE_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'Union')
    MOLDING_STAND_BY_MIRROR = (MobileBy.ACCESSIBILITY_ID, 'Try standing by a mirror for this part')
    # How's the bass
    HOW_IS_THE_BASS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'How’s the Bass?')
    HOW_IS_THE_BASS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Gently adjust both earbuds until you find the\nposition '
                                                           'that maximizes the bass.')
    MOLDING_IMAGE_VOLUME = (MobileBy.ACCESSIBILITY_ID, 'soundOn')
    MOLDING_BAR_ADJUST_VOLUME = (By.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                           '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                           '/XCUIElementTypeOther[2]/XCUIElementTypeSlider')
    MOLDING_CANCEL_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="CANCEL"]')
    # Starting soon
    MOLDING_START_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Starting Soon')
    MOLDING_START_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'During the molding process,\nthe tips will feel warm\nas '
                                                         'they mold to your ears.')
    MOLDING_START_SUBTITLE2 = (MobileBy.ACCESSIBILITY_ID, 'Gently hold your earbuds\nin place the entire time.')
    # Molding running
    MOLDING_PROGRESS_BAR = (By.XPATH, '//XCUIElementTypeProgressIndicator[@name="Progress"]')
    # Congratulations
    CONGRATULATIONS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Congratulations!')
    CONGRATULATIONS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'You now have perfectly fitting earbuds.\n\nTake the tour '
                                                           'to learn about the features\nof the app and how to make '
                                                           'the most of\nyour UE FITS.')
    CONGRATULATIONS_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'magic')
    TAKE_TOUR_BUTTON = (By.XPATH, '//XCUIElementTypeButton[@name="Take the Tour"]')
    SKIP_FOR_NOW_BUTTON = (By.XPATH, '//XCUIElementTypeStaticText[@name="Skip For Now"]')
    FINISH_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Finish"]')
    CONGRATULATIONS_SUBTITLE_FINISH = (MobileBy.ACCESSIBILITY_ID, 'You now have perfectly fitting earbuds.\nThrow on '
                                                                  'your favorite song and take\nthem for a spin.')
    # Mold new tips
    BACK_ARROW = (MobileBy.ACCESSIBILITY_ID, 'backArrow')
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
    CHANGE_YOUR_TIPS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'To remove tips, position one finger at the\ntop of the '
                                                            'tip and gently peel off.\nThen, open your new tips!')
    # REMOVE INSERTS
    REMOVE_INSERTS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Remove Inserts')
    REMOVE_INSERTS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Remove the hard plastic inserts from your new\ntips by '
                                                          'pulling on the insert tab.')
    REMOVE_INSERTS_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'yt_2')
    # MATCH THEM UP
    MATCH_THEM_UP_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Match Them Up')
    MATCH_THEM_UP_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Match the tips to the correct earbud. You’ll\nsee an ‘R’ '
                                                         'and ‘L’ on the inside of the tips.')
    MATCH_THEM_UP_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'yt_3')
    # Attach your tips
    ATTACH_YOUR_TIPS_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Attach Your Tips')
    ATTACH_YOUR_TIPS_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Insert each earbud into the tip.\nYou won’t have to '
                                                            'press too hard to attach them.')
    ATTACH_YOUR_TIPS_IMAGE = (MobileBy.XPATH,
                              '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                              '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther '
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeScrollView'
                              '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                              '/XCUIElementTypeOther')
    # CHECK THE FIT
    CHECK_THE_FIT_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Check The Fit')
    CHECK_THE_FIT_SUBTITLE = (MobileBy.ACCESSIBILITY_ID, 'Make sure the tips are flush with the earphones.')
    CHECK_THE_FIT_IMAGE = (MobileBy.ACCESSIBILITY_ID, 'tips_attached_diagram')


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
    HEADER_CONTAINER = (MobileBy.ACCESSIBILITY_ID, 'UE_FITS_beta.LeftMenuView')
    APPLICATION_LOGO = (MobileBy.ACCESSIBILITY_ID, 'ue-fits-dark')
    CLOSE_ICON = (MobileBy.ACCESSIBILITY_ID, 'Close')
    HOME_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Home"]')
    MOLD_NEW_TIPS_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Mold New Tips"]')
    TEST_YOUR_FIT_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Test Your Fit"]')
    LEARN_MORE_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Learn More"]')
    SUPPORT_ITEM = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Support"]')


class SupportPageLocators:
    FIRMWARE_ITEM = (MobileBy.XPATH, '//XCUIElementTypeApplication[@name="UE FITS beta"]/XCUIElementTypeWindow['
                                     '1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
                                     '/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeButton[4]')


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
    INSTALL_NOW_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Install Now"]')
    CANCEL_BUTTON = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]')
    INSTALLING_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Installing')
    AN_ERROR_OCCURRED_TITLE = (MobileBy.ACCESSIBILITY_ID, 'An Error Occurred')
    RESTARTING_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Restarting')
    YOU_ARE_ALL_SET_TITLE = (MobileBy.ACCESSIBILITY_ID, 'You’re All Set!')
    RECONNECTING_DIALOG_TITLE = (MobileBy.ACCESSIBILITY_ID, 'Reconnecting...')
    ERROR_DIALOG_TITLE = (MobileBy.ACCESSIBILITY_ID, 'PopupTitle')
    ERROR_MESSAGE_TEXT = (MobileBy.ACCESSIBILITY_ID, 'PopupSubtitle')


class TutorialHomePageLocators:
    pass
