import time
from splinter import Browser
from bs4 import BeautifulSoup
<<<<<<< HEAD
import pandas as pd
=======
from selenium import webdriver
import pandas as pd
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

>>>>>>> 6b55f32cdec32ae98f31dd02beb9b85856006a68

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    # create mars news dict that we can insert into mongo
    mars_data = {}
    
    # visit mars.nasa.gov
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)

    html = browser.html
    
    # create a soup object from the html
    soup = BeautifulSoup(html, "html.parser")
    
    # find the first news item
    news_item = soup.find("li", {"class": "slide"})
    
    # get the title text
    item_title = news_item.find("div", {"class": "content_title"})
    item_title_text = item_title.find("a").getText()
    mars_data["News Headline"]=item_title_text

    # get the item paragraph
    item_para_text = news_item.find("div", {"class": "article_teaser_body"}).getText()
    mars_data["News Body"]=item_para_text

    # visit www.jpl.nasa.gov
    mars_jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_jpl_url)

    html = browser.html
    
    # create a soup object from the html
    soup = BeautifulSoup(html, "html.parser")
    article=soup.find("article", {"class": "carousel_item"})
      
    #find featured image url
    featured_image_url=article.find("a", {"class": "button fancybox"})['data-fancybox-href']
    mars_data["Featured Image URL"]=featured_image_url
        
    # visit twitter.com
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)

    html = browser.html
    
    # create a soup object from the html
    soup = BeautifulSoup(html, "html.parser")
    mars_weather=soup.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}).getText()
    mars_data["Mars Weather"]=mars_weather
 
    # visit space-facts.com/mars/
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)

    html = browser.html
    
    # create a soup object from the html
    soup = BeautifulSoup(html, "html.parser")
    mars_fact_frame=soup.findAll("ul")[6]
    mars_fact_list=mars_fact_frame.findAll("li")
    
    dfMarsFacts=pd.DataFrame()
    index=0
    
    # create dataframe to accept fact list
    for row in mars_fact_list:
        rowtag=row.find("strong").getText()
        #dfMarsFacts[row][0]=rowtag
        dfMarsFacts.at[index, 0] = rowtag
        index=index+1
        
    # Convert df to html table
    MarsFactsHTML = dfMarsFacts.to_html()
    mars_data["Facts HTML"]=MarsFactsHTML
    
    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        ]
    
    mars_data["Hemisphere Images"]=hemisphere_image_urls
    
<<<<<<< HEAD
    browser.quit()
    
    return(mars_data)
=======
    return(mars_data)

    browser.quit()
>>>>>>> 6b55f32cdec32ae98f31dd02beb9b85856006a68
