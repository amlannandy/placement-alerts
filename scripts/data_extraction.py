import sys
sys.path.append('..')

from app import app
from scripts.scrapper import extract_articles
from helpers.send_email import send_article_email
from helpers.admin import save_article_from_json, find_by_title, fetch_all_user_emails, add_timestamp

def extract_data_from_source():
  with app.app_context():
    articles = extract_articles()
    user_emails = fetch_all_user_emails()
    count = 0
    for article in articles:
      in_db = find_by_title(article['title'])
      if not in_db:
        count += 1
        save_article_from_json(article)
        send_article_email(user_emails, article)
    add_timestamp(count)
    print(f'{count} new articles scrapped')
    return count