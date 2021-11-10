from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators

import time
from pathlib import Path

from ..utilities import logger


class BasePage:

    def __init__(self, driver, timeout=6):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def background_app_for_5_seconds(self):
        self.driver.background_app(5)

    def check_button(self, how, what, expected_result):
        assert self.is_element_present(how, what), f"Button with text {expected_result} not found"
        actual_result = self.driver.find_element(how, what).text
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    def check_screen_title(self, how, what, expected_result):
        assert self.is_element_present(how, what), f'Element with title {expected_result} not found'

        actual_result = self.driver.find_element(how, what).text
        assert actual_result == expected_result, f'Incorrect title {actual_result}, should be {expected_result}'

    def check_screen_subtitle(self, how, what, expected_result):
        assert self.is_element_present(how, what), f"Element with subtitle {expected_result} not found"
        actual_result = self.driver.find_element(how, what).text
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def check_message(self, how, what, expected_result):
        assert self.is_element_present(how, what), f"Element with text {expected_result} not found"
        actual_result = self.driver.find_element(how, what).text
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def click_element(self, how, what):
        time.sleep(1)
        try:
            element = self.driver.find_element(how, what)
            actions = TouchAction(self.driver)
            actions.tap(element)
            actions.perform()
        except NoSuchElementException:
            return False
        return True

    def click_element_10_times(self, how, what):
        time.sleep(1)
        try:
            element = self.driver.find_element(how, what)
            actions = TouchAction(self.driver)
            for i in range(10):
                actions.tap(element)
                actions.perform()
        except NoSuchElementException:
            return False
        return True

    def count_elements(self, how, what):
        try:
            return len(self.driver.find_elements(how, what))
        except NoSuchElementException:
            return 0

    def check_bt_dialog_presence_and_accept_it(self):
        try:
            self.click_element(*BasePageLocators.ACCEPT_BT_ALERT_BUTTON)
            logger.LOGGER.info("BT permission granted")
        except StaleElementReferenceException:
            return False
        return True

    def enter_text(self, how, what, text):

        try:
            self.driver.find_element(how, what).send_keys(text)
        except NoSuchElementException:
            return False

    def get_text(self, how, what, encoding=None):

        try:
            text = self.driver.find_element(how, what).text
        except NoSuchElementException:
            return False
        return text.encode(encoding) if encoding else text

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_enabled(self, how, what):
        try:
            return self.driver.find_element(how, what).is_enabled()
        except NoSuchElementException:
            return False

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def locate_element(self, how, what):
        try:
            return self.driver.find_element(how, what)
        except NoSuchElementException:
            return False

    def locate_elements(self, how, what):
        try:
            return self.driver.find_elements(how, what)
        except NoSuchElementException:
            return False

    def should_be_back_arrow(self):
        assert self.is_element_present(*BasePageLocators.BACK_ARROW)

    def swipe_left(self):
        self.driver.execute_script('mobile:swipe', {'direction': 'left'})

    def swipe_right(self):
        self.driver.execute_script('mobile:swipe', {'direction': 'right'})

    def swipe_up(self):
        self.driver.execute_script('mobile:swipe', {'direction': 'up'})

    def swipe_down(self):
        self.driver.execute_script('mobile:swipe', {'direction': 'down'})

    def scroll_down(self):
        TouchAction(self.driver).press(x=443, y=1965).move_to(x=436, y=1470).release().perform()

    def scroll_down_one_item(self):
        TouchAction(self.driver).press(x=209, y=819).move_to(x=211, y=779).release().perform()

    def show_available_elements(self):
        self.driver.execute_script("mobile: source", {'format': 'description'})
        logger.LOGGER.info("\n-----------------Values---------------")

    def take_screenshot(self):
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        path_to_current_directory = Path().absolute()
        path_to_screenshots_folder = str(path_to_current_directory) + '/Screenshots/'
        self.driver.save_screenshot(path_to_screenshots_folder + ts + ".png")

    def two_finger_tap_element_5_times(self, how, what):
        time.sleep(1)
        try:
            el = self.driver.find_element(how, what)
            for i in range(5):
                self.driver.execute_script('mobile:twoFingerTap', {'element': el})
        except NoSuchElementException:
            return False
        return True

    def two_finger_tap_element_10_times(self, how, what):
        time.sleep(1)
        try:
            el = self.driver.find_element(how, what)
            for i in range(10):
                self.driver.execute_script('mobile:twoFingerTap', {'element': el})
        except NoSuchElementException:
            return False
        return True

    def tap_back_arrow(self):
        self.click_element(*BasePageLocators.BACK_ARROW)

    def tap_keyboard_return_key(self):
        self.click_element(*BasePageLocators.KEYBOARD_RETURN)

    def wait_for_connection(self):
        time.sleep(14)
