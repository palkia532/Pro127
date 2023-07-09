from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/\Users\\pc\\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scrape = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        ## ADD CODE HERE ##
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        # Loop to find element using XPATH
        for ul_tag in soup.find_all("ul", attrs={"class", "wikitable"}):

            li_tags = ul_tag.find_all("li")
           
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:                   
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            scrape.append(temp_list)
    print(scrape[1])

        # Find all elements on the page and click to move to the next page
    browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()



        
# Calling Method    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "Radius", "Luminosity"]

# Define pandas DataFrame   
planet_df_1 = pd.DataFrame(scrape, columns=headers)

# Convert to CSV
planet_df_1.to_csv('scraped_data.csv',index=True, index_label="id")
    


