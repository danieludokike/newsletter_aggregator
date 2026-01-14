# AI-Powered Personal Newsletter Aggregator

An automated Python application that scrapes top tech news articles from popular platforms, summarizes them using AI, and delivers a clean, readable newsletter directly to your email inbox.

This project demonstrates real-world usage of **web scraping, AI-powered text summarization, modular backend design, and email automation**.


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Use Cases](#use-cases)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Output](#example-output)
- [Error Handling](#error-handling)
- [Security Considerations](#security-considerations)
- [Extensibility](#extensibility)
- [Future Enhancements](#future-enhancements)
- [License](#license)


## Overview

The **AI-Powered Personal Newsletter Aggregator** is designed to help developers and tech enthusiasts stay informed without information overload.

Instead of manually browsing multiple websites, the application:
1. Scrapes top articles from trusted tech news platforms
2. Uses AI to summarize the most important points
3. Sends a well-formatted newsletter to your email

The system is modular, extensible, and suitable for production-level improvements.

## Features

- Scrapes top 5 trending articles from tech news websites
- AI-generated concise summaries for each article
- Automated email newsletter delivery
- Clean and modular project structure
- Environment-variable based configuration
- Easily extendable to additional platforms or delivery channels


## Tech Stack

| Component | Technology |
|--------|-----------|
| Programming Language | Python 3.10+ |
| Web Scraping | Requests, BeautifulSoup |
| AI Summarization | OpenAI API |
| Email Delivery | SMTP (smtplib) |
| Configuration | python-dotenv |

## Project Architecture

```newsletter_aggregator/
├── scraper/
│ ├── hackernews.py # Hacker News scraper
│ └── lobsters.py # Lobsters scraper
│
├── ai/
│ └── summarizer.py # AI summarization logic
│
├── emailer/
│ └── send_email.py # Email formatting & sending
│
├── main.py # Application entry point
├── requirements.txt
├── .env
└── README.md```


## Installation

### 1.  Clone the Repository
git clone https://github.com/danieludokike/newsletter_aggregator.git 
cd newsletter_aggregator

### 2. Create and Activate Virtual Environment
```python -m venv venv```
```source venv/bin/activate```    # Windows: ```venv\Scripts\activate```

### 3. Install Dependencies
```pip install -r requirements.txt```

## Configuration

Create a .env file in the project root directory and add the following:

OPENAI_API_KEY=your_openai_api_key
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_email_app_password
EMAIL_RECEIVER=receiver_email@gmail.com

## Notes

Use Gmail App Passwords instead of your main email password

Never commit .env files to version control

### Usage

Run the application using:

```python main.py```


The application will:

Scrape the latest articles

Generate AI summaries

Send a newsletter email to the configured recipient

### Example Output
#### Your Daily Tech Newsletter

1. OpenAI releases new reasoning model
. Improved inference speed
. Reduced cost per request
. Better alignment and safety

2. Rust adoption grows in backend systems
. Memory safety advantages
. Improved performance
. Expanding ecosystem

Read more using the links provided.

### Error Handling

Network failures are gracefully handled

API errors return meaningful messages

Email sending failures are logged

Empty article lists are safely ignored

## Security Considerations

Sensitive credentials are stored using environment variables

No hardcoded API keys or passwords

SMTP authentication uses secure SSL connection


## Future Enhancements

Daily or weekly scheduling

User preference-based topic filtering

Web UI for managing subscriptions

Caching and rate-limiting

Multi-language summarization

## License

This project is licensed under the MIT License.
You are free to use, modify, and distribute it.

## Acknowledgements

Hacker News

Lobsters

OpenAI