from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# constants
CHROME_DRIVER_PATH = "Your chorme webdriver path/location"
URL = "http://orteil.dashnet.org/experiments/cookie/"

# creating service object
service_obj = Service(executable_path=CHROME_DRIVER_PATH)
# creating driver object 
driver = webdriver.Chrome(service=service_obj)
# opening the website
driver.get(url=URL)

# Get cookie button
cookie_btn = driver.find_element(By.ID, "cookie")
# getting items upgrade name/id
store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# using list compression to create the list of id in decending order.
items_id = [n.get_attribute("id") for n in store_items[:-1]]

# amount of time the game will run
five_min_count = time.time() +5*60
# the time at which the program starts to execute
initial_time = time.time()

# using while loop to run program for desired amount of time.
while time.time() < five_min_count:
    # clicking the cookie button
    cookie_btn.click()
    # checking if the program is running to past 5 sec (to buy upgrades every 5 sec)
    if time.time() > initial_time+5:
        # getting money in real-time
        money = int((driver.find_element(By.ID, "money").text).replace(",", ""))
        # getting items upgrade price
        store_price = driver.find_elements(By.CSS_SELECTOR, "#store b")
        # using list compression to create the list of prices in decending order.
        items_price = [int(n.text.split("-")[-1].strip().replace(",", "")) for n in store_price[:-1]]   

        for price in items_price[::-1]:  # list slicing to run the loop in reverse.
            # checking the highest(most expensive) upgrade availabe with the current amount of money/cookies
            if money > price:
                # gettting the index to pass the index of items_price list to items_id list containig the id of the buttons            
                item_index = items_price.index(price)
                # pressing upgrade button
                driver.find_element(By.ID, items_id[item_index]).click()
                break  # this break function here is very import because we need to stop the loop after clicking the
                       # upgrade button, othewise it may break the program.
        initial_time = time.time() + 5

# printing the cookies per second which my program has achieved
cps = driver.find_element(By.ID, "cps").text
print(f"Your scoring rate is\n{cps}")


# to quit the program after the program completes.
driver.quit()
