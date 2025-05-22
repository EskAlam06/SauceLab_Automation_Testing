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
# driver.maximize_window()


# Add individual item to the cart
def add_individual_item_to_cart(driver):
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    add_to_cart_button.click()
    print("First item added to the cart.")

# Add multiple items to the cart
def add_multiple_items_to_cart(driver, num_items=3):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    added_items = 0

    for i in range(min(num_items, len(products))):
        try:
            # Use relative XPath to get the button inside each product
            add_button = products[i].find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]")
            add_button.click()
            added_items += 1
            print(f"Item {i + 1} added to the cart.")
        except Exception as e:
            print(f"Could not add item {i + 1}: {e}")

    print(f"Total {added_items} items added to the cart.")

# Add a single item
add_individual_item_to_cart(driver)
time.sleep(2)

# Add multiple items
add_multiple_items_to_cart(driver, num_items=3)

# Verify cart item count
try:
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    print(f"Items in cart: {cart_count}")
except:
    print("Cart is empty!")

# Close the browser
driver.quit()