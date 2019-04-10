# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import pymongo


class ZuopinjiPipeline(object):

    def process_item(self, item, spider):
        author_name = str(item['author_name'])
        book_name = str(item['book_name'])
        chapter_name = str(item['chapter_name'])
        chapter_content = str(item['chapter_content'])
        if not os.path.exists(author_name):
            os.makedirs(author_name)
        if not os.path.exists(author_name + os.path.sep + book_name):
            os.makedirs(author_name + os.path.sep + book_name)
        book_path = author_name + os.path.sep + book_name + os.path.sep + chapter_name + '.txt'
        with open(book_path, 'a', encoding='utf-8') as f:
            f.write(chapter_name + '\n\n\n')
            f.write(chapter_content + '\n\n\n')
            f.close()
        return item


class MongoPipeline(object):
    collection_name = 'author'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 更新及去重
        self.db[self.collection_name].update({'chapter_name': item['chapter_name']}, dict(item), True)
        return item


class RedisPipeline(object):

    def process_item(self, item, spider):
        return item
