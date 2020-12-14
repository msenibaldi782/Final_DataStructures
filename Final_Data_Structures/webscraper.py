# -*- coding: utf-8 -*-
"""
Web Scraper

@author: Matt Senibaldi
6/21/2020

This Program is designed to pull information from Imodb website and put the movies into a neat list
"""

import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

headers = {"Accept-Language": "en-US, en;q=0.5"}
#Only allows for english translated headers

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv&ref=hackernoon.com" #Assigning the URL name to the actual URL
results = requests.get(url, headers=headers) #This is the variable the stores our request.get action
#and Requests.get is the method that pulls info from the URL
# Headers is just going to point to the English headers

soup = BeautifulSoup(results.text,"html.parser") #Now we are formatting the results of the Html to a desired format with soup

#print(soup.prettify()) #This prints the tree of information from that URL

#Creating empty lists for each bit of data

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')


for container in movie_div:
    #Name of movie
    name = container.h3.a.text
    titles.append(name)
    
    #Year Released
    year = container.h3.find('span', class_='lister-item-year').text
    years.append(year)
    
   # print(titles)
    
movies = pd.DataFrame({
    'Movie': titles,
    'Year': years,
    })
print(movies)  
    
    
    
    
   
    
    

    


