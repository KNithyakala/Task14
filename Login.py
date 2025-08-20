"""POM-Login Page of ZenPortal"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Zenlogin():
    def __init__(self):
        self.email_locator= (By.XPATH,'//input[@id=":r0:"]')
        self.password_locator= (By.XPATH,'//input[@id=":r1:"]')
        self.signin_locator= (By.XPATH,'//button[text()="Sign in"]')
    def test_login(self,pdriver,username,password):
        wait = WebDriverWait(pdriver, 25)
        wait.until(ec.visibility_of_element_located(self.email_locator))
        pdriver.find_element(*self.email_locator).send_keys(username)
        wait.until(ec.visibility_of_element_located(self.password_locator))
        pdriver.find_element(*self.password_locator).send_keys(password)
        pdriver.find_element(*self.signin_locator).click()