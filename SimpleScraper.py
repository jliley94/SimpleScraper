import requests
from lxml import html


def ScrapeHTML(link, matchQuery):
    r = requests.get(link)
    if (r.status_code == 200):
        print("Success...")
        # print(r.text)
        tree = html.fromstring(r.text)
        # This returns an array of elements matching query
        return tree.xpath(matchQuery)
