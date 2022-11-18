import json

import scrapy


class PhoneItem(scrapy.Item):
    version = scrapy.Field()
    product_url = scrapy.Field()


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['ozon.by']
    start_urls = ['http://ozon.by/']
    os_list = []
    os_dict = {}

    def start_requests(self):
        phones = 0
        with open("test.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            for url in data:
                if phones < 101:
                    phones += 1
                    yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = PhoneItem()
        item['product_url'] = response.url
        item['version'] = response.xpath('//dl/dt/span/text() | '
                                         '//dl/dd/a/text() | '
                                         '//dl/dd/a/@href/text() | '
                                         '//dl/dd/text()').getall()
        for i in range(len(item['version'])):
            if item['version'][i][0:6] == 'Версия':
                self.os_list.append(item['version'][i + 1])
                yield item
