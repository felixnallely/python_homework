#Task 1: Review robots.txt to Ensure Policy Compliance 
#This robots.txt allows all users to view the website and pages except the staff page. 
# There are also many bots that are not allowed.

#Task 2: Understanding HTML and the DOMM for the Durham Library Site 
#HTML for single search result(hint and li element): div "cp-search-result-item-info" 
#Element that stores title (tag/class value): h3 "cp-title"
# Author element (hint: a link): 
#Book format and year published: div "cp-format-info" span "display-info-primary"




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

#Step 1: Find result tags and class "cp-search=result-item-content"
results_divs = driver.find_elements(By.XPATH, ".//div[@class='cp-search-result-item-info']")
print("Found results:", len(results_divs))

results = []

for div in results_divs: 
    try: #Step 2: Find title tag with class "cp-title-link"
        title_element = div.find_element(By.XPATH, ".//h3[@class='cp-title']")
        title = title_element.text.strip()
    except:
        continue 

    #Step 3: find author tag and class "cp-author-link"
    author_elements = div.find_elements(By.XPATH, ".//span[@class='cp-author-link']")
    authors = ";".join(a.text.strip() for a in author_elements)

    #Step 4: <span> w class for format and year "cp-screen-reader-message"
    format_elements = div.find_elements(By.XPATH, ".//span[@class='cp-screen-reader-message']")

    if format_elements: 
        info = format_elements[0].text.strip()
        if "," in info:
            format_text, rest = [x.strip() for x in info.split(",", 1)]
        else:
            format_text = info
            rest = "Unknown"

        if "-" in rest:
            year_text = [x.strip() for x in rest.split("-", 1)] 
        else:
            year_text = rest
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