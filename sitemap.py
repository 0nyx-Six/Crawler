import xml.etree.ElementTree as ET
import requests

# Prompt the user for the sitemap URL
sitemap_url = input("Enter the sitemap.xml URL: ").strip()
response = requests.get(sitemap_url)
urls = []
if response.status_code == 200:
    root = ET.fromstring(response.content)
    for url_elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is not None:
            urls.append(loc.text)
    print('\n'.join(urls))
else:
    print(f"Failed to fetch sitemap. Status code: {response.status_code}")

