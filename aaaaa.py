from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(options=options)
    driver.get("https://mycurrentlocation.net/")

    # Wait for the page to load for 6 seconds
    time.sleep(6)
    
    # Scroll to the "Detect My Location" button
    detect_button = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/div[1]/div/div[1]/div/button')
    driver.execute_script("arguments[0].scrollIntoView();", detect_button)
    
    # Click the button using JavaScript
    driver.execute_script("arguments[0].click();", detect_button)
    
    # Wait for a few seconds to allow the location to be detected
    time.sleep(5)
    
    # Find latitude and longitude elements within the loaded web page
    latitude_element = driver.find_element(By.ID, 'latitude')
    longitude_element = driver.find_element(By.ID, 'longitude')
    
    # Get the text (latitude and longitude values) from these elements
    latitude = latitude_element.text
    longitude = longitude_element.text
    
    driver.quit()
    
    return (latitude, longitude)

print(getLocation())

