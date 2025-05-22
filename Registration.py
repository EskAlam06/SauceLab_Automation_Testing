import time
from winreg import KEY_CREATE_SUB_KEY

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Specify the path to the chromedriver executable
service = Service(executable_path=r"D:\edge_driver\edgedriver_win64\msedgedriver.exe")

# Initialize the WebDriver using the Service object
driver = webdriver.Edge(service=service)
driver.implicitly_wait(10)


# Open the Saucedemo website

def login_to_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Insert Username
    driver.find_element(By.ID,"user-name").send_keys("standard_user")

    # Insert Password
    driver.find_element(By.ID,"password").send_keys("secret_sauce")

    # Click Login
    driver.find_element(By.ID,"login-button").click()

# Call the login function
login_to_saucedemo(driver)

# Check for successful login
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
    print("Login Successful!")
except:
    print("Login Failed!")


driver.quit()