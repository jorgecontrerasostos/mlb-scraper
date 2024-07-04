import scrapy


class MlbSpiderSpider(scrapy.Spider):
    name = "mlb_spider"
    allowed_domains = ["www.mlb.com"]
    start_urls = ["https://www.mlb.com/redsox/roster"]

    def parse(self, response):
        yield {
            "players": response.css('td.info a::text').getall()
        }
