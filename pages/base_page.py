import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_element_visibility(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element

    def click(self, locator):
        element = self.wait_element_visibility(locator)
        element.click()

    def send_keys(self, locator, value):
        action = ActionChains(self.driver)
        element = self.wait_element_visibility(locator)
        action.send_keys_to_element(element, value).perform()

    def is_displayed(self, locator):
        element = self.wait_element_visibility(locator)
        return element.is_displayed()

    def is_enabled(self, locator):
        element = self.wait_element_visibility(locator)
        return element.is_enabled()

    def is_selected(self, locator):
        element = self.wait_element_visibility(locator)
        return element.is_selected()

    def scroll_to_element(self, locator):
        action = TouchAction(self.driver)
        element = self.wait_element_visibility(locator)
        action.scroll_to_element(element).perform()

    def scroll_to_element_2(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_element_visibility(locator)
        action.scroll_to_element(element).perform()

    def move_to_element(self):
        action = TouchAction(self.driver)
        action.press(x=290, y=800).move_to(x=290, y=200).release().perform()

    def swipe_page(self):
        self.driver.swipe(150, 1000, 150, 100, 1000)

    def double_click(self, locator):
        action = TouchAction(self.driver)
        element = self.wait_element_visibility(locator)
        action.double_click(element).perform()

    def hover_over(self, locator):
        action = TouchAction(self.driver)
        element = self.wait_element_visibility(locator)
        action.move_to_element(element).perform()

    def click_and_hold(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_element_visibility(locator)
        action.click_and_hold(element).perform()

    def click_release(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_element_visibility(locator)
        action.release(element).perform()

    def hold_and_release_click(self, locator):
        action = ActionChains(self.driver)
        element = self.wait_element_visibility(locator)
        action.click_and_hold(element).perform()
        time.sleep(7)
        action.release(element).perform()

    def get_text(self, locator):
        element = self.wait_element_visibility(locator)
        return element.text

    def hide_keyboard(self):
        return self.driver.hide_keyboard()

    def driver_back(self):
        return self.driver.back()

    def enter_keyboard(self, element):
        return self.send_keys(element, Keys.ENTER)
