from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl('Unidays_spider')  # Replace 'spider_name' with the name of your spider
    process.start()
    
if __name__ == "__main__":
    run_spider()
