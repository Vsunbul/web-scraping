import scrapy

class AlintiSpiderSpider(scrapy.Spider):
    name = "alinti_spider"
    start_urls = ["https://quotes.toscrape.com/page/" + str(page_number) for page_number in range(1, 11)]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall()  # Fixed: added parentheses to call getall()
            }