from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import matplotlib.pyplot as plt

def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-cache")
    options.add_argument("--disable-application-cache")
    options.add_argument("--incognito")  # Helps simulate cache-less state

    driver = webdriver.Chrome(options=options)
    return driver

def measure_browser_load_times(url, n):
    load_times = []

    for i in range(n):
        driver = setup_driver()  # New session simulates cleared cache
        try:
            print(f"Attempt {i + 1}...", end=' ')
            start = time.time()
            driver.get(url)
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

def plot_results(load_times, url):
    valid_times = [t for t in load_times if t is not None]
    mean_time = sum(valid_times) / len(valid_times) if valid_times else 0

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, len(load_times)+1), load_times, marker='o', color='blue')
    plt.axhline(y=mean_time, color='red', linestyle='--', label=f'Mean = {mean_time:.2f}s')
    plt.title(f"Browser Load Time Test for {url}")
    plt.xlabel("Attempt Number")
    plt.ylabel("Load Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f"\nMean Load Time: {mean_time:.2f} seconds")

# Example usage
url_to_test = "https://www.honuae.com"
num_attempts = 2

load_times = measure_browser_load_times(url_to_test, num_attempts)
plot_results(load_times, url_to_test)
