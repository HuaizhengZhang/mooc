# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mooc.items import MoocItem
class MoocSpider(CrawlSpider):
    
    name = 'mooc'
    allowed_domains = ['mooc.cn']
    start_urls = []

    for i in range(1,37):
        start_urls.append('http://www.mooc.cn/course/page/%d'%i)

    rules = [Rule(LinkExtractor(allow=['/.*\.html']),'parse_mooc')]
     

    def parse_mooc(self, response):
        mooc = MoocItem()
        moocs = []
        
        mooc['url'] = response.url
        ch_name = response.xpath("//h1/text()").extract()
        en_name = response.xpath("//div[@class='course_enname']/text()").extract()
        university = response.xpath("//h2[1]/text()").extract()
        time = response.xpath("//div[@class='coursetime']/text()").extract()
        desc = response.xpath("//div[@class='content-entry clearfix']/p[1]/text()").extract()

        mooc['ch_name'] = [m.encode('utf-8') for m in ch_name]
        mooc['en_name'] = [m.encode('utf-8') for m in en_name]
        mooc['university'] = [m.encode('utf-8') for m in university]
        mooc['time'] = [m.encode('utf-8') for m in time]
        mooc['desc'] = [m.encode('utf-8') for m in desc]

        moocs.append(mooc)
        
        
        return moocs
 
    
  