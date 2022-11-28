from time import sleep

class BasePage:

    USER = 'Demo-User'
    USER_PASSWORD = 'Demo-Access1'
    ADMIN = 'Bank-Admin'
    ADMIN_PASSWORD = 'Demo-Access1'
    TIMEOUT = 10


    def __init__(self, driver) -> None:
        self.driver = driver
    

    def text_exists(self, text):
        wait = 0
        while wait < self.TIMEOUT:
            if text.lower() not in self.driver.page_source.lower():
                sleep(1)
                wait += 1
            else:
                return True
        return False
        
