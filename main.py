from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = 'http://www.imdb.com/chart/top'
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, "html.parser")

movies = soup.select('td.titleColumn')



