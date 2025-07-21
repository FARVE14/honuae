"""

"""

__author__ = "Faisal Ahmed"

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

def setup_driver():
    """

    """
    chromedriver_autoinstaller.install()

    options = Options()
    options.add_argument("--headless=new")  # new headless mode is more stable
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    return driver


def measure_browser_load_time(
        host_url: str,
        no_of_attempts: int
) -> list[float]:
    """
    :param host_url:
    :param no_of_attempts:
    :return:
    """
    load_times = []
    for i in range(no_of_attempts):
        driver = setup_driver()  # New session simulates cleared cache
        try:
            print(f"Attempt {i + 1}...", end=' ')
            start = time.time()
            driver.get(host_url)
            driver.execute_script("return document.readyState")  # Ensure page is loaded
            load_time = time.time() - start
            load_times.append(load_time)
            print(f"Loaded in {load_time:.2f} seconds")
        except Exception as e:
            print(f"Error: {e}")
            load_times.append(None)
        finally:
            driver.quit()

    return load_times
