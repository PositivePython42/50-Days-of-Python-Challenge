import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.DataFrame.from_dict({
    "Year": [2009, 2002, 2009, 2010, 2009],
    "Title": ["Brothers", "spider-man", "Watchmen", "Inception", "Avatar"],
    "Genre": ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"]})

print(df)

url = "https://en.wikipedia.org/wiki/Python_(programming_language)#Typing"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
table = soup.find("table", {"class": "wikitable"})
df = pd.read_html(str(table))[0]

print(df)