#!/usr/bin/env python
# coding: utf-8


#Dependencies

from webdriver_manager.chrome import ChromeDriverManager

# Using selenium industry standard as suggested
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time

from urllib.parse import urljoin

import pandas as pd


#Urls of page to be scraped

mars_web_site_url = "https://redplanetscience.com/"
mars_images_url = "https://spaceimages-mars.com/"
mars_facts_url = "https://galaxyfacts-mars.com/"
mars_hemisphere_images_site_url = "https://marshemispheres.com/"

# Initialize chrome web driver
driver = webdriver.Chrome(ChromeDriverManager().install()) 

# Retrieve page using Selenium and chrome driver

def get_page_source(url, delay):
    driver.get(url)
    # if dynamic content - better to wait for few seconds for the content to load
    if delay == True:
        time.sleep(5)        
    return driver.page_source


mars_web_site_response = get_page_source(mars_web_site_url, True)
mars_images_site_response = get_page_source(mars_images_url, True)
mars_facts_site_response = get_page_source(mars_facts_url, False)
mars_hemispheres_site_response = get_page_source(mars_hemisphere_images_site_url, False)


# ##### Create beautifulsoup objects by parsing with 'html.parser'

mars_web_site_soup = BeautifulSoup(mars_web_site_response, 'html.parser')
mars_images_site_soup = BeautifulSoup(mars_images_site_response, 'html.parser')
mars_facts_site_soup = BeautifulSoup(mars_facts_site_response, 'html.parser')
mars_hemispheres_site_soup = BeautifulSoup(mars_hemispheres_site_response, 'html.parser')


# ##### Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables for later reference

news_title = mars_web_site_soup.find_all('div', class_='content_title')[0].text.strip()
news_p = mars_web_site_soup.find_all('div', class_='article_teaser_body')[0].text.strip()


# ##### JPL Mars Space Images - Get current Featured Mars Image

featured_image_url = mars_images_site_soup.find_all('img', class_='headerimage fade-in')[0]['src']
featured_image_url = urljoin(mars_images_url,featured_image_url)


# ##### Scrape Mars Facts Using Pandas

mars_facts_html = pd.read_html(mars_facts_url)
mars_facts_df = mars_facts_html[0]

# ##### Pandas DataFrame To HTML Table String

html_table_string = mars_facts_df.to_html()

# ##### Mars Hemispheres

hemisphere_image_urls = []
mars_hemispheres_descriptions = mars_hemispheres_site_soup.find_all('div', class_='description')

for mars_hemispheres_description in mars_hemispheres_descriptions:
    mars_hemispheres_link = mars_hemispheres_description.find("a")
    hemisphere_page_url = urljoin(mars_hemisphere_images_site_url, mars_hemispheres_link['href'])
    title = mars_hemispheres_link.h3.text.strip()
    
    hemisphere_page_html = get_page_source(hemisphere_page_url, False)
    hemisphere_page_soup = BeautifulSoup(hemisphere_page_html, 'html.parser')
    
    downloads_div = hemisphere_page_soup.find("div", class_='downloads')
    
    hemisphere_full_res_img_url = downloads_div.find('ul').find('li', recursive = False).a['href']
    
    hemisphere_image_urls.append(dict({
        "title" : title,
        "img_url" : urljoin(mars_hemisphere_images_site_url ,hemisphere_full_res_img_url)
    }))
    
