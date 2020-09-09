# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     # image = scrapy.Field()
#     # href = scrapy.Field()
#     # name = scrapy.Field()
#     # cost = scrapy.Field()
#     chapterName = scrapy.Field()
#     href = scrapy.Field()

class FictionItem(scrapy.Item):
    name = scrapy.Field()   #小说名字
    chapter_name = scrapy.Field()   #小说章节名字
    chapter_content = scrapy.Field()    #小说章节内容