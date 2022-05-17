from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# constants
CHROME_DRIVER_PATH = "/Users/amaansaifi/Documents/Programs - P/chromed/chromedriver"
URL = "http://orteil.dashnet.org/experiments/cookie/"


service_obj = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service_obj)
driver.get(url=URL)

# Get cookie to click on.
cookie_btn = driver.find_element(By.ID, "cookie")
# getting items upgrade name
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [n.get_attribute("id") for n in store_items[:-1]]


five_min_count = time.time() +5*60

initial_time = time.time()

while time.time() < five_min_count:
    cookie_btn.click()
    # checking which is the biggest upgrade available
    if time.time() > initial_time+5:
        # getting money in real-time
        money = int((driver.find_element(By.ID, "money").text).replace(",", ""))
        # getting items upgrade price
        store_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        items_price = [int(n.text.split("-")[-1].strip().replace(",", "")) for n in store_price[:-1]]

        for price in items_price[::-1]:
            if money > price:
                item_index = items_price.index(price)
                # pressing upgrade button
                driver.find_element(By.ID, items_id[item_index]).click()
                break  # this break function here is very import because we need to stop the loop after clicking the
                       # upgrade button, othewise it may break the program.
        initial_time = time.time() + 5


cps = driver.find_element(By.ID, "cps").text
print(f"Your scoring rate is\n{cps}")



driver.quit()