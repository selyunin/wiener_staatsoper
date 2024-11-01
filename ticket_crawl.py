import json
import logging
import time
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def read_credentials():
    current_dir = Path(__file__).parent
    credentials_file = current_dir / 'credentials.json'
    if not credentials_file.is_file():
        raise FileNotFoundError(f"Provide credentials in `{credentials_file}`")
    with credentials_file.open() as f:
        return json.load(f)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)-8s]: %(filename)s:%(lineno)d %(message)s',
        handlers=[
            logging.FileHandler(f'{Path(__file__).stem}.log', mode='w'),
            logging.StreamHandler(sys.stdout),
        ])
    logger = logging.getLogger(__name__)

    credentials = read_credentials()
    logger.info(f"{credentials=}")

    selenium_logger = logging.getLogger('selenium')
    selenium_logger.setLevel(logging.ERROR)  # Run selenium at ERROR level
    urllib_logger = logging.getLogger('urllib3')
    urllib_logger.setLevel(logging.ERROR)
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
    options.set_capability("browserVersion", "129")
    options.add_argument(
        'user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36')

    driver = webdriver.Chrome(options=options)
    driver.get("https://tickets.wiener-staatsoper.at/webshop/webticket/eventlist")
    # accept all cookies
    accept_all_cookies = driver.find_element(By.XPATH, "//button[@data-full-consent]")
    accept_all_cookies.click()
    # click "weiter" button
    weiter_button = driver.find_element(By.XPATH, "//a[@class='btn btn-default full-width']")
    weiter_button.click()
    # login
    login_link = driver.find_element(By.XPATH, "//a[@id='nav_login']")
    login_link.click()

    email_input = driver.find_element(By.XPATH, "//input[@id='username']")
    email_input.send_keys(credentials['email'])

    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys(credentials['password'])

    login_button = driver.find_element(By.XPATH, "//button[@value='emailpasswort']")
    login_button.click()

    # select date
    date = "November 28, 2024"
    date_container = driver.find_element(By.XPATH, f"//span[@class='icon-calender']")
    date_container.click()
    date_picker = driver.find_element(By.XPATH, f"//span[@aria-label='{date}']")
    date_picker.click()
    # select

    # driver.close()
    time.sleep(2)
