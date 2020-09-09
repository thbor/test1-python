import scrapy
import re
from tutorial.TItem import TItem
from scrapy.http import Request
import json
import random
class test1(scrapy.Spider):
    name = 'test1'
    # allowed_domains = ['sklb.scu.edu.cn']
    start_urls = [
        'http://sklb.scu.edu.cn/notice?categoryId=&pageIndex=1&pageSize=1000',
        # 'http://sklb.scu.edu.cn/articles?categoryId=&pageIndex=1&pageSize=1000',
        # 'http://sklb.scu.edu.cn/f_articles.html',
    ]
    #获取每一链接的URL
    def parse(self, response):
        noticeIds = []
        t1 = json.loads(response.text)
        # print(t1)
        for item in t1['data']['entities']['result']:
            contentUrl='http://sklb.scu.edu.cn/noticeDetail?id='+str(item['id'])
            yield Request(contentUrl, callback=self.parse_content)
            # noticeIds.append(item['id'])
        # print(noticeIds)
    def parse_content(self,response):
        # print(response.text)
        result1 = json.loads(response.text)
        result = result1['data']['detail']['content']
        title = result1['data']['detail']['topic']
        print('============')
        print(title)
        print('============')
        # print(title)
        # result = result1['data']['detail']['content']
        # title = result1['data']['detail']['topic']
        # chapter_content_reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
        # chapter_content_2 = re.findall(chapter_content_reg, result, re.S)[0]
        # chapter_content_1 = chapter_content_2.replace('    ', '')
        # chapter_content = chapter_content_1.replace('<br />', '')
        item = TItem()
        item['content'] = result
        item['title'] = title
        yield item
     
