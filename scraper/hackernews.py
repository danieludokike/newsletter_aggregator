
import requests
from bs4 import BeautifulSoup


HACKERNEWS_URL = "https://news.ycombinator.com/"


def get_top_hackernews_articles(limit: int = 5) -> list[dict]:
    """
    Scrape top articles from Hacker News.

    Returns:
        List of dictionaries with 'title' and 'link'
    """
    response = requests.get(HACKERNEWS_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    items = soup.select(".athing")[:limit]

    for item in items:
        title_tag = item.select_one(".titleline a")
        if not title_tag:
            continue

        articles.append({
            "title": title_tag.text.strip(),
            "link": title_tag["href"]
        })

    return articles
