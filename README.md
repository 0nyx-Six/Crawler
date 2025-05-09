# Crawler

A lightweight Python crawler for web scraping and data extraction.

## Features

- **Web Crawling**: Fetch and parse web pages efficiently.
- **Single & Batch Processing**: Includes scripts for crawling a single URL (`crawl_single.py`) and multiple URLs (`crawl_all.py`).
- **Sitemap Support**: Generate and parse sitemaps (`sitemap.py`).
- **Easy Setup**: Minimal dependencies (see `requirements.txt`).

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/0nyx-Six/Crawler.git
   cd Crawler
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

- **Crawl a single URL:**

  ```sh
  python crawl_single.py 
  ```
  You will receive a prompt for the URL.

- **Crawl multiple URLs (from a file):**

  ```sh
  python crawl_all.py
  ```
Make a urls.txt in your project folder. Paste your URLs in the .txt and save.

- **Generate or parse a sitemap:**

  ```sh
  python sitemap.py
  ```
You will receive a prompt for the URL.
