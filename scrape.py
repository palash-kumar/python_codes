from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions() # Create Chrome options
#options.add_argument("--headless") # Run Chrome in headless mode
chrome_driver = webdriver.Chrome(options=options)
#chrome_driver.get("https://daraz.com.bd/")
chrome_driver.get("https://daraz.com.bd/manual-juicers/") # Open the page from where to scrape data

# Then Copy the xpath of the element you want to scrape
# /html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]
time.sleep(10)
text_element = chrome_driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span[1]')
print(text_element.text)  # Print the text content of the element

#chrome_driver.maximize_window()

time.sleep(30)  # Wait for the page to load
