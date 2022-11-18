import json
import scrapy


class Task3Item(scrapy.Item):
    page_url = scrapy.Field()
    product_url = scrapy.Field()


class PhoneItem(scrapy.Item):
    version = scrapy.Field()
    product_url = scrapy.Field()


def xor(first_condition, second_condition):
    return bool((first_condition and not second_condition) or (not first_condition and second_condition))


class CatalogSpider(scrapy.Spider):
    name = 'catalog'
    allowed_domains = ['ozon.by']
    start_urls = ['https://ozon.by/category/telefony-i-smart-chasy-15501/']
    pages_count = 200
    phones_count = 0
    phone_urls = []

    def start_requests(self):
        page = 0

        while self.phones_count < 101:
            page += 1
            # if page == 1:
            #     url = 'https://ozon.by/category/telefony-i-smart-chasy-15501/?sorting=rating'
            # else:
            #     url = f"https://ozon.by/category/telefony-i-smart-chasy-15501/?page={page}&sorting=rating"
            if page == 1:
                url = 'https://ozon.by/category/smartfony-15502/?sorting=rating'
            else:
                url = f"https://ozon.by/category/smartfony-15502/?page={page}&sorting=rating"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = Task3Item()
        item['page_url'] = response.url
        item['product_url'] = response.xpath('//a[@class="tile-hover-target ok9"]/@href').getall()

        for i in range(len(item['product_url'])):
            if item['product_url'][i][0:17] == '/product/smartfon':
                url = 'https://ozon.by' + item['product_url'][i]
                if url not in self.phone_urls:
                    self.phone_urls.append(url)
                    self.phones_count += 1

        with open("test.json", "w", encoding='utf-8') as file:
            json.dump(self.phone_urls, file)
