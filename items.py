# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoocItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    ch_name = scrapy.Field()
    en_name = scrapy.Field()
    university = scrapy.Field()
    time = scrapy.Field()
    desc = scrapy.Field()
    
