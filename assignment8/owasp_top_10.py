#Task 6: Scraping Structured Data
import pandas as pd 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")
time.sleep(3)

#load page 2 (that contains the list)
link2 = driver.find_element(By.XPATH, "//a[contains(text(), '2021')]").get_attribute("href")

driver.get(link2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

items = driver.find_elements(By.XPATH, "//ol/li/a")

results = []
for item in items: 
    title = item.text.strip()
    link = item.get_attribute("href")

    results.append({
        "Title": title,
        "Link" : link
    })

driver.quit()

#Save to df
df = pd.DataFrame(results)
print(df)

df.to_csv("owasp_top_10.csv", index=False)
print("CSV File was Created.")
