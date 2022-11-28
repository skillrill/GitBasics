from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # constructor method
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "[type='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    
    
    def user_login(self):
        self.login(self.USER, self.USER_PASSWORD)
    

    def admin_login(self):
        self.login(self.ADMIN, self.ADMIN_PASSWORD)
    

    # def login_with_blank_user_name(self):
    #     self.login('', 'Demo-Access1')


    # def login_with_incorrect_credentials(self):
    #     self.login('test', 'test')