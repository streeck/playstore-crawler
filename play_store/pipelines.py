# -*- coding: utf-8 -*-

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.contrib.exporter import JsonItemExporter
from datetime import date


class CategoryPipeline(object):

    def __init__(self, spider):
        if spider.name == 'categories':
            self.file = open('categories.json', 'wb')
            dispatcher.connect(self.spider_opened, signals.spider_opened)
            dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        if crawler.spider is not None:
            return cls(spider=crawler.spider)

    def spider_opened(self, spider):
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if spider.name == 'categories':
            self.exporter.export_item(item)
        return item


class AppsPipeline(object):

    def __init__(self, spider):
        self.file = open('{category}-{today}.json'.format(
            today=date.today().strftime('%d-%m-%Y'),
            category=spider.category), 'wb')
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        if crawler.spider is not None:
            return cls(spider=crawler.spider)

    def spider_opened(self, spider):
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        if spider.name == 'apps':
            self.exporter.export_item(item)
        return item
