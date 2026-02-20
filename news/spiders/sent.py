import scrapy
from news.items import NewsItem
import time

class NewsSpider(scrapy.Spider):
    name = "FinNews"
    start_urls = ['https://finance.yahoo.com/quote/NKE/news/']
    #start_urls = ['https://finance.yahoo.com/topic/stock-market-news/']  
    'https://query1.finance.yahoo.com/v7/finance/spark?symbols=AMZN%2CQS%2CICE%2CCORZ%2CHSAI%2CAVAV%2CENPH%2CEQIX%2CXPEV%2CVSEC%2CETSY%2CRELY%2CNVDA%2CLCID%2CNU%2CCYN%2CRKLB%2C1810.HK&range=1d&interval=5m&indicators=close&includeTimestamps=false&includePrePost=false&corsDomain=finance.yahoo.com&.tsrc=finance'
    
    def spider_opened(self, spider):
        self._t0 = time.perf_counter()

    def spider_closed(self, spider, reason):
        elapsed = time.perf_counter() - self._t0
        self.logger.info(f"Spider finished in {elapsed:.2f} seconds. Reason: {reason}")      
    
    ### parser getting text inside the text and also the link, title, ticker, and source
    def parse(self, response): 
        for headline in response.css('li.stream-item.story-item.yf-1drgw5l'):    
            link = headline.css('a.subtle-link::attr(href)').get()    
            #link = headline.css('a.subtle-link.fin-size-small.titles.noUnderline.yf-u4gyzs::attr(href)').get()
            title = headline.css('h3.clamp').get()
            date = headline.css('div.publishing').getall() 
            ticker = headline.css('div.name > span').getall()
            source = headline.css('div.publishing').getall()
            if link:
                yield response.follow(link, self.text_parse, meta={'TITLE': title,'date': date ,'ticker' : ticker})  
 
    def text_parse(self, response):
        StockNews = NewsItem()
        StockNews['date'] = response.meta.get('date'),
        StockNews['title'] = response.meta.get('TITLE'),
        StockNews['ticker'] = response.meta.get('ticker'),
        StockNews['source'] = response.meta.get('source'),
        StockNews['content'] = ''.join(response.css('p.yf-1090901::text').getall()),
        yield StockNews 
