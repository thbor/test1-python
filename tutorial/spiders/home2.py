

import scrapy
import sys
import time
import os
from scrapy.selector import Selector
from scrapy.http import Request
sys.path.append('..')
# from tutorial.items import TutorialItem
from scrapy import cmdline
#循環1到4頁數據
class Home2(scrapy.Spider):
    name = 'home2'
    start_urls = []
    url = "https://m.hndfbg.com/?mdid=6922&from=singlemessage"
    start_urls.append(url)
    def parse(self, response):
      items = []
      for ul in response.css('div.swiper-slide'):
        item = TutorialItem()
        item['image'] = ul.xpath('a/img/@src').get(),
        item['href'] = ul.xpath('a/@href').get(),
        item['name'] = ul.xpath('a[@class="gs-name text-over-two font14"]/text()').get(),
        item['cost'] = ul.xpath('span[@class="font14"]/text()').get()
        items.append(item)
        yield item
            # yield {
              
                # 'image': ul.xpath('div[has-class("p_img")]/a/img/@src').get(),
                # 'href': ul.xpath('div[has-class("p_productCN")]/a/@href').get(),
                # 'name': ul.xpath('div[has-class("p_productCN")]/a/text()').get(),
                # 'cost':ul.xpath('div[has-class("p_discount","commonFontPrice")]/text()').getall()
                # 'cost': quote.css('span.text::text').get(),
            # }
        #怎麼確定下一頁數據存不存在，如果最後一頁不確定呢？？？？
      for i in range(2, 5):  # 爬取第2，4页的数据
        url = "https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=" + str(i) + "&filters="
        yield Request(url, callback=self.parse)
    
    if __name__ == '__main__':
      while True:
        os.system("scrapy crawl home2")
        time.sleep(60)  #每隔一天运行一次 24*60*60=86400s