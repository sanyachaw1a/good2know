import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import fillerWords
from article import Article

# Calculate the dates for "today" and "yesterday"
yesterday = datetime.now() - timedelta(1)
yesterday_str = yesterday.strftime('/%Y/%B/%d/').lower()
today_str = datetime.now().strftime('/%Y/%B/%d/').lower()

punctuation_table = str.maketrans('', '', ',?.!"')

# Parse the HTML content of an article page and extract the URL and title
def parse(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('h1')
    if title_tag:
        title = title_tag.text.strip()
        title_words = set(
            word.translate(punctuation_table).lower().replace("'s", "") for word in title.split()
            if word.lower() not in fillerWords.filler_words
        )
    else:
        title = None
        title_words = set()

    # Extract the first image source if available
    img_tag = soup.find('img')
    picture_tag = soup.find('picture')
    if picture_tag:
        img_tag = picture_tag.find('img')

    img_src = img_tag['src'] if img_tag and 'src' in img_tag.attrs else None

    return url, title, title_words, img_src

# Get all the links on the page
all_urls = []
url = 'https://www.theguardian.com/international'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

def url_is_article(url):
    # Check if the URL contains today's or yesterday's date
    if url:
        if 'article' in url:
            return True
    return False

# Look for all of the <a> tags with an href value
for a in soup.find_all('a', href=True):
    href = a['href']
    if href and href[0] == '/':
        # Extends the shortened URLs to include the domain and protocol information
        href = 'https://www.theguardian.com' + href
    all_urls.append(href)

# Filter URLs to only include articles from today or yesterday
article_urls = [url for url in all_urls if url_is_article(url)]

# Scrape article data and create Article objects
articles = []
titles_seen = set()
for idx, article_url in enumerate(article_urls):
    article_data = requests.get(article_url).text
    url, title, title_words, img_source = parse(article_data, article_url)
    if title and title not in titles_seen:
        articles.append(Article('Guardian', idx + 1, url, title, title_words, img_source))
        titles_seen.add(title)

# Print the list of articles
for article in articles:
    print(article)


