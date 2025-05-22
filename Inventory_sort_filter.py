import time
from winreg import KEY_CREATE_SUB_KEY

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

def print_products(driver, count=5):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"Top {count} products:")
    for i, product in enumerate(products[:count], start=1):
        name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"{i}. {name} - {price}")
    print("-" * 40)

def select_sort_option(value):
    # Re-find the sort dropdown to avoid stale element reference
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value(value)
    time.sleep(2)  # wait for page to update

print("Sorting by Price: Low to High")
select_sort_option("lohi")
print_products(driver)

print("Sorting by Price: High to Low")
select_sort_option("hilo")
print_products(driver)

print("Sorting by Name: A to Z")
select_sort_option("az")
print_products(driver)

print("Sorting by Name: Z to A")
select_sort_option("za")
print_products(driver)

driver.quit()