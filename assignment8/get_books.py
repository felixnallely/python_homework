#Task 1: Review robots.txt to Ensure Policy Compliance 
#This robots.txt allows all users to view the website and pages except the staff page. 
# There are also many bots that are not allowed.

#Task 2: Understanding HTML and the DOMM for the Durham Library Site 
#HTML for single search result(hint a li element): li class="row cp-search-result-item" 
#Element that stores title (tag/class value): h3 class="cp-title-link"
# Author element (hint: a link): a class="cp-author-link"
#Book format and year published:  span class="cp-screen-reader-message" (tried div "cp-format-info" span "display-info-primary")


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
    try: #Expand to load format/year
        div.click()
        time.sleep(0.5)
    except: 
        pass

    #Title 
    title_elements = div.find_elements(By.CLASS_NAME, "cp-title-link")
    if len(title_elements) > 0: 
        title = title_elements[0].text.strip()
    else:
        title_elements = div.find_elements(By.CLASS_NAME, "cp-title")
        if len(title_elements) > 0:
            title = title_elements[0].text.strip()
        else:
            continue

    #Author
    author_element = div.find_elements(By.CLASS_NAME, "cp-author-link")
    authors = "; ".join([a.text.strip() for a in author_element])

    #format/year
    try:
        info = div.find_element(By.CLASS_NAME, "display-info-primary").text.strip()
        if "," in info: 
            format_text, year_text = [x.strip() for x in info.split(",", 1)]
        else: 
            format_text = info
            year_text = "Unknown"
    except: 
        format_text = "Unknown"
        year_text = "Unknown" 

    format_year = f"{format_text} - {year_text}"
    
    results.append({
        "Title": title,
        "Author": authors,
        "Format-Year": format_year
    })
driver.quit()


#Task 4: Write out the Data
df = pd.DataFrame(results)
print(df)

#Task 4: Write out the Data 
df.to_csv("get_books.csv", index=False)
print("CSV file created.")

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)
print("JSON file Created.")