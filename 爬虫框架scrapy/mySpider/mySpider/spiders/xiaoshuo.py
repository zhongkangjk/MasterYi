# -*- coding: utf-8 -*-
import scrapy
from myspider.items import MyspiderItem
from bs4 import BeautifulSoup

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['www.biqiuge8.com']
    start_urls = ['https://www.biqiuge8.com/book/4772/']
    


    def parse(self, response):
        chapter_list = response.xpath("//dd/a/@href").extract()
        for href in chapter_list:
            #item = {}
            url = 'https://www.biqiuge8.com' + href
            yield scrapy.Request(
                url,
                callback=self.parse_1,
                #meta = {"item":item},
                dont_filter=True
                )
    def parse_1(self, response):
        #item = response.meta["item"]
        soup = BeautifulSoup(response.text,"html.parser")
        title = soup.select('.content > h1:nth-child(1)')[0].text
        title1 = "\r\n\r\n\r\n\r\n\r\n    "+title+"\r\n\r\n\r\n\r\n    "
        text = soup.select('#content')[0].text.split("https")[0]
        text = '\r\n\r\n    '.join(text.split())
        item = MyspiderItem()
        item['title'] = title
        item['text']  = text
        yield item
        #href = soup.select('.page_chapter > ul:nth-child(1) > li:nth-child(3) > a:nth-child(1)')[0]['href']
        #if not href.endswith('/'):
            #next_url = 'https://www.biqiuge8.com' + href'''