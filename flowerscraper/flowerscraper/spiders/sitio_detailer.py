# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import csv

class SitioDetailerSpider(scrapy.Spider):
    # custom_settings = { 'FEED_FORMAT': csv }
    name = 'sitio-detailer'
    allowed_domains = ['sitiodamata.com.br']
    start_urls = ['https://www.sitiodamata.com.br/especies-de-plantas?p=1']
    output = "output.csv"

    def __init__(self):
        # open(self.output, "w").close()
        # with open(self.output, "a") as f:
            FIELDS = ['Nome popular', 'Nome científico', 'Família', 'Origem', 'Época da semeadura',
            'Instrução de semeadura', 'Tempo para germinação', 'Colheita', 'Sementes por envelope', 'Peso envelope',
            'Ciclo de vida', 'Folha', 'Crescimento da planta', 'Quando da frutos', 'Frutos', 'Quando da flores',
            'Flores', 'Como adubar', 'Como regar', 'Clima nativo', 'Aceita poda', 'Vai na sombra', 'Vai bem com outras plantas',
            'Altura das mudas', 'Atrai passaros', 'Atrai borboletas', 'Formigas matam', 'Pragas', 'Mais informações']

            # writer = csv.writer(f, delimiter =';')
            # writer.writerow(FIELDS)

    def parse(self, response):
        for flower in response.css('ul.products-grid>li.item'):
            url = flower.css('div.product-info>h2.product-name a::attr(href)').get()
            yield scrapy.Request(url=url, callback=self.parse_flower)

            next_page = response.xpath('//a[@class="next i-next fa fa-caret-right"]/@href').get()
            # if next_page:
            #     yield Request(next_page)



    def parse_flower(self, response):
        firstfield = response.css('#product_tabs_adicional4_contents>p>strong::text').get()

        if (firstfield == 'Nome popular:'):
            ps = {}

            flowers = response.css('#product_tabs_adicional4_contents>p').getall()
            # details = response.css('#product_tabs_adicional4_contents>p::text').getall()
            # details = [detail.strip().replace('\u', '').encode('cp1252') for detail in details]
            # with open(self.output, "a") as f:
            #     writer = csv.writer(f, delimiter =';')
            #     writer.writerow(details)

        # yield