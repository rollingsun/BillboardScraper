# -*- coding: utf-8 -*-
import scrapy


class BillboarderSpider(scrapy.Spider):
    name = "billboarder"
    start_urls = ['http://billboard.com/charts/hot-100']

    def parse(self, response):
        for i in xrange(0,99):
            dic= {
                'rank':response.css('div.container span.chart-row__current-week::text')[i].extract(),
                'last_week':response.css('div.container span.chart-row__last-week::text')[i].extract(),
                'song':response.css('div.container h2.chart-row__song::text')[i].extract(),
                'artist':response.css('div.container a.chart-row__artist::text')[i].extract()
            }
            yield dic
