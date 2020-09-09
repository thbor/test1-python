

# import scrapy
# from scrapy.selector import Selector
# from scrapy.http import Request

# #循環1到4頁數據
# class Story(scrapy.Spider):
#     name = 'story'
#     start_urls = []
#     url = "https://www.230book.com/book/12170/"
#     start_urls.append(url)
#     def parse(self, response):
#         for res in response.css('ul._chapter'):
#             yield {
#                 'chapterName': res.xpath('li/a/text()').get(),
#                 'href': res.xpath('li/a/@href').get(),
#             }
# # with open("../config/record.json",'r') as load_f:
# #      load_dict = json.load(load_f)
# #      print(load_dict)
#         #怎麼確定下一頁數據存不存在，如果最後一頁不確定呢？？？？
#         # for i in range(2, 5):  # 爬取第2，4页的数据
#         #     url = "https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=" + str(i) + "&filters="
#         #     yield Request(url, callback=self.parse)




import scrapy
import re
from tutorial.items import FictionItem
from scrapy.http import Request
class Story(scrapy.Spider):
    name = 'story'
    allowed_domains = ['quanshuwang.com']
    start_urls = [
        'http://www.quanshuwang.com/list/1_2.html',
        'http://www.quanshuwang.com/list/1_3.html',
        'http://www.quanshuwang.com/list/1_4.html',
        'http://www.quanshuwang.com/list/1_5.html',
        'http://www.quanshuwang.com/list/1_6.html',
        'http://www.quanshuwang.com/list/1_7.html',
        'http://www.quanshuwang.com/list/1_8.html',
        'http://www.quanshuwang.com/list/1_9.html',
        'http://www.quanshuwang.com/list/1_10.html',
    ] #全书网玄幻魔法类前10页
    #获取每一本书的URL
    def parse(self, response):
        # 'image': ul.xpath('div[has-class("p_img")]/a/img/@src').get(),
        book_urls = response.xpath('li/a[@class="l mr10"]/@href').extract()
        for book_url in book_urls:
            yield Request(book_url, callback=self.parse_read)
 
    #获取马上阅读按钮的URL，进入章节目录
    def parse_read(self, response):
        read_url = response.xpath('//a[@class="reader"]/@href').extract()[0]
        yield Request(read_url, callback=self.parse_chapter)
 
    #获取小说章节的URL
    def parse_chapter(self, response):
        chapter_urls = response.xpath('//div[@class="clearfix dirconone"]/li/a/@href').extract()
        for chapter_url in chapter_urls:
            yield Request(chapter_url, callback=self.parse_content)
 
    #获取小说名字,章节的名字和内容
    def parse_content(self, response):
        #小说名字
        name = response.xpath('//div[@class="main-index"]/a[@class="article_title"]/text()').extract_first()
 
        result = response.text
        #小说章节名字
        chapter_name = response.xpath('//strong[@class="l jieqi_title"]/text()').extract_first()
        #小说章节内容
        chapter_content_reg = r'style5\(\);</script>(.*?)<script type="text/javascript">'
        chapter_content_2 = re.findall(chapter_content_reg, result, re.S)[0]
        chapter_content_1 = chapter_content_2.replace('    ', '')
        chapter_content = chapter_content_1.replace('<br />', '')
 
        item = FictionItem()
        item['name'] = name
        item['chapter_name'] = chapter_name
        item['chapter_content'] = chapter_content
        yield item
