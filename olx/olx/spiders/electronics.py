from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ElectronicsSpider(CrawlSpider):
    name = "electronics"
    allowed_domains = ["www.olx.com.br"]
    start_urls = [
        'http://sc.olx.com.br/eletronicos-e-celulares',
        'http://sc.olx.com.br/veiculos-e-pecas',
        'http://sc.olx.com.br/para-a-sua-casa'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
