from scrapy import Field,Item

class PopulationWebscraperItem(Item):
    url = Field()
    id = Field()
    title = Field()
    sub_title = Field()
    sub_description = Field()
    country_name = Field()
    population = Field()
    yearly_change = Field()
    net_change = Field()
    density = Field()
    land_area = Field()
    migrants = Field()
    fertility_rate = Field()
    med_rate = Field()
    minority_population = Field()
    world_share = Field()