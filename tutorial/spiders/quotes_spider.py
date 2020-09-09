
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=1&filters=',
            'https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=2&filters=',
         
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)