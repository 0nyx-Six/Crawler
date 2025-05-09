# Crawler

A lightweight Python crawler for web scraping and data extraction, utilizing [Crawl4AI](https://docs.crawl4ai.com/) backend for ease of use for LLMs.

## Features

- **Web Crawling**: Fetch and parse web pages efficiently.
- **Data Extraction**: Downloads data in Markdon
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

 3. **Create urls.txt in the project folder.**  

## Usage

- **Crawl a single URL:**

  ```sh
  python crawl_single.py 
  ```
  You will receive a prompt for the URL. The output will be placed in markdown_downloads directory.

- **Crawl multiple URLs (from a file):**

  ```sh
  python crawl_all.py
  ```
  Paste your URLs in  urls.txt and save. The output will be placed in markdown_downloads directory.

- **Generate or parse a sitemap:**

  ```sh
  python sitemap.py
  ```
  You will receive a prompt for the URL. Copy output to crawl_all.py.


  **DISCLAIMER**
This project and its associated tools are provided for ethical purposes only. The maintainer is not responsible for how you use these tools or for any consequences arising from their use.

Please use these tools responsibly and ethically. Always adhere to the website's robots.txt file and respect the site's terms of service. Unauthorized scraping or misuse may violate laws or site policies.

By using this software, you agree to take full responsibility for your actions.
