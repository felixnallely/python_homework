#Task 3: Write a Program to Extract this Data
import pandas as pd 
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

time.sleep(3)

results_divs = driver.find_elements(By.CLASS_NAME, "cp-search-result-item-content")
print("Found results:", len(results_divs))

results = []

for div in results_divs: 
    title_elements = div.find_elements(By.CLASS_NAME, "cp-title-link")
    if len(title_elements) > 0: 
        title = title_elements[0].text.strip()
    else:
        title_elements = div.find_elements(By.CLASS_NAME, "cp-title")
        if len(title_elements) > 0:
            title = title_elements[0].text.strip()
        else:
            continue

    author_element = div.find_elements(By.CLASS_NAME, "cp-author-link")
    authors = "; ".join([a.text.strip() for a in author_element])

    format_elements = div.find_elements(By.CLASS_NAME, "cp-screen-reader-message")

    if len(format_elements) > 0:
        format_year_text = format_elements[0].text.strip()

        if "," in format_year_text:
            format_text, year_text = [x.strip() for x in format_year_text.split(",", 1)]
        else:
            format_text = format_year_text
            year_text = "Unknown"
    else: 
        format_text = "Unknown"
        year_text = "Unknown"
    
    format_year = f"{format_text} - {year_text}"
    
    results.append({
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    })

driver.quit()

df = pd.DataFrame(results)
print(df)

#Task 4: Write out the Data 
df.to_csv("get_books.csv", index=False)
print("CSV file created.")

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
print("JSON file Created.")