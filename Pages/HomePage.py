from Base.BaseModule import Base
from selenium.webdriver.common.by import By

class Home(Base):
    #b = Base()
    
    def navigate_to_FightsMenu(self):
        print(self.driver)
        self.driver.find_element(By.CSS_SELECTOR,".menu_Flights a").click()
    
    def navigate_to_CabsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Hotels a").click()
    
    def navigate_to_HotelsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Trains a").click()
    
    def navigate_to_TrainsMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Buses a").click()
        
    def navigate_to_BusesMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,".menu_Cabs a").click()
    

b.setUp()

h = Home()
h.navigate_to_FightsMenu()   
h.navigate_to_BusesMenu()
h.navigate_to_HotelsMenu()
h.navigate_to_CabsMenu()
h.navigate_to_TrainsMenu()

b.tearDown()