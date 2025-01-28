from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import json



url = 'http://www.imdb.com/chart/top'
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Request successful!")
    soup = BeautifulSoup(response.text, "html.parser")
    json_data = soup.find('script', type='application/ld+json').string
    data = json.loads(json_data)
    movie_list = []
    for item in data['itemListElement']:
        movie = item['item']
        movie_details = {
            "place": movie.get('position', 'N/A'),
            "movie_title": movie.get('name', 'N/A'),
            "rating": movie.get('aggregateRating', {}).get('ratingValue', 'N/A'),
            "year": movie.get('year', 'N/A'),  
            "star_cast": movie.get('cast', 'N/A'),  
        }
        movie_list.append(movie_details)
    
    for movie in movie_list:
        print(f"place: {movie['place']} - title: {movie['movie_title']} ({movie['year']}) - Rating: {movie['rating']}")
else:
    print(f"request failed, statuscode: {response.status_code}")

df = pd.DataFrame(movie_list)
df.to_csv('imdb_top_250_movies.csv',index=False)