# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import csv

class FlowerIte(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()

class SitiodamataSpider(scrapy.Spider):
    custom_settings = {
        'FEED_FORMAT': csv
    }
    name = 'sitiodamata'
    allowed_domains = ['sitiodamata.com.br']
    start_urls = ['https://www.sitiodamata.com.br/especies-de-plantas?p=1']
    output = "output.csv"

    def __init__(self):
            open(self.output, "w").close()

    def parse(self, response):
        with open(self.output, "a") as f:
            writer = csv.writer(f, delimiter =';')
            writer.writerow(['Name', 'Description'])

            for flower in response.css('ul.products-grid>li.item'):
                item = {}
                item['name'] = flower.css('div.product-info>h2.product-name a::attr(title)').get().replace('\n', '').encode('cp1252')
                item['description'] = flower.css('div.product-info>div.short_description>div.texto::text').get().replace('\n', '').strip().encode('cp1252')
                writer.writerow([item['name'], item['description']])

                yield item

        next_page = response.xpath('//a[@class="next i-next fa fa-caret-right"]/@href').get()
        if next_page:
            yield Request(next_page)