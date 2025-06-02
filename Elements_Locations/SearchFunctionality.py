from re import S
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchProduct:
    def __init__(self,driver):
        self.driver = driver
    Lanuage_popup_Xpath = "//androidx.recyclerview.widget.RecyclerView[@resource-id='com.meesho.supply:id/language_recycler_view']/android.widget.FrameLayout[2]/android.widget.ImageView"
    Notification_popup_ID = "com.android.permissioncontroller:id/permission_deny_button"
    Search_BY_IMAGE_ID = "com.meesho.supply:id/iv_camera"
    android_permissioncontroller_ID = "com.android.permissioncontroller:id/permission_deny_button"
    Search_bar_ID = "com.meesho.supply:id/query_edit_text"
    regular_tshirt_ID = "com.meesho.supply:id/catalog_cover"
    price_ID = "com.meesho.supply:id/price_text"

    def click_lanuage_popup(self):
        self.mywait = WebDriverWait(self.driver,10)
        self.mywait.until(EC.element_to_be_clickable((By.XPATH,self.Lanuage_popup_Xpath)))
        self.driver.find_element(By.XPATH,self.Lanuage_popup_Xpath).click()
    def click_notification_popup(self):
        self.mywait = WebDriverWait(self.driver,10)
        self.mywait.until(EC.element_to_be_clickable((By.ID,self.Notification_popup_ID)))
        self.driver.find_element(By.ID,self.Notification_popup_ID).click()
    def click_serach_by_image(self):
        self.mywait = WebDriverWait(self.driver,10)
        self.mywait.until(EC.element_to_be_clickable((By.ID,self.Search_BY_IMAGE_ID)))
        self.driver.find_element(By.ID,self.Search_BY_IMAGE_ID).click()
    def click_android_permissioncontroller(self):
        self.mywait = WebDriverWait(self.driver,10)
        self.mywait.until(EC.element_to_be_clickable((By.ID,self.android_permissioncontroller_ID)))
        self.driver.find_element(By.ID,self.android_permissioncontroller_ID).click()
    def enter_search_bar(self,search_text):
        self.mywait = WebDriverWait(self.driver,10)
        self.mywait.until(EC.element_to_be_clickable((By.ID,self.Search_bar_ID)))
        self.driver.find_element(By.ID,self.Search_bar_ID).send_keys(search_text)
        self.driver.execute_script("mobile: performEditorAction", {"action": "search"})
    def click_regular_tshirt(self):
        self.mywait = WebDriverWait(self.driver,10)
        self.mywait.until(EC.element_to_be_clickable((By.ID,self.regular_tshirt_ID)))
        self.price = self.driver.find_element(By.ID,self.regular_tshirt_ID)
        self.price.click()
        print(self.price.get_attribute("text"))
        if self.price.text == "₹150":
            print("Actually price is" + self.price.text)
        else:
            print("wrong price of product")
        print("Test_001 PASSED sucessfully")

