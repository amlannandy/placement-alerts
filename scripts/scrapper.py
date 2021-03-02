import requests
from bs4 import BeautifulSoup

URL = 'https://trident.ac.in/maintain/category/placement-notice/'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
articleTags = soup.find_all(name='article')

def extract_articles():
  articles = []
  for a in articleTags:
    titleTag = a.find('h1', class_='entry-title')
    title = titleTag.text
    url = titleTag.find('a')['href']
    content = a.find('p').text.split('… Continue reading')[0]
    article = {
      'title': title,
      'content': content,
      'url': url,
    }
    articles.append(article)
  return articles