import scrapy


class MLBTeamsSpider(scrapy.Spider):
    name = "active_roster_spider.py"
    allowed_domains = ["www.mlb.com"]
    teams: [str] = [
        "redsox",
        "yankees",
        "rays",
        "orioles",
        "bluejays",
        "whitesox",
        "guardians",
        "tigers",
        "royals",
        "twins",
        "astros",
        "angels",
        "athletics",
        "mariners",
        "rangers",
        "braves",
        "marlins",
        "mets",
        "phillies",
        "nationals",
        "cubs",
        "reds",
        "brewers",
        "pirates",
        "cardinals",
        "dbacks",
        "rockies",
        "dodgers",
        "padres",
        "giants",
    ]
    start_urls = [f"https://www.mlb.com/{team}/roster" for team in teams]

    def parse(self, response):
        yield {
            "name": response.url.split("/")[-2],
            "players": response.css("td.info a::text").getall(),
        }
