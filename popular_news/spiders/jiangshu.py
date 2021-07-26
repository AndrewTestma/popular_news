import scrapy

from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import JianshuNews


class JiangshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/techareas/backend']
    rules = (
        Rule(LinkExtractor(allow=r'/p/\d+', ), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        item = JianshuNews()
        item['title'] = soup(class_='_1RuRku')
        item['auth'] = soup(class_='_1OhGeD')
        return item

