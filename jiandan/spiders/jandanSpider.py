# coding:utf-8
import scrapy
from jiandan.items import JiandanItem

from scrapy.crawler import CrawlerProcess


class jiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    start_urls = ["http://www.meizitu.com/"]

    def parse(self, response):
        item = JiandanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        yield item
        counter = 2;
        n = 90;
        while counter <= n:
            new_url = "http://www.meizitu.com" + "/a/more_"+ str(counter) +".html";
            # print 'new_url',new_url
            if new_url:
                yield scrapy.Request(new_url, callback=self.parse)