# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hongniang.items import HongniangItem

class HongniangspiderSpider(CrawlSpider):
    name = 'hongniangSpider'
    allowed_domains = ['hongniang.com']
    start_urls = ['http://www.hongniang.com/index/search?sort=0&wh=0&sex=2&starage=0&province=0&city=0&marriage=0&edu=0&income=0&height=0&pro=0&house=0&child=0&xz=0&sx=0&mz=0&hometownprovince=0']

    #中国红娘index页面的分页
    page_lx = LinkExtractor(allow=('index/search\?.*&page=\d+'))
    #个人详细的信息
    self_lx = LinkExtractor(allow=('user/member/id/\d+'))
    #规则
    rules = (
        Rule(page_lx,follow=True),
        Rule(self_lx,callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        item = HongniangItem()
        # 用户名称
        item['nickname'] = self.get_nickname(response)
        # 用户id
        item['loveid'] = self.get_loveid(response)
        # 用户的照片
        item['photos'] = self.get_photos(response)
        # 用户年龄
        item['age'] = self.get_age(response)
        # 用户的身高
        item['height'] = self.get_height(response)
        # 用户是否已婚
        item['ismarried'] = self.get_ismarried(response)
        # # 用户年收入
        item['yearincome'] = self.get_yearincome(response)
        # # 用户的学历
        item['education'] = self.get_education(response)
        # # 用户的地址
        item['workaddress'] = self.get_workaddress(response)
        # 用户的内心独白
        item['soliloquy'] = self.get_soliloquy(response)
        # 用户的性别
        item['gender'] = self.get_gender(response)
        print item
        yield item


    def get_nickname(self,response):
        nickname  = response.xpath('//div[@class="info1"]/div[@class="name nickname"]/text()').extract()[0]
        if len(nickname)>0:
             nickname = nickname.strip()
        else:
            nickname = "NULL"
        return nickname

    def get_loveid(self, response):
        loveid = response.xpath('//div[@class="info1"]/div[@class="loveid"]/text()').extract()[0]
        if len(loveid) > 0:
            loveid = loveid.strip()
        else:
            loveid = "NULL"
        return loveid

    def get_photos(self, response):
        photos = response.xpath('//div[@id="tFocus-btn"]/ul/li/img/@src').extract()
        if len(photos) > 0:
            pass
        else:
            photos = "NULL"
        return photos

    def get_age(self, response):
        age = response.xpath('//div[@class="info2"]/div/ul/li/text()').extract()[0]
        if len(age) > 0:
            age = age.strip()
        else:
            age = "NULL"
        return age

    def get_height(self, response):
        height = response.xpath('//div[@class="info2"]/div/ul/li/text()').extract()[2]
        if len(height) > 0:
            height = height.strip()
        else:
            height = "NULL"
        return height

    def get_ismarried(self, response):
        ismarried = response.xpath('//div[@class="info2"]/div/ul/li/text()').extract()[1]
        if len(ismarried) > 0:
            ismarried = ismarried.strip()
        else:
            ismarried = "NULL"
        return ismarried

    def get_yearincome(self, response):
        yearincome = response.xpath('//div[@class="info2"]/div/ul/li/text()').extract()[4]
        if len(yearincome) > 0:
            yearincome = yearincome.strip()
        else:
            yearincome = "NULL"
        return yearincome

    def get_education(self, response):
        education = response.xpath('//div[@class="info2"]/div/ul/li/text()').extract()[3]
        if len(education) > 0:
            education = education.strip()
        else:
            education = "NULL"
        return education

    def get_workaddress(self, response):
        workaddress = response.xpath('//div[@class="info2"]/div/ul/li/text()').extract()[5]
        if len(workaddress) > 0:
            workaddress = workaddress.strip()
        else:
            workaddress = "NULL"
        return workaddress

    def get_soliloquy(self, response):
        soliloquy = response.xpath('//div[@class="info5"]/div[@class="text"]/text()').extract()[0]
        if len(soliloquy) > 0:
            soliloquy = soliloquy.strip()
        else:
            soliloquy = "NULL"
        return soliloquy

    def get_gender(self, response):
        return "女"
