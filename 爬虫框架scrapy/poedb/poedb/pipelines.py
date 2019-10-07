# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class PoedbPipeline(object):
    def process_item(self, item, spider):
        with open("物品.txt", 'a', encoding='utf-8') as f:
            f.write(str(item)+',')
        print(item)
        return item
