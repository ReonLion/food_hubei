# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from food_hubei.items import FoodHubeiItem, FoodTypeItem

class FoodspiderSpider(scrapy.Spider):
    handle_httpstatus_list = [404]
    name = 'foodSpider'
    allowed_domains = ['www.foods12331.cn']
    start_urls = ['http://www.foods12331.cn']
    
    data = {
        "food_type":u"粮食加工品",
        "check_flag":u"不合格",
        "order_by":"1",
        "pageNo":0,
        "pageSize":20,
        "bar_code":"",
        "sampling_province":"",
        "name_first_letter":None,
        "food_name":None,
    }
    
    header_dict = {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "Connection":"keep-alive",
        "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":"JSESSIONID=F48AF93D76167EAF1263C81EB6CA2B68",
        "Host":"www.foods12331.cn",
        "Origin":"http://www.foods12331.cn",
        "Referer":"http://www.foods12331.cn/web/index.jsp?&food_type=%E7%B2%AE%E9%A3%9F%E5%8A%A0%E5%B7%A5%E5%93%81",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 OPR/47.0.2631.80",
        "X-Requested-With":"XMLHttpRequest",
    }

    def food_parse(self, response):
        res_data = json.loads(response.body)
        food_data_list = res_data['resultData']['items']
        for food_data in food_data_list:
            item = FoodHubeiItem()
            item['check_flag'] = response.meta['check_flag']
            item['id'] = food_data['id']
            item['food_name'] = food_data['food_name']
            item['production_name'] = food_data['production_name']
            item['food_model'] = food_data['food_model']
            item['sampling_province'] = food_data['sampling_province']
            item['food_type'] = food_data['food_type']
            item['check_num'] = food_data['check_num']
            item['qualified_num'] = food_data['qualified_num']
            item['unqualified_num'] = food_data['unqualified_num']
            item['qualified_rate'] = food_data['qualified_rate']
            item['name_first_letter'] = food_data['name_first_letter']
            item['bar_code'] = food_data['bar_code']
            yield item
    
    def parse(self, response):
        sub_selector_first = response.xpath('//div[@class="firstdiv"]/a')
        
        for sub_first in sub_selector_first:
            print "firsts" + str(len(sub_selector_first))
            sub_selector_second = sub_first.xpath('../../div[@class="secenddiv"]/a')
            for sub_second in sub_selector_second:
                print "seconds" + str(len(sub_selector_second))
                item = FoodTypeItem()
                item['first_div'] = sub_first.xpath('./text()').extract()[0]
                item['second_div'] = sub_second.xpath('./text()').extract()[0]
                
                self.data['food_type'] = item['second_div']
                
                for i in range(0, 40):
                    self.data['pageNo'] = i
                    i += 1
                    self.data['check_flag'] = u'不合格'
                    form_data = {'filters':json.dumps(self.data)}
                    yield scrapy.FormRequest('http://www.foods12331.cn/food/detail/findFoodByPage.json',
                                             formdata = form_data,
                                             method = 'POST',
                                             headers = self.header_dict,
                                             meta = {'check_flag':u'不合格'},
                                             callback = self.food_parse)
                    
                for i in range(0, 40):
                    self.data['pageNo'] = i
                    i += 1
                    self.data['check_flag'] = u'合格'
                    form_data = {'filters':json.dumps(self.data)}
                    yield scrapy.FormRequest('http://www.foods12331.cn/food/detail/findFoodByPage.json',
                                             formdata = form_data,
                                             method = 'POST',
                                             headers = self.header_dict,
                                             meta = {'check_flag':u'合格'},
                                             callback = self.food_parse)
        