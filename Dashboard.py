"""POM-Dashboard page of Zenportal"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Dashboard():
    def __init__(self):
        self.profile_click_locator = (By.XPATH,'//img[@id="profile-click-icon"]')
        self.logout_locator = (By.XPATH,'//div[text()="Log out"]')
    def test_logout(self,pdriver):
        wait=WebDriverWait(pdriver,25)
        wait.until(ec.visibility_of_element_located(self.profile_click_locator))
        pdriver.find_element(*self.profile_click_locator).click()
        wait.until(ec.visibility_of_element_located(self.logout_locator))
        pdriver.find_element(*self.logout_locator).click()