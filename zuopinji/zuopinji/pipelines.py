# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


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
