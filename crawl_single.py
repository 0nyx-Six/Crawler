import asyncio
import os
import re
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def main():
    url = input("Enter the URL you want to crawl: ").strip()
    if not url:
        print("No URL provided. Exiting.")
        return

    # Set up browser and run configs
    browser_config = BrowserConfig(headless=True)
    run_config = CrawlerRunConfig(
        word_count_threshold=100,  # Set your threshold here
        # verbose=True  # DO NOT set verbose here; only in BrowserConfig if needed
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=url,
            config=run_config
        )

        os.makedirs("markdown_downloads", exist_ok=True)

        if result.success:
            filename = re.sub(r'[^\w\-_\. ]', '_', result.url)
            filepath = os.path.join("markdown_downloads", f"{filename}.md")
            with open(filepath, "w", encoding="utf-8") as md_file:
                md_file.write(result.markdown)
            print(f"Successfully crawled and saved: {result.url}")
        else:
            print(f"Failed to crawl: {result.url}")
            print(f"Error: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())
