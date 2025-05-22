import time
from winreg import KEY_CREATE_SUB_KEY

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Test_Login.Registration import login_to_saucedemo

# Specify the path to the chromedriver executable
service = Service(executable_path=r"D:\edge_driver\edgedriver_win64\msedgedriver.exe")

# Initialize the WebDriver using the Service object
driver = webdriver.Edge(service=service)
driver.implicitly_wait(10)

# Login first
login_to_saucedemo(driver)

# Open the Saucedemo Inventory page
driver.get("https://www.saucedemo.com/inventory.html")
driver.maximize_window()

# Verify that products are displayed on the inventory page
try:
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    if len(products) > 0:
        print("Products are displayed correctly!")
    else:
        print("No products found on the page!")

    # Verify product details: name, price, and image
    for product in products:
        # Verify product name
        product_name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        print(f"Product Name: {product_name}")

        # Verify product price
        product_price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Product Price: {product_price}")

        # Verify product image
        try:
            product_image = product.find_element(By.CLASS_NAME, "inventory_item_img")
            image_url = product_image.get_attribute("src")
            print(f"Product Image URL: {image_url}")
        except:
            print("Product image is not displayed!")

except Exception as e:
    print(f"An error occurred: {e}")

# Close the browser
driver.quit()


