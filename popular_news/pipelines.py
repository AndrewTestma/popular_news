# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PopularNewsPipeline:
    def process_item(self, item, spider):
        return item


class JiangshuSpiderPipeline(object):
    def open_spider(self, spider):
        self.file = open('jianshu.html', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(str(item['text']))