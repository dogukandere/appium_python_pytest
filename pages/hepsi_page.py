from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HepsiPage(BasePage):

    NAV_BAR_HEPSI_BUTTON = (By.ID, "com.pozitron.hepsiburada:id/ivMenuItemAll")
    MARKET_BUTTON = (By.XPATH, "//androidx.cardview.widget.CardView[@content-desc='Market']/android.widget.ImageView")
    WATER_BUTTON = (By.XPATH, "//androidx.cardview.widget.CardView[@content-desc='Su']/android.widget.ImageView")
    PLANE_TICKET_BUTTON = (By.XPATH, "//androidx.cardview.widget.CardView[@content-desc='Uçak Bileti']/android.widget.ImageView")
    FLOWER_BUTTON = (By.XPATH, "//androidx.cardview.widget.CardView[@content-desc='Çiçek']/android.widget.ImageView")
    GAME_BUTTON = (By.XPATH, "//androidx.cardview.widget.CardView[@content-desc='Oynadıkça Kazan']/android.widget.ImageView")

    def click_hepsi_button(self):
        self.click(self.NAV_BAR_HEPSI_BUTTON)
        
    def is_market_button_displayed(self):
        return self.is_displayed(self.MARKET_BUTTON)

    def is_water_button_displayed(self):
        return self.is_displayed(self.WATER_BUTTON)

    def is_plane_ticket_button_displayed(self):
        return self.is_displayed(self.PLANE_TICKET_BUTTON)

    def is_flower_button_displayed(self):
        return self.is_displayed(self.FLOWER_BUTTON)

    def is_game_button_displayed(self):
        return self.is_displayed(self.GAME_BUTTON)

