# -*- coding: utf-8 -*-
import scrapy


class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['poedb.tw/tw']
    start_urls = ['http://poedb.tw/tw/unique.php?cn=Claw']

    def parse(self, response):
        #处理start
        #ch_name = response.xpath("//tbody/tr/td[2]/a/text()").extract()
        #print(ch_name)
        td_list = response.xpath("//tbody/tr/td[2]")
        for td in td_list:
            item = {}
            item["ch_name"]=td.xpath(".//a/text()").extract_first().split(" ")[0]
            item["en_name"] = td.xpath(".//span[@class='item_description']/text()").extract()[-1]
            #print(item)
            yield item
