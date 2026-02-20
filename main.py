from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# where is going to run
def main():
    print("Finance  News \n\n")
    print(10*"*")
    anarchyReading()
  
# call parsers to get it to start  
def anarchyReading():
    process = CrawlerProcess(get_project_settings())
    process.crawl("FinNews", domain="scrapy.org")
    process.start()



if __name__ == "__main__":
    main()