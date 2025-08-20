"""Zenportal is automated using Page Object Model"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
#importing POM
from Task14 import Dashboard
from Task14 import Zenlogin

def Zenportal_automation():
    try:
        #Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs ={"profile.default_content_setting_values.notifications":2}
        chrome_options.add_experimental_option("prefs",prefs)

        #Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        #Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        #Creating Object/instance for Zenlogin() class
        zenlogin=Zenlogin()

        #Calling login method in Zenlogin class
        username="cknithyakala@gmail.com"
        password="Bnrh@7677"
        zenlogin.login(pdriver=driver,username=username,password=password)

        #Closing launch alert using wait
        wait.until(ec.presence_of_element_located((By.XPATH,"//button[contains(text(),'✕')]")))
        driver.find_element(By.XPATH,"//button[contains(text(),'✕')]").click()

        #Creating object/instance for Dashboard class
        dashboard=Dashboard()

        #Calling logout method in Dashboard class
        dashboard.logout(pdriver=driver)

    finally:
        #closing the browser
        driver.quit()

