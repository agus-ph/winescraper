import scrapy


class WinespiderSpider(scrapy.Spider):
    name = 'winespider'
    allowed_domains = ['storedevinos.com/']
    start_urls = ['https://www.storedevinos.com/']

    def parse(self, response,):

        wines = response.xpath("//div[contains(@class, 'item-inner')]")

        for wine in wines:
            wine_name = wine.xpath(
                ".//div[contains(@class, 'item-title')]/a/@title").extract_first()
            price = wine.xpath(
                ".//span[contains(@class, 'regular-price')]/span[contains(@class, 'price')]/text()").extract_first()
            desc = wine.xpath(
                ".//div[contains(@class, 'item-desc')]/text()").extract_first()
            img = wine.xpath(
                ".//div[contains(@class, 'item-image')]/a/img/@src").extract_first()

            yield {
                "wine_name": wine_name,
                "price": price,
                "desc": desc,
                "img": img,
            }
