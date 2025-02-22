import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ----- CONFIGURATION -----
FRAMER_PROJECT_URL = "https://framer.com/example"  # Replace with actual Framer URL
TOOL_URL = "https://nocodexport.com/tools/framer-to-html"
DOWNLOAD_DIR = "/path/to/your/download/folder"  # Change this to match your system's download folder
GITHUB_REPO_DIR = "/path/to/your/github/repo"
GITHUB_REPO = "your-username/your-repo"

# ----- SET UP SELENIUM (HEADLESS) -----
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without opening a browser
options.add_argument("--disable-gpu")  # Required for some headless systems
options.add_argument("--window-size=1920,1080")  # Avoid potential rendering issues
options.add_experimental_option("prefs", {"download.default_directory": DOWNLOAD_DIR})

driver = webdriver.Chrome(options=options)

try:
    # Step 1: Open the website
    driver.get(TOOL_URL)
    time.sleep(3)  # Allow time for the page to load

    # Step 2: Find the input field and paste the Framer project link
    input_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Framer URL']")
    input_field.send_keys(FRAMER_PROJECT_URL)

    # Step 3: Click the "Export HTML" button
    export_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Export HTML')]")
    export_button.click()

    time.sleep(10)  # Wait for the file to download (adjust if necessary)

    # Step 4: Find the most recently downloaded HTML file
    files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".html")]
    if not files:
        print("No HTML files found in download directory!")
        driver.quit()
        exit(1)

    latest_file = max(files, key=lambda f: os.path.getctime(os.path.join(DOWNLOAD_DIR, f)))
    downloaded_file_path = os.path.join(DOWNLOAD_DIR, latest_file)

    # Step 5: Move the file to the GitHub repo
    new_file_path = os.path.join(GITHUB_REPO_DIR, latest_file)
    os.rename(downloaded_file_path, new_file_path)

    # Step 6: Push to GitHub
    os.chdir(GITHUB_REPO_DIR)
    subprocess.run(["git", "add", latest_file])
    subprocess.run(["git", "commit", "-m", f"Added {latest_file}"])
    subprocess.run(["git", "push", "origin", "main"])  # Change branch if needed

    print(f"File {latest_file} uploaded to GitHub successfully!")

finally:
    driver.quit()  # Close the browser
