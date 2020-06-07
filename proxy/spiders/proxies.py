# -*- coding: utf-8 -*-
import scrapy


class ProxiesSpider(scrapy.Spider):
    name = 'proxies'
    allowed_domains = ['https://ipinfo.io/']
    start_urls = ['http://https://ipinfo.io//']

    def parse(self, response):
        pass
