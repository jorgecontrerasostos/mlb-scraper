import scrapy


class MLBTeamsSpider(scrapy.Spider):
    name = "mlb_spider"
    allowed_domains = ["www.mlb.com"]
    teams: [str] = ['redsox', 'yankees', 'rays', 'orioles']
    start_urls = [f"https://www.mlb.com/{team}/roster" for team in teams]

    def parse(self, response):
        yield {
            "name": response.url.split("/")[-2],
            "players": response.css('td.info a::text').getall()
        }
