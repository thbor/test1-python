

import scrapy
from scrapy.selector import Selector
from scrapy.http import Request

#循環1到4頁數據
class Home(scrapy.Spider):
    name = 'home'
    start_urls = []
    url = "https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=1&filters="
    start_urls.append(url)
    def parse(self, response):
        for ul in response.css('div.p_cont'):
            yield {
                'image': ul.xpath('div[has-class("p_img")]/a/img/@src').get(),
                'href': ul.xpath('div[has-class("p_productCN")]/a/@href').get(),
                'name': ul.xpath('div[has-class("p_productCN")]/a/text()').get(),
                # 'cost':ul.xpath('div[has-class("p_discount","commonFontPrice")]/text()').getall()
                # 'cost': quote.css('span.text::text').get(),
            }
        #怎麼確定下一頁數據存不存在，如果最後一頁不確定呢？？？？
        for i in range(2, 5):  # 爬取第2，4页的数据
            url = "https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=" + str(i) + "&filters="
            yield Request(url, callback=self.parse)