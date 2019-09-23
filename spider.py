# -*- coding: utf-8 -*-
import scrapy
from renren.items import RenrenItem

class RenspiderSpider(scrapy.Spider):
    name = 'renspider'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url="http://www.renren.com/PLogin.do"    # 人人网登陆页面

        data={
              "email":"15702318381",         # 人人网账号
              "password":"kqs2000..",        #  人人网密码
        }
        # FormRequest  执行post请求时 提交数据
        request=scrapy.FormRequest(url=url,formdata=data,callback=self.parse_page)
        # 把请求发送给引擎  让其通过调用其他组件来下载网页
        yield  request

    def parse_page(self,response):
        # 发送登陆大鹏个人用户的页面请求
       request = scrapy.Request(url="http://www.renren.com/880151247/profile",callback=self.parse_profile)
       yield  request

    def parse_profile(self,respnse):

        #  解析网页数据
        name=respnse.xpath("//h1[@class='avatar_title']//text()").get().strip()
        value_school=respnse.xpath("//li[@class='school']/span/text()").get()
        value_birthday=respnse.xpath("//li[@class='birthday']/span[2]/text()").get()
        user_hometown=respnse.xpath("//li[@class='hometown']/text()").get()

        yield RenrenItem(name=name,value_school=value_school,value_birthday=value_birthday,user_hometown=user_hometown)

        pass
