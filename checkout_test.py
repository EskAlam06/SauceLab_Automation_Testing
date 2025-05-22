import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Test_Login.Registration import login_to_saucedemo

# Set up Edge WebDriver
service = Service(executable_path=r"D:\edge_driver\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.implicitly_wait(10)

# Explicit wait
wait = WebDriverWait(driver, 10)

# Login
login_to_saucedemo(driver)

# Navigate to inventory page (optional if login redirects automatically)
driver.get("https://www.saucedemo.com/inventory.html")

# Add first item to cart
add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))
add_to_cart_btn.click()

# Go to Cart
cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
cart_icon.click()

# Click Checkout
checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
checkout_btn.click()

# Ensure checkout page is loaded
wait.until(EC.presence_of_element_located((By.ID, "first-name")))

# Fill out checkout info
first_name_field = wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
first_name_field.send_keys("John")

last_name_field = wait.until(EC.visibility_of_element_located((By.ID, "last-name")))
last_name_field.send_keys("Doe")

postal_code_field = wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))
postal_code_field.send_keys("12345")

# Click Continue
continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
continue_btn.click()

# Optional: wait for overview page
wait.until(EC.presence_of_element_located((By.ID, "finish")))

# Click Finish
finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
finish_btn.click()

print("Checkout process automated successfully!")

# Close the browser
driver.quit()
