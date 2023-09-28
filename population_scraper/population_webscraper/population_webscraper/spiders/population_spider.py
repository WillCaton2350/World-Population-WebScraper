from scrapy import Spider
from population_webscraper.items import PopulationWebscraperItem

class CountrySpider(Spider):
    name = 'population_spider'
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']
    counter = 1
    def parse(self, response):
        web_item = PopulationWebscraperItem()
        web_item['url'] = response.url
        web_item['id'] = None
        web_item['title'] = None
        web_item['sub_title'] = None
        web_item['sub_description'] = None
        web_item['country_name'] = None
        web_item['population'] = None
        web_item['yearly_change'] = None
        web_item['net_change'] = None
        web_item['density'] = None
        web_item['land_area'] = None
        web_item['migrants'] = None
        web_item['fertility_rate'] = None
        web_item['med_rate'] = None
        web_item['minority_population'] = None
        web_item['world_share'] = None
        if response.url in self.start_urls:
            web_item['title'] = response.css('title::text').getall()
            web_item['sub_title'] = response.css('h1::text').getall()
            web_item['sub_description'] = response.css('meta[name="description"]::attr(content)').getall()
        for i in range(self.counter):
            self.counter += 1
            web_item['country_name'] = response.css(
                f'tr.odd:nth-child({self.counter}) td:nth-child(2) a::text').getall()
            web_item['population'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(3)::text').getall()
            web_item['yearly_change'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(4)::text').getall()
            web_item['net_change'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(5)::text').getall()
            web_item['density'] = response.css(
                f'tr.even:nth-child({self.counter}) > td:nth-child(6)::text').getall()
            web_item['land_area'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(7)::text').getall()
            web_item['migrants'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(8)::text').getall()
            web_item['fertility_rate'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(9)::text').getall()
            web_item['med_rate'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(10)::text').getall()
            web_item['minority_population'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(11)::text').getall()
            web_item['world_share'] = response.css(
                f'tr.odd:nth-child({self.counter}) > td:nth-child(12)::text').getall()
        yield web_item