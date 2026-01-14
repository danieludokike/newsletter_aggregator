
import requests
from bs4 import BeautifulSoup


LOBSTERS_URL = "https://lobste.rs/"


def get_top_lobsters_articles(limit: int = 5) -> list[dict]:
    """
    Scrape top articles from Lobsters.

    Returns:
        List of dictionaries with 'title' and 'link'
    """
    response = requests.get(LOBSTERS_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    items = soup.select(".story")[:limit]

    for item in items:
        title_tag = item.select_one(".u-url")
        if not title_tag:
            continue

        articles.append({
            "title": title_tag.text.strip(),
            "link": title_tag["href"]
        })

    return articles
