import scrapy


class DetailSpider(scrapy.Spider):
    name = "detail"
    start_urls = [
        'http://ekt2.com/EKT/Car_Service/Battery_Charging_AND_Maintenance/Battery_Car/',
    ]

    def parse(self, response):
    	#follow link to event page
    	for href in response.css('div.right-details > a::attr(href)'):
    		yield response.follow(href, self.parse_detail)
    	

    def parse_detail(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('div.title::text'),
            'date': extract_with_css('div.date-bar > div.date::text'),
            'image': extract_with_css('div.img > a::attr(href)'),
        }	



