# SauceLab_Automation_Testing

## 📋 Project Description
This project contains Selenium WebDriver test scripts to automate and verify various functionalities on the SauceDemo website.

---

## 🧪 List of Automated Test Cases

1. **Login to SauceDemo**  
   - Uses a helper function to log in with valid credentials.

2. **Product Verification** 
   - User can Verify that products are displayed on the inventory page.

3. **Inventory Sorting**
   - Sorting the inventory by price ( Low to High , High to Low) & Sorting by name ( A-Z, Z-A).

4. **Cart Details**
    - Uses can verify item count in cart.

5. **Add/Remove/View Product to Cart**  
   - Adds/Remove/View the first available product from the inventory page to the shopping cart.

6. **Navigate to Cart and Checkout**  
   - Opens the cart and initiates the checkout process.

7. **Enter Checkout Information**  
   - Fills in user data: First Name, Last Name, and Postal Code.

8. **Complete Purchase**  
   - Proceeds through checkout and clicks the “Finish” button to complete the purchase.

---

## 🛠️ Tools and Technologies Used

- **Python 3.x**
- **Selenium WebDriver**
- **Microsoft Edge WebDriver**
- **PyCharm IDE**
- **WebDriverWait & Explicit Waits** for stable element interactions
- **Page Object Pattern** (partially implemented)

---

## 🧾 Test Data

- **Username**: `standard_user`
- **Password**: `secret_sauce`
- **First Name**: John
- **Last Name**: Doe
- **Postal Code**: 12345

---


## How to Run the Project

1. Prerequisites

 • Python installed (preferably Python 3.7+)

 • Selenium package installed (pip install selenium)

 • Microsoft Edge browser installed

 • Edge WebDriver downloaded and its path correctly set in each script (e.g., D:\edge_driver\edgedriver_win64\msedgedriver.exe)

 • Ensure the Test_Login/Registration.py module with the login_to_saucedemo(driver) function is in your project folder

2. Running Tests
  • Open a terminal or command prompt in your project directory
  • Run each test script individually using Python.

  Each Script Will-
  • Launch Microsoft Edge browser
  • Perform login automatically via login_to_saucedemo(driver)
  • Execute the respective tests
  • Close the browser upon completion



## 🚫 Limitations / Notes

- This script is built specifically for the SauceDemo test site and may not work on other domains.
- Assumes the inventory page always loads the same items in the same order.
- Designed for demo and educational purposes.
- The script currently uses hardcoded test data.

---


## 🙌 Acknowledgements
Thanks to Sauce Labs for providing a public practice platform for automation testers.

---

## 📄License

This project is licensed under the MIT License.



