from pathlib import Path

import scrapy
from scrapy.loader import ItemLoader
from ..items import PropertyscraperItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["bayut.sa"]
    start_urls = [
        "https://www.bayut.sa/en/western-region/apartments-for-rent-in-jeddah/"
    ]


    def parse(self, response):
        items = PropertyscraperItem()
        properties = response.xpath('//*[@id="body-wrapper"]/main/div[2]/div[2]'
                                    '/div/div[2]/div[1]/div[2]/div/ul//*[@role="article"]')
        for property in properties:
            price_details = property.css('h4 span::text').getall()
            currency = price_details[0]
            price = price_details[1]
            frequency = price_details[2]
            location = property.css('h3::text').get()
            bedrooms = property.xpath('article/div[3]/div[2]/div[1]/div/span[2]/span[2]/text()').get()
            bath = property.xpath('article/div[3]/div[2]/div[1]/div/span[3]/span[2]/text()').get()
            area = property.xpath('article/div[3]/div[2]/div[1]/div/span[4]/span[2]/h4/text()').get()
            link = "www.bayut.sa" + property.xpath('article/div[1]/a').attrib['href']
            items['price'] = price
            items['currency'] = currency
            items['frequency'] = frequency
            items['location'] = location
            items['bedrooms'] = bedrooms
            items['bath'] = bath
            items['area'] = area
            items['link'] = link
            yield items
        next_page = response.xpath('//*[@id="body-wrapper"]/main/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/div[3]/ul/li//*[@title="Next"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)









