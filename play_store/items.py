# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayStoreItem(scrapy.Item):
    title = scrapy.Field()
    genre = scrapy.Field()
    score = scrapy.Field()
    reviews_num = scrapy.Field()
    downloads = scrapy.Field()
    os = scrapy.Field()
    pass
