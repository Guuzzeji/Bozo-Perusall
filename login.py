import sys
from time import sleep
from selenium.webdriver.common.by import By

from browser import Browser

_LOGIN_URL = "https://app.perusall.com/"


class Login(Browser):
    def __init__(self, driver, headless) -> None:
        super(Login, self).__init__(driver, headless)
        self.is_login = False

    def login_to_perusall(self, username: str, password: str) -> None:
        self.driver.get(_LOGIN_URL)
        sleep(5)

        # Login html
        username_field = self.driver.find_element(By.ID, "at-field-email")
        password_field = self.driver.find_element(By.ID, "at-field-password")
        login_btn = self.driver.find_element(By.ID, "at-btn")

        # Login action
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_btn.click()
        sleep(3)

        if self._is_login():
            print("[ERROR] --> Failed to login")
            self.close_browser()
            sys.exit(1)

        print("[LOGIN TO ACCOUNT]")
        self.is_login = True

    def _is_login(self) -> bool:
        return len(self.driver.find_elements(By.CLASS_NAME, "at-error")) > 0
