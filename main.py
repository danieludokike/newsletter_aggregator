
from scraper.hackernews import get_top_hackernews_articles
from scraper.lobsters import get_top_lobsters_articles
from ai.summarizer import summarize_article
from emailer.send_email import send_newsletter


def build_newsletter() -> str:
    """
    Build the newsletter content.
    """
    content_lines = ["📰 Your Daily Tech Newsletter\n"]

    articles = []
    articles.extend(get_top_hackernews_articles())
    articles.extend(get_top_lobsters_articles())

    for idx, article in enumerate(articles[:5], start=1):
        summary = summarize_article(article["title"], article["link"])

        content_lines.append(f"{idx}. {article['title']}")
        content_lines.append(summary)
        content_lines.append(f"Read more: {article['link']}\n")

    return "\n".join(content_lines)


def main():
    newsletter_content = build_newsletter()
    send_newsletter(
        subject="📰 Your Daily Tech Newsletter",
        body=newsletter_content
    )
    print("Newsletter sent successfully!")


if __name__ == "__main__":
    main()
