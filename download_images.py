import os
import shutil
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from urllib.parse import urljoin, urlparse

BASE_URL = "https://www.mb-wensink.nl"
urls = [
        "https://www.mb-wensink.nl/mercedes-benz/a-klasse/250-e-amg-line/wensink-leeuwarden/detail/occ19147874",
        "https://www.mb-wensink.nl/mercedes-benz/a-klasse/180-luxury-line/wensink-nijmegen/detail/occ19138941?conpag=p000720"
    ]
target_html_element_id = "car-detail"
current_time = datetime.now().strftime("%Y%m%d%H%M%S")

# ANSI escape codes for text formatting
GREEN_BOLD = "\033[1;32m"  # Bold Green
RED_BOLD = "\033[1;31m"  # Bold Red
RESET_FORMAT = "\033[0m"  # Reset formatting

def download_images(driver, folder_path=f'images_{current_time}'):
    try:
        # Find the images div
        images_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, target_html_element_id))
        )

        # Find all image tags inside the main div with data-src attribute
        img_tags = images_div.find_elements(By.XPATH, './/img[contains(@data-src, "mercedes-occasions/") and (contains(@data-src, ".jpg") or contains(@data-src, ".png"))]')

        # Create a folder for the site
        site_folder = os.path.join(folder_path, os.path.basename(urlparse(driver.current_url).path))
        if not os.path.exists(site_folder):
            os.makedirs(site_folder)

        # Download images
        for img_tag in img_tags:
            img_url = img_tag.get_attribute('data-src')
            if img_url is not None:
                # Add base URL to the image path
                img_url = urljoin(BASE_URL, img_url)

                try:
                    img_data = requests.get(img_url).content

                    # Extract filename from the URL
                    filename = os.path.basename(urlparse(img_url).path)
                    img_path = os.path.join(site_folder, filename)

                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_data)

                    # Print the downloaded image path
                    print(f"Downloaded: {img_path}")

                except Exception as e:
                    print(f"{RED_BOLD}Failed to download {img_url}. Error: {e}{RESET_FORMAT}")

    except Exception as e:
        print(f"{RED_BOLD}Failed to download images from 'main' div. Error: {e}{RESET_FORMAT}")

def scrape_webpage(url, folder_path=f'images_{current_time}'):
    # Set up Selenium webdriver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        # Open the URL
        driver.get(url)

        # Download the images from the 'car-detail' div
        download_images(driver, folder_path)

        # Print success message after downloading images
        print(f"{GREEN_BOLD}Successfully downloaded images from: {url}{RESET_FORMAT}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    target_urls = urls

    for url in target_urls:
        scrape_webpage(url)

    # Print success message after all URLs are scraped
    print(f"{GREEN_BOLD}All urls are scraped!{RESET_FORMAT}")

    # Zip the 'images' folder with date and time in the filename
    zip_filename = f"images_{current_time}"
    shutil.make_archive(zip_filename, 'zip', f'images_{current_time}')

    # Print success message when zipping is done
    print(f"{GREEN_BOLD}Successfully zipped images!{RESET_FORMAT}")


    # Print final success message
    print(f"{GREEN_BOLD}Script finished successfully! Images are zipped to: {zip_filename}{RESET_FORMAT}")




