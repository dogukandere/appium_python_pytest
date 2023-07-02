from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    HEPSIBURADA_LOGO = (By.ID, "com.pozitron.hepsiburada:id/image_message_of_day")
    SEARCH_WITH_CAMERA_BUTTON = (By.ID, "com.pozitron.hepsiburada:id/ivCamera")
    NOTIFICATION_BUTTON = (By.ID, "com.pozitron.hepsiburada:id/imageViewNotification")
    ACCOUNT_BUTTON = (By.ID, "com.pozitron.hepsiburada:id/account_menu_button")
    LOCATION_CHOOSE_BUTTON = (By.ID, "com.pozitron.hepsiburada:id/textViewLocation")

    def is_hepsiburada_logo_displayed(self):
        return self.is_displayed(self.HEPSIBURADA_LOGO)

    def is_search_with_camera_button_displayed(self):
        return self.is_displayed(self.SEARCH_WITH_CAMERA_BUTTON)

    def is_notification_button_displayed(self):
        return self.is_displayed(self.NOTIFICATION_BUTTON)

    def is_account_button_displayed(self):
        return self.is_displayed(self.ACCOUNT_BUTTON)

    def is_location_button_displayed(self):
        return self.is_displayed(self.LOCATION_CHOOSE_BUTTON)



