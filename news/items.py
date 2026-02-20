import scrapy
## class were data gets normalize to respective values
class NewsItem(scrapy.Item):
    date =  scrapy.Field()
    title = scrapy.Field()
    ticket = scrapy.Field()
    source = scrapy.Field()
    content = scrapy.Field()
    
    
