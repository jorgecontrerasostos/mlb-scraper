import scrapy


class StandingsSpider(scrapy.Spider):
    name = 'standings'
    allowed_domains = ['mlb.com']
    start_urls = ['https://www.mlb.com']

    def parse(self, response):
        pass
