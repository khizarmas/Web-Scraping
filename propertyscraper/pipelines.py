# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class PricePipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['price'] = float(adapter['price'].replace(',',''))
        return item

class BedroomPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['bedrooms'] = int(adapter['bedrooms'])
        adapter['bath'] = int(adapter['bath'])
        return item

class AreaPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['area'] = float(adapter['area'].split()[0])
        return item

