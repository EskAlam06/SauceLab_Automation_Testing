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

# Add some items to the cart for testing
def add_items_to_cart(driver, num_items=2):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for i in range(min(num_items, len(products))):
        add_button = products[i].find_element(By.XPATH, ".//button[contains(@id, 'add-to-cart')]")
        add_button.click()
        print(f"Added item {i + 1} to cart.")

add_items_to_cart(driver, num_items=2)

# Click the cart icon to view the cart
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()
time.sleep(2)  # wait for the cart page to load

# Verify items in the cart
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
print(f"Number of items in the cart: {len(cart_items)}")

print("Items in the cart:")
for i, item in enumerate(cart_items, start=1):
    item_name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
    print(f"{i}. {item_name}")

# Close browser
driver.quit()