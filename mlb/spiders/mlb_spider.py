import scrapy


class MlbSpiderSpider(scrapy.Spider):
    name = "mlb_spider"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["http://www.mlb.com/"]

    def parse(self, response):
        pass
