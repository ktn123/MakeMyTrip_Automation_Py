from selenium import webdriver

class Base:
    global driver
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\Ketan\\eclipse-workspace-finalprojects\\FlightBooking_Automation\\Executables\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
    def setUp(self):
        self.driver.get("https://www.makemytrip.com/")
    def tearDown(self):
        self.driver.quit()
        
    #WebDriver methods will be declared here
    
    
    
b = Base()
b.setUp()
b.tearDown()




