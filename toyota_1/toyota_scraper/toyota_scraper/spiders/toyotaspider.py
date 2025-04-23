import scrapy


class ToyotaspiderSpider(scrapy.Spider):
    name = "toyotaspider"
    allowed_domains = ["tmcars.info"]
    start_urls = ["https://tmcars.info"]

    def parse(self, response):
        pass
