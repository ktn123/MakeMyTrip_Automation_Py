from selenium import webdriver

class Base:
    global driver
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\Ketan\\eclipse-workspace-finalprojects\\MakeMyTrip_Automation_Py\\Executables\\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        print(self.driver)
    def setUp(self):
        self.driver.get("https://www.makemytrip.com/")
    def tearDown(self):
        self.driver.quit()
        
    #WebDriver methods will be declared here
    




