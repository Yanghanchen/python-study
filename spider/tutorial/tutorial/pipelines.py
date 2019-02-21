# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pymongo

class TutorialPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip()+'...'
            return item
        else:
            return DropItem('Missing Text')

class MongoPipeline(object):
    def __init__(self):
        self.uri = "localhost"
        self.db = "tutorial"

    def open_spider(self,crawler):
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[self.db]
    
    def process_item(self,item,spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item
    
    def close_spider(self,spider):
        self.client.close()