from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Get Devpost domain from user
devpost_domain = input("Enter your Devpost domain: ")

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver with options
driver = webdriver.Chrome(options=options)

# Function to extract data from a single page
def extract_data():
    projects = []
    items = driver.find_elements(By.CLASS_NAME, 'gallery-item')

    for item in items:
        try:
            name = item.find_element(By.TAG_NAME, 'h5').text
            description = item.find_element(By.CLASS_NAME, 'tagline').text
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            projects.append({"name": name, "description": description, "link": link})
        except:
            continue
    return projects

all_projects = []

# Loop through the pages
page_number = 1
start_time = time.time()
while True:
    url = f"https://{devpost_domain}.devpost.com/project-gallery?page={page_number}"
    driver.get(url)
    time.sleep(3)  # Wait for the page to load
    projects = extract_data()

    if not projects:
        break  # Exit the loop if no projects are found on the page

    all_projects.extend(projects)
    print(f"Page {page_number} scraped. {len(projects)} projects found.")
    page_number += 1

# Close the WebDriver
driver.quit()

# Save to CSV
df = pd.DataFrame(all_projects)
df.to_csv(f"{devpost_domain}_projects.csv", index=False)

# Calculate and print the execution time
end_time = time.time()
execution_time = end_time - start_time
print(f"Scraping completed. {len(all_projects)} projects found in {execution_time:.2f} seconds.")
