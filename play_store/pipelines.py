# -*- coding: utf-8 -*-

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher
from scrapy.contrib.exporter import JsonItemExporter


class CategoryPipeline(object):

    def __init__(self):
        self.file = open('categories.json', 'wb')
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

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
