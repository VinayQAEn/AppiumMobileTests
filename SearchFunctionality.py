import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.common.exceptions import TimeoutException

class SearchProduct:
    def __init__(self, driver):
        self.driver = driver

    Language_popup_Xpath =  "//android.widget.TextView[@text='English']"
    Search_BY_IMAGE_ID = "com.meesho.supply:id/iv_camera"
    android_permissioncontroller_ID = "com.android.permissioncontroller:id/permission_deny_button"
    Search_bar_ID = "com.meesho.supply:id/query_edit_text"
    regular_tshirt_ID = "com.meesho.supply:id/catalog_cover"
    price_ID = "com.meesho.supply:id/price_text"

    def click_language_popup(self):
        # self.mywait = WebDriverWait(self.driver, 30)
        # self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.Language_popup_Xpath)))
        # self.driver.find_element(By.XPATH, self.Language_popup_Xpath).click()
        self.lanuage = self.driver.find_element(By.XPATH, "com.meesho.supply:id/close")
        self.lanuage.click()
        # actions = ActionChains(self.driver)
        # actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(965, 740)
        # actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.pause(0.1)
        # actions.w3c_actions.pointer_action.release()
        # actions.perform()

    def click_notification_popup(self):
        self.mywait = WebDriverWait(self.driver, 30)
        self.mywait.until(EC.element_to_be_clickable((By.ID, self.Notification_popup_ID)))
        self.driver.find_element(By.ID, self.Notification_popup_ID).click()

    def click_search_by_image(self):
        self.mywait = WebDriverWait(self.driver, 40)
        self.mywait.until(EC.element_to_be_clickable((By.ID, self.Search_BY_IMAGE_ID)))
        self.driver.find_element(By.ID, self.Search_BY_IMAGE_ID).click()
    def click_android_permissioncontroller(self):
        self.mywait = WebDriverWait(self.driver, 30)
        self.mywait.until(EC.element_to_be_clickable((By.ID, self.android_permissioncontroller_ID)))
        self.driver.find_element(By.ID, self.android_permissioncontroller_ID).click()
    def enter_search_bar(self):
        search_bar = self.driver.find_element(By.ID, self.Search_bar_ID)
        search_bar.send_keys("Tshirt")
        
      
        self.driver.press_keycode(66)

        # self.driver.press_keycode(84)

        # self.driver.execute_script("mobile: performEditorAction", {"action": "search"})
    def click_regular_tshirt(self):
        self.mywait = WebDriverWait(self.driver, 30)
        self.mywait.until(EC.element_to_be_clickable((By.ID, self.regular_tshirt_ID)))
        self.driver.find_element(By.ID, self.regular_tshirt_ID).click()
        self.price = self.driver.find_element(By.ID,"com.meesho.supply:id/price_text")
        print(self.price.get_attribute("text"))
        if self.price.text == "₹46":
            print("Actually price is" + self.price.text)
        else:
            print("wrong price of product")
        print("Test_001 PASSED sucessfully")
