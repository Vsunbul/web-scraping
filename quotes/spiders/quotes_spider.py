import scrapy
from pathlib import Path
from typing import Iterable

class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    
    def start_requests(self):
        urls = ["https://quotes.toscrape.com/page/1/",
                "https://quotes.toscrape.com/page/2/"]
    

        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)
    #allowed_domains = ["quotes.toscrape.com"]
    #start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        
        
        
        page = response.url.split("/")[-2]
        file_name = f"quotes{page}.html"

        Path(file_name).write_bytes(response.body)

        self.log("saved file{file_name}")