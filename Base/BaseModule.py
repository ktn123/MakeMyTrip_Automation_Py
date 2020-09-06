from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Base:
    global driver
    global ex_wait
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\Ketan\\eclipse-workspace-finalprojects\\MakeMyTrip_Automation_Py\\Executables\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.ex_wait = WebDriverWait(self.driver,20)
    
    def login_box_appear(self):
        try:
            if self.ex_wait.until(EC.visibility_of_element_located((By.XPATH,"//p[text()='Login/Signup for Best Prices']"))):
                visible=self.ex_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#stickyScroll")))
                clickable = self.ex_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#stickyScroll")))
                print("-------",visible,clickable)
                self.driver.find_element_by_css_selector("#stickyScroll").click()
                self.ex_wait.until(EC.invisibility_of_element_located((By.XPATH,"//p[text()='Login/Signup for Best Prices']")))
        except:
            print("An Exception occured.")        
    def wait_for_page_to_load(self):
        #To wait for page to load(a specific element to load)
        self.ex_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div#PROMOTIONS")))
        self.login_box_appear()
    
    def setUp(self):
        self.driver.get("https://www.makemytrip.com/")
        self.wait_for_page_to_load()
    
    def tearDown(self):
        self.driver.quit()
        
    #WebDriver methods will be declared here
    




