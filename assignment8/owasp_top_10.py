#Task 6: Scraping Structured Data
import pandas as pd 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/2021/")
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

items = driver.find_elements(By.XPATH, "//a[starts-with(@href, 'https://owasp.org/Top10/2021/A')]")

results = []
for item in items: 
    title = item.text.strip()
    link = item.get_attribute("href")

    results.append({
        "Title": title,
        "Link" : link
    })

driver.quit()

print(results)

df = pd.DataFrame(results)
df.to_csv("owasp_top_10.csv", index=False)
print("CSV File was Created.")
