# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PopularNewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JianshuNews(scrapy.Item):
    auth = scrapy.Field()
    title = scrapy.Field()
    approval = scrapy.Field()
    read = scrapy.Field()
    comment = scrapy.Field()
