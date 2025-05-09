import os, sys

# append 2 parent directories to sys.path to import crawl4ai
parent_dir = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
sys.path.append(parent_dir)

import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    # Initialize the AsyncWebCrawler
    async with AsyncWebCrawler(verbose=True) as crawler:
        # Load URLs from file
        with open('urls.txt', 'r') as f:
            urls = [line.strip() for line in f if line.strip()]

        # Set up crawling parameters
        word_count_threshold = 100

        # Run the crawling process for multiple URLs
        results = await crawler.arun_many(
            urls=urls,
            word_count_threshold=word_count_threshold,
            bypass_cache=True,
            verbose=True,
        )

        # Ensure "markdown_downloads" directory exists
        os.makedirs("markdown_downloads", exist_ok=True)

        # Process the results and save Markdown
        for result in results:
            if result.success:
                # Create a safe filename from the URL
                import re
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
