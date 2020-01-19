import scrapy


class DetailSpider(scrapy.Spider):
    name = "detail"
    start_urls = [
        'https://kharkov.internet-bilet.ua/#all-events',
    ]

    def parse(self, response):
    	#follow link to event page
    	for href in response.css('div.event-title > a::attr(href)'):
    		yield response.follow(href, self.parse_detail)
    	

    def parse_detail(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h1.event-title::text'),
            'date': extract_with_css('div.date-bar > div.date::text'),
        }	



