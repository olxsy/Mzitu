# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Mzitu.items import MzituItem

class MzituSpider(CrawlSpider):
    name = 'mzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['http://www.mzitu.com/all/']

# href="http://www.mzitu.com/132145"
# http://i.meizitu.net/2013/08/1-130H9114214.jpg
    rules = (
        Rule(LinkExtractor(allow=r'www.mzitu.com/\d+'),callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'www.mzitu.com/\d+/\d+'),callback='parse_item', follow=True),
      #  Rule(LinkExtractor(allow=r'i.meizitu.net/\d+/\d+/\w+\.jpg'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = MzituItem()
        item['name'] = response.xpath('//div/h2/text()').extract()[0]
        item['imglink'] = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]

        yield item
        # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
