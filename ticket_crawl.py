import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

logger = logging.getLogger('seleniumwire')
logger.setLevel(logging.ERROR)  # Run selenium wire at ERROR level
options = webdriver.ChromeOptions()

options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option("excludeSwitches", ['enable-logging'])
options.add_argument("--log-level=3")
options.set_capability("browserVersion", "117")
options.add_argument(
    'user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36')

i = 1
if True:
    driver = webdriver.Chrome(options=options)
    driver.get("https://tickets.wiener-staatsoper.at/webshop/webticket/eventlist")
    # accept all cockies
    accept_all_cookies = driver.find_element(By.XPATH, "//button[@data-full-consent]")
    accept_all_cookies.click()
    # click "weiter" button
    weiter_button = driver.find_element(By.XPATH, "//a[@class='btn btn-default full-width']")
    weiter_button.click()
    # select date
    date = "November 28, 2024"
    date_container = driver.find_element(By.XPATH, f"//span[@class='icon-calender']")
    date_container.click()
    date_picker = driver.find_element(By.XPATH, f"//span[@aria-label='{date}']")
    date_picker.click()
    # select

    # driver.close()
    time.sleep(2)
