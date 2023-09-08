# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MainItem(scrapy.Item):
    car_model = scrapy.Field()
    car_model_link = scrapy.Field()
    production_date = scrapy.Field()
    car_series = scrapy.Field()
    series_model = scrapy.Field()
    series_model_link = scrapy.Field()
    series_production_date = scrapy.Field()
    series = scrapy.Field()
    maingroup = scrapy.Field()
    maingroup_link = scrapy.Field()
    code = scrapy.Field()
    link_no = scrapy.Field()
    code_link = scrapy.Field()
    parameter = scrapy.Field()
    note = scrapy.Field()
    sub_production_date = scrapy.Field()
    page = scrapy.Field()