import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'microsoft.com'
    allowed_domains = ['docs.microsoft.com']
    start_urls = ['https://docs.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-start-page']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
