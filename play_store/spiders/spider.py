#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy

from play_store.items import PlayStoreApp, PlayStoreCategory

# The maximum number of records on the 'Top' lists.
MAX = 540

class AppSpider(scrapy.Spider):
    name = "apps"
    start_urls = ['https://play.google.com/store/apps/category/ANDROID_WEAR/collection/topgrossing']
    category = "Teste"

    rank = 0

    def parse(self, response):
        if not self.rank % 60 and self.rank != MAX:
            for href in response.xpath('//a[@class="title"]/@href').extract():
                item = PlayStoreApp()
                item['rank'] = self.rank + 1
                full_url = response.urljoin(href)
                request = scrapy.Request(full_url, callback=self.parse_app)
                request.meta['item'] = item
                self.rank += 1
                yield request
            url = response.urljoin("?start=" + str(self.rank))
            yield scrapy.Request(url)

    def parse_app(self, response):
        item = response.meta['item']

        item['title'] = response.xpath(
            '//div[@class="id-app-title"]/text()').extract()
        item['genre'] = response.xpath(
            '//span[@itemprop="genre"]/text()').extract()
        item['score'] = response.xpath(
            '//meta[@itemprop="ratingValue"]/@content').extract()
        item['reviews_num'] = response.xpath(
            '//meta[@itemprop="ratingCount"]/@content').extract()
        item['downloads'] = response.xpath(
            '//div[@itemprop="numDownloads"]/text()').extract()
        item['os'] = response.xpath(
            '//div[@itemprop="operatingSystems"]/text()').extract()

        yield item


class CategorySpider(scrapy.Spider):
    name = "categories"
    start_urls = ['https://play.google.com/store/apps/']
    category = ""

    def parse(self, response):
        # The way top lists work with age ranges are a bit different on the
        # link construction, I'll leave them out for now with not(contains).
        categories = response.xpath("//a[contains(@href, 'category') and \
                            not(contains(@href, '?')) and \
                            @class='child-submenu-link']")

        for category in categories:
            item = PlayStoreCategory()
            item['title'] = category.xpath("text()").extract()[0]
            item['url'] = category.xpath("@href").extract()[0]

            yield item
