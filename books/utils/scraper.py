import re
import requests
from bs4 import BeautifulSoup


def url_scraper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {
        "title": soup.find('h1').text.strip(),
        "description": soup.find('div', {'id': "description"}).text.strip(),
        "author": soup.find('span', {"itemprop": "name"}).text.strip(),
        "rating": float(soup.find('span', {'itemprop': "ratingValue"}).text.strip()),
        "rating_count": int(soup.find('meta', {"itemprop": "ratingCount"})["content"]),
        "review_count": int(soup.find('meta', {"itemprop": "reviewCount"})["content"]),
        "page": int(re.findall(r'\d+', soup.find('span', {"itemprop": "numberOfPages"}).text)[0])
    }
    return data
