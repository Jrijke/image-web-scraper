# Web Scraping Script Readme

## Description
This Python script is designed for web scraping images from specific URLs on the website "https://www.mb-wensink.nl." It utilizes the Selenium WebDriver to navigate the web pages and download images associated with Mercedes-Benz car details. The script organizes the downloaded images into folders based on the car details and creates a zip archive containing all the images.

## Dependencies
The script relies on the following Python libraries, which need to be installed before running the script:
- `os`: Operating system-specific functionality.
- `shutil`: High-level file operations.
- `datetime`: Provides date and time-related functionality.
- `selenium`: A web testing library.
- `requests`: HTTP library for making requests.
- `urllib.parse`: URL parsing and manipulation.

Ensure these dependencies are installed using the following command:
```bash
pip install os shutil datetime selenium requests urllib
# image-web-scraper
