# <p align="center"> web-scraping-challenge</p>
## Objective:
  The goal of this assignment is to build a web application that scrapes various websites for data related to the Mission to Mars and display the information in a single HTML     page.
  
## Step 1 - Scraping: 
  Using Jupyter Notebook file called mission_to_mars.ipynb, initial scraping and analysis tasks was done.
    
### What was scraped?    
### NASA Mars News:
  Scraped the Mars News Site and collected the latest News Title and Paragraph Text. Then assigned the text to variables for future reference.
### Example:
        1. news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"
        2. news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg 
           Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."

> ### *Dynamic Content Scraping: Some of the content on the mars web pages used for scraping were renderred dynamically by Java Script. Selenium library was chosen over splinter as it was suggested by the instructor that selenium was the industry standard library to scrape dynamic content*          

### JPL Mars Space Images - Featured Image:
       
Featured Space Image URL was obtained by visiting the site. Used Selenium to navigate the site to find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

### Example:
  
  featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'

Found the full size .jpg image in sample variable and saved a complete url string for this image.

## Mars Facts:
Using Pandas, scraped the Mars Facts table by visiting the webpage and converted the data to a HTML table string.

### Mars Hemispheres:
Retrieved high resolution images for each of Mar's hemispheres from astrogeology site. Clicked each link of the hemispheres a found the image url to the full resolution image. Saved both the image url string for the full resolution hemisphere image, and the hemisphere title containing the hemisphere name. Used Python dictionary to store the data using the keys image_url and title.
Appended list dictionary with the image url string and the hemisphere title. The list now has one dictionary for each hemisphere.
### Example:
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]

## Step 2 - MongoDB And Flask Application:
#### Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the urls' mentioned above.
First, converted the Jupyter Notebook into a Pythin script called scrape_mars.py with a function called scrape that executed all of the scraped code from above and returned one Python dictionary containing all of the scraped data. Next, created a route called "/scrape" that imported scrape_mars.py script and return the scrape function. The returned value was stored in Mongo as Python dictionary. Then, created a root route called "/" that queried Mongo database and passed the mars data into the HTML template to display the data. Finally, created a template HTML file called "mission_to_mars.html" that can access mars data dictionary to display all of the data in the appropriate HTML elements. 

#### Screen shots

![The final application matched the homework instruction page.](https://github.com/jemiflor/web-scraping-challenge/blob/main/Screenshot_of_the_application.png)



  

            

