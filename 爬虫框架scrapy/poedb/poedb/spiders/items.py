# -*- coding: utf-8 -*-
import scrapy


class ItemsSpider(scrapy.Spider):
    name = 'items'
    allowed_domains = ['poedb.tw/tw']
    start_urls = ['http://poedb.tw/tw/unique.php']

    def parse(self, response):
        chuanqi_list = response.xpath("//div[@class='panel-body']")[1].xpath(".//li/a")
        for chuanqi in chuanqi_list:
            item = {}
            #item["name"] = chuanqi.xpath("./text()").extract_first()
            item["href"] = chuanqi.xpath("./@href").extract_first()
            if item["href"] is not "unique.php?l=1":
                item["href"] = "http://poedb.tw/tw/" + item["href"]
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_1,
                    #meta = {"item":item},
                    dont_filter=True
                )
    def parse_1(self,response):
        #item = response.meta["item"]
        td_list = response.xpath("//tbody/tr/td[2]")
        item = {}
        for td in td_list:
            item["ch_name"]=td.xpath(".//a/text()").extract_first().split(" ")[0]
            item["en_name"] = td.xpath(".//span[@class='item_description']/text()").extract()[-1]
            yield item

