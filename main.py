from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import json

# Dictionary with the possible top lists for apps.
dic_top = {'paid': '/topselling_paid', 'free': '/topselling_free',
           'gross': '/topgrossing'}

base_url = 'https://play.google.com'

process = CrawlerProcess(get_project_settings())

f = open('categories.json')

categories = json.load(f)

for category in categories:
    for toplist in dic_top.values():
        crawl_url = base_url + category['url'] + '/collection' + toplist
        process.crawl('apps', start_urls=[crawl_url], category=category['title'])
        process.start()
        break
