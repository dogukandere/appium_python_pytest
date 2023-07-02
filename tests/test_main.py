import pytest
from pages.main_page import MainPage
from pages.hepsi_page import HepsiPage

@pytest.mark.usefixtures("setup")
class TestMain:

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.mainpage = MainPage(self.driver)
        self.hepsipage = HepsiPage(self.driver)

    def test_main_page(self):
        assert (self.mainpage.is_hepsiburada_logo_displayed())
        assert (self.mainpage.is_search_with_camera_button_displayed())
        assert (self.mainpage.is_notification_button_displayed())
        assert (self.mainpage.is_account_button_displayed())
        assert (self.mainpage.is_location_button_displayed())

    def test_hepsi_overlay(self):
        self.hepsipage.click_hepsi_button()
        assert (self.hepsipage.is_market_button_displayed())
        assert (self.hepsipage.is_water_button_displayed())
        assert (self.hepsipage.is_plane_ticket_button_displayed())
        assert (self.hepsipage.is_flower_button_displayed())
        assert (self.hepsipage.is_game_button_displayed())


