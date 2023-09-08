import scrapy
from main.items import MainItem

class LinkSpider(scrapy.Spider):
    name = "link"
    subgroup_link_no = 0

    def start_requests(self):
        url = 'https://catcar.info/subaru/?lang=en&l=cmVnaW9uPT1saGR8fHN0PT0yMHx8c3RzPT17IjEwIjoiTWFya2V0IiwiMjAiOiJFdXJvcGUgKExIRCkifQ%3D%3D'
        yield scrapy.Request(url, callback=self.parse)
            
    def parse(self, response):
        tr_elements = response.css('tr')
        for model in tr_elements[1:]:
            car_model = model.css('td:nth-child(1) a::text').get()
            car_model_link = model.css('td:nth-child(1) a::attr(href)').get()
            production_date = model.css('td:nth-child(2)::text').get()
            car_series = model.css('td:nth-child(3)::text').get()
            yield scrapy.Request(car_model_link, callback=self.series_page,cb_kwargs={'car_model':car_model,'car_model_link':car_model_link,'production_date':production_date,'car_series':car_series})

    def series_page(self, response,car_model,car_model_link,production_date,car_series):

        tr_elements = response.css('tr')
        for model in tr_elements[1:]:
            series_model = model.css('td:nth-child(1) a::text').get()
            series_model_link = model.css('td:nth-child(1) a::attr(href)').get()
            series_production_date = model.css('td:nth-child(2)::text').get()
            series = model.css('td:nth-child(3)::text').get()
            yield scrapy.Request(series_model_link, callback=self.maingroup_page,cb_kwargs={'car_model':car_model,'car_model_link':car_model_link,'production_date':production_date,'car_series':car_series,
                                                                                      'series_model':series_model,'series_model_link':series_model_link,'series_production_date':series_production_date,'series':series
                                                                                      })


    def maingroup_page(self, response,car_model,car_model_link,production_date,car_series,series_model,series_model_link,series_production_date,series):
        tr_elements = response.css('tr')

        for model in tr_elements:
            maingroup = model.css('td:nth-child(1) a::text').get()
            maingroup_link = model.css('td:nth-child(1) a::attr(href)').get()
            yield scrapy.Request(maingroup_link, callback=self.subgroup_page,cb_kwargs={'car_model':car_model,'car_model_link':car_model_link,'production_date':production_date,'car_series':car_series,
                                                                                      'series_model':series_model,'series_model_link':series_model_link,'series_production_date':series_production_date,'series':series,
                                                                                      'maingroup':maingroup,'maingroup_link':maingroup_link
                                                                                      })


    def subgroup_page(self, response,car_model,car_model_link,production_date,car_series,series_model,series_model_link,series_production_date,series,maingroup,maingroup_link):
        pages = response.xpath('//div[@class="content-left"]/ul/li/a/@href').getall()
        if pages:
            for page in pages:
                yield scrapy.Request(page, callback=self.page,cb_kwargs={'car_model':car_model,'car_model_link':car_model_link,'production_date':production_date,'car_series':car_series,
                                                                                    'series_model':series_model,'series_model_link':series_model_link,'series_production_date':series_production_date,'series':series,
                                                                                    'maingroup':maingroup,'maingroup_link':maingroup_link
                                                                                    })
        else:
            tr_elements = response.css('tr')
            for tr in tr_elements[1:]:
                code = tr.xpath('td[1]/a/text()').get()
                code_link = tr.xpath('td[1]/a/@href').get()
                parameter = tr.xpath('td[2]/text()').get()
                note = tr.xpath('td[3]/text()').get()
                sub_production_date = tr.xpath('td[4]/text()').get()
                page = tr.xpath('td[5]/text()').get()
                
                self.subgroup_link_no+=1
                item = MainItem()
                item['car_model'] = car_model
                item['car_model_link'] = car_model_link
                item['production_date'] = production_date
                item['car_series'] = car_series
                item['series_model'] = series_model
                item['series_model_link'] = series_model_link
                item['series_production_date'] = series_production_date
                item['series'] = series
                item['maingroup'] = maingroup
                item['maingroup_link'] = maingroup_link
                item['code'] = code
                item['link_no'] = self.subgroup_link_no
                item['code_link'] = code_link
                item['parameter'] = parameter
                item['note'] = note
                item['sub_production_date'] = sub_production_date
                item['page'] = page
                
                yield item

    def page(self,response,car_model,car_model_link,production_date,car_series,series_model,series_model_link,series_production_date,
             series,maingroup,maingroup_link):
            
            tr_elements = response.css('tr')
            for tr in tr_elements[1:]:
                code = tr.xpath('td[1]/a/text()').get()
                code_link = tr.xpath('td[1]/a/@href').get()
                parameter = tr.xpath('td[2]/text()').get()
                note = tr.xpath('td[3]/text()').get()
                sub_production_date = tr.xpath('td[4]/text()').get()
                page = tr.xpath('td[5]/text()').get()
                
                self.subgroup_link_no+=1
                item = MainItem()
                item['car_model'] = car_model
                item['car_model_link'] = car_model_link
                item['production_date'] = production_date
                item['car_series'] = car_series
                item['series_model'] = series_model
                item['series_model_link'] = series_model_link
                item['series_production_date'] = series_production_date
                item['series'] = series
                item['maingroup'] = maingroup
                item['maingroup_link'] = maingroup_link
                item['code'] = code
                item['link_no'] = self.subgroup_link_no
                item['code_link'] = code_link
                item['parameter'] = parameter
                item['note'] = note
                item['sub_production_date'] = sub_production_date
                item['page'] = page
                
                yield item
            
