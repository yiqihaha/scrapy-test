# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MyprojectItem 


class MydomainSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['linux.cn']
    start_urls = ['https://linux.cn/index.php']

    def parse(self, response):
        item = MyprojectItem()
        item['name']=response.xpath('//title/text()').extract()
        return item
