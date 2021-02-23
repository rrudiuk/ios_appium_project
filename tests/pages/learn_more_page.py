from .base_page import BasePage
from .locators import LearnMoreLocators

from ..utilities import logger


class LearnMorePage(BasePage):
    def should_be_learn_more_menu_icon(self):
        assert self.is_element_present(*LearnMoreLocators.MENU_ICON), "Close button not located"

    def tap_learn_more_menu_icon(self):
        logger.LOGGER.info('Tapping close button')
        self.click_element(*LearnMoreLocators.MENU_ICON)

    def should_be_page_indicator(self):
        assert self.is_element_present(*LearnMoreLocators.PAGE_INDICATOR), 'Page indicator not found'

    # Double tap control
    def should_be_double_tap_control_title(self):
        self.check_screen_title(*LearnMoreLocators.DOUBLE_TAP_CONTROL_TITLE, "Double Tap Control")

    def should_be_double_tap_control_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.DOUBLE_TAP_CONTROL_SUBTITLE,
                                   'Double-tap the left or right earbud to Play/Pause audio or Answer/End calls.')

    def should_be_double_tap_control_animation(self):
        self.is_element_present(*LearnMoreLocators.DOUBLE_TAP_CONTROL_ANIMATION), "Animation video not found"

    # Custom Control
    def should_be_custom_control_title(self):
        self.check_screen_title(*LearnMoreLocators.CUSTOM_CONTROL_TITLE, 'Custom Control')

    def should_be_custom_control_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.CUSTOM_CONTROL_SUBTITLE, 'Left and Right Double tap controls '
                                                                               'can be customized independently in '
                                                                               'the Settings menu.')

    def should_be_custom_control_image(self):
        assert self.is_element_present(*LearnMoreLocators.CUSTOM_CONTROL_IMAGE), 'Custom control image not found'

    # Switching devices
    def should_be_switching_devices_title(self):
        self.check_screen_title(*LearnMoreLocators.SWITCHING_DEVICES_TITLE, 'Switching Devices')

    def should_be_switching_devices_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.SWITCHING_DEVICES_SUBTITLE,
                                   'To connect to another device that has been previously '
                                   'paired, go to the Bluetooth menu of the new device and '
                                   'select UE FITS.')

    def should_be_switching_devices_image(self):
        assert self.is_element_present(*LearnMoreLocators.SWITCHING_DEVICES_IMAGE), 'Switching devices image not found'

    # EQ Customization
    def should_be_eq_customization_title(self):
        self.check_screen_title(*LearnMoreLocators.EQ_CUSTOMIZATION_TITLE, 'EQ Customization')

    def should_be_eq_customization_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.EQ_CUSTOMIZATION_SUBTITLE, 'Select from fine-tuned default UE '
                                                                                 'presets or tap Customize to create '
                                                                                 'your own.')

    def should_be_eq_customization_image(self):
        assert self.is_element_present(*LearnMoreLocators.EQ_CUSTOMIZATION_IMAGE), 'EQ customization image not found'

    # Test your fit
    def should_be_test_your_fit_title(self):
        self.check_screen_title(*LearnMoreLocators.TEST_YOUR_FIT_TITLE, 'Test Your Fit')

    def should_be_test_your_fit_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.TEST_YOUR_FIT_SUBTITLE,
                                   'Your fit is guaranteed for 30 days.\nFrom the main menu, '
                                   'you can take a short quiz to confirm you have the perfect '
                                   'fit.')

    def should_be_test_your_fit_image(self):
        assert self.is_element_present(*LearnMoreLocators.TEST_YOUR_FIT_IMAGE), "No test your fit image"

    # Pair a new device
    def should_be_pair_new_device_title(self):
        self.check_screen_title(*LearnMoreLocators.PAIR_NEW_DEVICE_TITLE, 'Pair a New Device')

    def should_be_pair_new_device_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.PAIR_NEW_DEVICE_SUBTITLE,
                                   'To pair with a new device, place your earbuds in the '
                                   'case and press the case button until the earbuds flash '
                                   'white.')

    def should_be_pair_new_device_animation(self):
        assert self.is_element_present(*LearnMoreLocators.PAIR_NEW_DEVICE_ANIMATION), 'Pair a new device animation ' \
                                                                                      'not found'

    def should_be_pair_new_device_notice(self):
        self.check_message(*LearnMoreLocators.PAIR_NEW_DEVICE_NOTICE, 'Note: You can only have one device connected at'
                                                                      ' any given time.')

    # Status Indicators
    def should_be_status_indicators_title(self):
        self.check_screen_title(*LearnMoreLocators.STATUS_INDICATORS_TITLE, 'Status Indicators')

    def should_be_status_indicators_subtitle(self):
        self.check_screen_subtitle(*LearnMoreLocators.STATUS_INDICATORS_SUBTITLE,
                                   'Lighting indicators on the charging case and '
                                   'the earbud indicate charging status of UE FITS.')

    def should_be_status_indicators_image(self):
        assert self.is_element_present(*LearnMoreLocators.STATUS_INDICATORS_IMAGE), "No status indicators image"

    def should_be_status_indicators_notice(self):
        self.check_message(*LearnMoreLocators.STATUS_INDICATORS_NOTICE, '*To reset your earbuds, press and hold '
                                                                        'the case button '
                                                                        'until the earbuds blink amber.')
