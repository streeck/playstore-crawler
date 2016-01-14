import scrapy

from play_store.items import PlayStoreItem

MAX = 540

class PlayStoreSpider(scrapy.Spider):
    name  = "playstore"
    start_urls = ['https://play.google.com/store/apps/category/GAME/collection/topselling_free']

    start = 0

    def parse(self, response):
        if self.start < MAX:
            for href in response.xpath('//a[@class="title"]/@href').extract():
                full_url = response.urljoin(href)
                yield scrapy.Request(full_url, callback=self.parse_app)
            self.start += 60
            url = response.urljoin("?start=" + str(self.start))
            yield scrapy.Request(url)

    def parse_app(self, response):
        item = PlayStoreItem()

        item['title'] = response.xpath('//div[@class="id-app-title"]/text()').extract()
        item['genre'] = response.xpath('//span[@itemprop="genre"]/text()').extract()
        item['score'] = response.xpath('//meta[@itemprop="ratingValue"]/@content').extract()
        item['reviews_num'] = response.xpath('//meta[@itemprop="ratingCount"]/@content').extract()
        item['downloads'] = response.xpath('//div[@itemprop="numDownloads"]/text()').extract()
        item['os'] = response.xpath('//div[@itemprop="operatingSystems"]/text()').extract()

        yield item
