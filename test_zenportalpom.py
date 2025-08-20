"""
Test Cases are designed for
1. Email and Password Validation
2. Submit button Validation
3. Logout Functionality
4. Successful Login
5. Unsuccessful Login
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

# importing POM of Zen portal
import sys, os
sys.path.append(os.path.dirname(os.path.abspath("D:\Workspace\PAT\Task14")))
from Task14.POM_ZenPortal.Dashboard import Dashboard
from Task14.POM_ZenPortal.Login import Zenlogin

# c. Email text box validation

def test_email_validation():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()
        email_textbox= driver.find_element(*zenlogin.email_locator)

        print("Email Text Box Validation:")
        # 1. Verify whether email is displayed
        if email_textbox.is_displayed():
            print("1. Email is displayed")

        # 2. Verify whether email is enabled
        if email_textbox.is_enabled():
            print("2. Email is enabled")

        # 3. Verify whether user is able to enter the value in email textbox
        email_textbox.send_keys("cknithyakala.gmail.com")
        print("3. User is able to enter value in the Email text box")

        # 4. Retrieve the entered value (email)
        user_entered_value= email_textbox.get_attribute("value")
        print("4. User Entered Value:",user_entered_value)

        # 5. Verify whether email is required field
        #select all text in email text box
        email_textbox.send_keys(Keys.CONTROL+"a")

        #delete selected text
        email_textbox.send_keys(Keys.DELETE)

        wait.until(ec.visibility_of_element_located((By.XPATH,'//p[ @ id = ":r1:-helper-text"]')))
        help_msg = driver.find_element(By.XPATH,'//p[ @ id = ":r1:-helper-text"]').text
        print("5. Message is displayed when we remove the value in Email: ", help_msg)
    finally:
        #close the browser
        driver.quit()

# c. Password text box Validation
def test_password_validation():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()
        password_textbox = driver.find_element(*zenlogin.password_locator)

        print("Password Text Box Validation:")
        # 1. Verify whether email is displayed
        if password_textbox.is_displayed():
            print("1. Password text box is displayed")

        # 2. Verify whether email is enabled
        if password_textbox.is_enabled():
            print("2. Password is enabled")

        # 3. Verify whether user is able to enter the value in email textbox
        password_textbox.send_keys("Bnrh@7677")
        print("3. User is able to enter value in the Password text box")

        # 4. Retrieve the entered value (email)
        user_entered_value = password_textbox.get_attribute("value")
        print("4. User Entered Value:", user_entered_value)

        # 5. Verify whether email is required field
        # select all text in email text box
        password_textbox.send_keys(Keys.CONTROL + "a")

        # delete selected text
        password_textbox.send_keys(Keys.DELETE)

        wait.until(ec.visibility_of_element_located((By.XPATH, '//p[ @ id = ":r1:-helper-text"]')))
        help_msg = driver.find_element(By.XPATH, '//p[ @ id = ":r1:-helper-text"]').text
        print("5. Message is displayed when we remove the value in Password: ", help_msg)
    finally:
        # close the browser
        driver.quit()

# d. Submit button - Positive test case
def test_submit_button_positive():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()

        # Calling login method in Zenlogin class
        username = "cknithyakala@gmail.com"
        password = "Bnrh@7677"
        zenlogin.test_login(pdriver=driver, username=username, password=password)

        # Closing launch alert using wait
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'✕')]")))
        driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()

        #Verifying the webpage after login
        if driver.current_url == "https://www.zenclass.in/dashboard":
            print("Submit button is working properly.")
    finally:
        #Closing the browser
        driver.quit()

#d. Submit is not working - Negative test case 1
def test_submit_button_negative1():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()

        # Calling login method in Zenlogin class
        # Trying to signin without giving value for Email and Password
        username = ""
        password = ""
        zenlogin.test_login(pdriver=driver, username=username, password=password)

        #Verifying the webpage after login
        if driver.current_url == "https://www.zenclass.in/dashboard":
            print("Submit button is working properly.")
        else:
            #Getting the message displayed in the webpage
            wait.until(ec.visibility_of_element_located((By.XPATH, '//p[ @ id = ":r0:-helper-text"]')))
            help_msg1 = driver.find_element(By.XPATH, '//p[ @ id = ":r0:-helper-text"]').text
            print("Message 1:",help_msg1)

            wait.until(ec.visibility_of_element_located((By.XPATH, '//p[ @ id = ":r1:-helper-text"]')))
            help_msg2 = driver.find_element(By.XPATH, '//p[ @ id = ":r1:-helper-text"]').text
            print("Message 2:", help_msg2)

    finally:
        #Closing the browser
        driver.quit()

#d. Submit is not working - Negative test case 2
def test_submit_button_negative2():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()

        # Calling login method in Zenlogin class
        # Trying to signin by not giving value for Password
        username = "cknithyakala@gmail.com"
        password = ""
        zenlogin.test_login(pdriver=driver, username=username, password=password)

        #Verifying the webpage after login
        if driver.current_url == "https://www.zenclass.in/dashboard":
            print("Submit button is working properly.")
        else:
            #Getting the message displayed in the webpage
            wait.until(ec.visibility_of_element_located((By.XPATH, '//p[ @ id = ":r1:-helper-text"]')))
            help_msg1 = driver.find_element(By.XPATH, '//p[ @ id = ":r1:-helper-text"]').text
            print("Message displayed:", help_msg1)

    finally:
        #Closing the browser
        driver.quit()

#d. Submit is not working - Negative test case 3
def test_submit_button_negative3():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()

        # Calling login method in Zenlogin class
        # Trying to signin by giving value incorrect Password
        username = "cknithyakala@gmail.com"
        password = "abcde@2"
        zenlogin.test_login(pdriver=driver, username=username, password=password)

        #Verifying the webpage after login
        if driver.current_url == "https://www.zenclass.in/dashboard":
            print("Submit button is working properly.")
        else:
            #Getting the message displayed in the webpage
            wait.until(ec.visibility_of_element_located((By.XPATH, '//p[ @ id = ":r1:-helper-text"]')))
            help_msg1 = driver.find_element(By.XPATH, '//p[ @ id = ":r1:-helper-text"]').text
            print("Message displayed:", help_msg1)

    finally:
        #Closing the browser
        driver.quit()

# a. Successful Login
def test_successful_login():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating instance for WebDriverwait
        wait = WebDriverWait(driver, 30)

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()

        # Calling login method in Zenlogin class
        username = "cknithyakala@gmail.com"
        password = "Bnrh@7677"
        zenlogin.test_login(pdriver=driver, username=username, password=password)

        # Closing launch alert using wait
        wait.until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(),'✕')]")))
        driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()

        #Verifying the webpage after login
        assert "https://www.zenclass.in/dashboard"==driver.current_url, "Login is not working properly."
    finally:
        driver.quit()

# b. Unsucessful Login
def test_unsuccessful_login():
    try:
        # Setup chrome options
        chrome_options = Options()

        # 1 -Allow 2 - Block in notification popup
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)

        # Launch Chrome
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.get("https://www.zenclass.in/login")

        # Creating Object/instance for Zenlogin() class
        zenlogin = Zenlogin()

        # Calling login method in Zenlogin class
        username = "cknithyakala@gmail.com"
        password = "Bnrh"
        zenlogin.test_login(pdriver=driver, username=username, password=password)
        print(driver.current_url)
        # Verifying the webpage after login
        assert "https://www.zenclass.in/dashboard"!=driver.current_url, "Incorrect page is displayed"

    finally:
        #closing the browser
        driver.quit()

# e. Logout functionality
def test_logout_functionality():
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
        zenlogin.test_login(pdriver=driver,username=username,password=password)

        #Closing launch alert using wait
        wait.until(ec.presence_of_element_located((By.XPATH,"//button[contains(text(),'✕')]")))
        driver.find_element(By.XPATH,"//button[contains(text(),'✕')]").click()

        #Creating object/instance for Dashboard class
        dashboard=Dashboard()

        #Calling logout method in Dashboard class
        dashboard.test_logout(pdriver=driver)
        wait.until(ec.visibility_of_element_located(zenlogin.email_locator))

        #Verifying the webpage after logout
        assert "https://www.zenclass.in/login"==driver.current_url,"Logout is not working properly"

    finally:
        driver.quit()

