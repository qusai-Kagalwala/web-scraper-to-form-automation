"""
Project: Zillow Scraper to Google Form Automation
Author: Qusai Kagalwala

Description:
This script performs two main tasks:
1. Scrapes property listings (links, addresses, prices) from a Zillow clone site.
2. Automatically fills and submits this data into a Google Form using Selenium.

Tech Stack:
- BeautifulSoup (HTML parsing)
- Requests (HTTP requests)
- Selenium (browser automation)
"""

# ------------------ IMPORTS ------------------ #

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ------------------ STEP 1: SCRAPING DATA ------------------ #

# Headers to mimic a real browser request
header = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

# Target website (Zillow clone)
URL = "https://appbrewery.github.io/Zillow-Clone/"

# Send GET request
response = requests.get(URL, headers=header)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract all property links
all_links = [
    link["href"]
    for link in soup.select(".StyledPropertyCardDataWrapper a")
]

# Extract all property addresses
all_addresses = [
    address.get_text().replace(" | ", " ").strip()
    for address in soup.select(".StyledPropertyCardDataWrapper address")
]

# Extract all property prices
all_prices = [
    price.get_text().replace("/mo", "").split("+")[0]
    for price in soup.select(".PropertyCardWrapper span")
    if "$" in price.text
]

# Debug check
print(f"Links: {len(all_links)}, Addresses: {len(all_addresses)}, Prices: {len(all_prices)}")


# ------------------ STEP 2: SELENIUM AUTOMATION ------------------ #

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)  # Keeps browser open after script ends

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Increase page load timeout to avoid crashes
driver.set_page_load_timeout(300)

# Explicit wait setup (better than sleep)
wait = WebDriverWait(driver, 20)

# Google Form URL (target)
FORM_URL = "https://forms.gle/ca9mjxuwEkGaq4of8"


# ------------------ STEP 3: LOOP THROUGH DATA ------------------ #

for n in range(len(all_links)):
    try:
        # Open Google Form
        driver.get(FORM_URL)

        # Wait until input fields are present
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))

        # Get all input fields
        inputs = driver.find_elements(By.XPATH, '//input[@type="text"]')

        # Assign fields (order matters!)
        address_input = inputs[0]
        price_input = inputs[1]
        link_input = inputs[2]

        # Fill the form
        address_input.send_keys(all_addresses[n])
        price_input.send_keys(all_prices[n])
        link_input.send_keys(all_links[n])

        # Locate and click submit button
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]')
            )
        )
        submit_button.click()

        print(f"✅ Submitted entry {n + 1}")

        # Delay to prevent rate limiting / blocking
        time.sleep(2)

    except Exception as e:
        print(f"❌ Error on listing {n}: {e}")
        continue


# ------------------ END ------------------ #
