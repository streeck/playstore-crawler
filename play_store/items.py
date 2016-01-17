# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class PlayStoreApp(Item):
    rank = Field()
    title = Field()
    genre = Field()
    score = Field()
    reviews_num = Field()
    downloads = Field()
    os = Field()


class PlayStoreMovie(Item):
    title = Field()
    date = Field()
    genre = Field()
    duration = Field()
    actors = Field()
    director = Field()
    score = Field()
    reviews_num = Field()
    purchase_price = Field()
    rent_price = Field()
    audio = Field()
    subtitles = ()
    content_rating = Field()
