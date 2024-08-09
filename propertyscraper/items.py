# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyscraperItem(scrapy.Item):
    # define the fields for your item here like:
    price = scrapy.Field()
    location = scrapy.Field()
    bedrooms = scrapy.Field()
    bath = scrapy.Field()
    area = scrapy.Field()
    frequency = scrapy.Field()
    link = scrapy.Field()
    currency = scrapy.Field()
