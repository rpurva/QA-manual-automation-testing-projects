from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)
wait.until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
).click()

cart_count = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
).text

if cart_count == "1":
    print("PASS: Item added to cart")
else:
    print("FAIL: Cart not updated")

wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
).click()

time.sleep(2)
product_name = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
).text

print("Product in cart:", product_name)

if "Sauce Labs Backpack" in product_name:
    print("PASS: Correct product found in cart")
else:
    print("FAIL: Wrong or missing product")

time.sleep(3)
driver.quit()