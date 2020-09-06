from Base.BaseModule import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
class Home(Base):
    #b = Base()
    
    def navigate_to_FightsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Flights a").click()
    
    def navigate_to_CabsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Hotels a").click()
    
    def navigate_to_HotelsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Trains a").click()
    
    def navigate_to_TrainsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Buses a").click()
        
    def navigate_to_BusesMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Cabs a").click()
    
    def scroll_to_super_offers(self):
        self.driver.execute_script("window.scrollTo(0, 400)") 
        self.ex_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div#Offers_Listing")),"Element is Present now.")
        
    def scroll_to_travel_blog(self):
        self.driver.execute_script("window.scrollTo(0,1100)")
        self.ex_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.travelBlog")))
        
    def change_from_booking_country(self,country):
        self.ex_wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"ctrySelect")), "Element is now clickable.")
        self.driver.find_element_by_class_name("ctrySelect").click()
        self.ex_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".ctryList p.ctryListItem:nth-child(1)")))
            
        if country.lower() == "india":
            self.driver.find_element_by_css_selector(".ctryList p.ctryListItem:nth-child(1)").click()
        elif country.lower() == "uae":
            self.driver.find_element_by_css_selector(".ctryList p.ctryListItem:nth-child(2)").click()
        elif country.lower() == "us":
            self.driver.find_element_by_css_selector(".ctryList p.ctryListItem:nth-child(3)").click()
        else:
            print("Country no found in the list")
        #time.sleep(10)
        self.wait_for_page_to_load()
        
    def return_back_to_mmt_homepage(self):
        self.driver.find_element_by_css_selector(".mmtLogo").click()
        self.wait_for_page_to_load()
try:
    h = Home()
    h.setUp()
    h.change_from_booking_country("us")
finally:    
    h.tearDown()
    
    
    
    