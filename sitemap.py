import xml.etree.ElementTree as ET
import requests

url = "https://swisskyrepo.github.io/sitemap.xml"
response = requests.get(url)
urls = []
if response.status_code == 200:
    root = ET.fromstring(response.content)
    for url_elem in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is not None:
            urls.append(loc.text)
    print('\n'.join(urls))

