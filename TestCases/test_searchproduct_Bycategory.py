import pytest
import time
from Locators.SearchFunctionality import SearchProduct
@pytest.mark.usefixtures("setup")
class TestSearchproductBycategory:
    def test_searchproductbycategory(self):
        self.sp = SearchProduct(self.driver)
        self.sp.click_language_popup()
        self.sp.click_notification_popup()
        self.sp.click_search_by_image()
        self.sp.click_android_permissioncontroller()
        self.sp.enter_search_bar("Tshirt")
        self.sp.click_regular_tshirt()
        