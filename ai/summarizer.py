
import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_article(title: str, link: str) -> str:
    """
    Generate an AI summary for a given article.
    """
    prompt = f"""
    Summarize the following tech article in 3 short bullet points.
    Keep it concise and clear.

    Title: {title}
    Link: {link}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content.strip()
