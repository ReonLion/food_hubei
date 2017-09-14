# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FoodHubeiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    qualified_rate = scrapy.Field()
    qualified_num = scrapy.Field()
    food_name = scrapy.Field()
    food_model = scrapy.Field()
    bar_code = scrapy.Field()
    unqualified_num = scrapy.Field()
    sampling_province = scrapy.Field()
    name_first_letter = scrapy.Field()
    production_name = scrapy.Field()
    check_num = scrapy.Field()
    food_type = scrapy.Field()
    id = scrapy.Field()
    check_flag = scrapy.Field()
    
class FoodTypeItem(scrapy.Item):
    first_div = scrapy.Field()
    second_div = scrapy.Field()