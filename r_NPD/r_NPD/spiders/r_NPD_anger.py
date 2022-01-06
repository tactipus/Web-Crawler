import scrapy
from scrapy_splash import SplashRequest


class RNpdAngerSpider(scrapy.Spider):
    name = 'r_NPD_anger'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/NPD/']
    handle_httpstatus_list = [500, 502]

    def start_requests(self):
        yield SplashRequest('https://www.reddit.com/r/NPD/', self.parse, args={'wait': 0.5})

    def parse(self, response):
        print("Processing: " + response.url)

        # extract data using css selectors
        post_title = response.css("h3::text").extract()
        votes = response.css("._1rZYMD_4xY3gRcSS3p8ODO._25IkBM0rRUqWX5ZojEMAFQ::text").extract()
        author = response.xpath('//div[@class="_2mHuuvyV9doV3zwbZPtIPG"]//a/text()').extract()

        #

        print(post_title)
        print(votes)
        print(author)
        row_data = zip(post_title, votes, author)

        # making extracted data row wise
        for item in row_data:
            scraped_info = {
                'post_title': item[0],
                'votes': item[1],
                'author': item[2]
            }

            yield scraped_info
