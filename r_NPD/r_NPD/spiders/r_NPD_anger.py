import scrapy


class RNpdAngerSpider(scrapy.Spider):
    name = 'r_NPD_anger'
    allowed_domains = ['reddit.com']
    start_urls = ['https://www.reddit.com/r/NPD/']

    def parse(self, response):
        print("Processing: " + response.url)

        # extract data using css selectors
        post_title = response.css("h3::text").extract()
        # price_range = response.css('.value::text').extract()

        # extract data using xpath
        # orders = response.xpath("//em[@title='Total Orders']/text()").extract()
        # company_name = response.xpath("//a[@class='store $p4pLog']/text()").extract()

        row_data = zip(post_title)

        # making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page' : response.url,
                'post_title' : item[0]
                # 'product_name' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                # 'price_range' : item[1],
                # 'orders' : item[2],
                # 'company_name' : item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
