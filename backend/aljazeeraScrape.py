import requests 
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import fillerWords
from article import Article

# Calculate the dates for "today" and "yesterday"
today = datetime.now()
yesterday = today - timedelta(1)
today_str = today.strftime('%Y/%m/%d')
yesterday_str = yesterday.strftime('%Y/%m/%d')

# Function to remove leading zeros from the date parts
def strip_leading_zeros(date_str):
    parts = date_str.split('/')
    parts[1] = parts[1].lstrip('0')  # for month
    parts[2] = parts[2].lstrip('0')  # for day
    return '/'.join(parts)

# Strip leading zeros from the date strings
yesterday_str = strip_leading_zeros(yesterday_str)
today_str = strip_leading_zeros(today_str)

punctuation_table = str.maketrans('', '', ',?.!:;"')

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
    
    first_figure_tag = soup.find('figure', class_='article-featured-image')
    if first_figure_tag:
        img_tag = first_figure_tag.find('img')
        if img_tag and 'src' in img_tag.attrs:
            img_src = 'https://www.aljazeera.com' + img_tag['src']
        else:
            img_src = None
    else:
        img_src = None

    return url, title, title_words, img_src

# Check if the URL is an article from today or yesterday and contains '/news/'
def url_is_article(url):
    if url:
        if '/news/' in url and (today_str in url or yesterday_str in url):
            return True
    return False

# Get all the links on the Al Jazeera website
all_urls = []
url = 'https://www.aljazeera.com'
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

# Extract URLs from <a> tags
for a in soup.find_all('a', href=True):
    href = a['href']
    if href and href[0] == '/':
        # Extend shortened URLs to include the domain and protocol information
        href = 'https://www.aljazeera.com' + href
    all_urls.append(href)

# Filter URLs to only include articles from today or yesterday
article_urls = [url for url in all_urls if url_is_article(url)]

# Remove duplicate URLs
article_urls = list(set(article_urls))

# Scrape article data and create Article objects
articles = []
titles_seen = set()
for idx, article_url in enumerate(article_urls):
    article_data = requests.get(article_url).text
    url, title, title_words, img_source = parse(article_data, article_url)
    if title and title not in titles_seen:
        articles.append(Article('Al Jazeera', idx + 1, url, title, title_words, img_source))
        titles_seen.add(title)

# Print the list of articles
for article in articles:
   print(article)
