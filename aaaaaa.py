from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://localhost:8000/geolocation.html")

# Wait for the page to load
time.sleep(5)  # Adjust the sleep time as needed

while True:
    location = driver.execute_script("return currentLocation;")
    print(location)
    time.sleep(5)  # Adjust the interval for updating location

driver.quit()
