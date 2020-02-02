import scrapy
from urllib.parse import urljoin

class DetailSpider(scrapy.Spider):
    name = "detail"
    start_urls = [
        'https://ekt2.com/EKT/Car/Battery-Charging-Maintenance/Battery',
    ]
    

    def parse(self, response):
    	#follow link to event page
    	for href in response.css('div.r53 a::attr(href)'):
    		yield response.follow(href, self.parse_detail)
    	

    def parse_detail(self, response):

        '''def extract_with_css(query):

            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('div.c58 p::text'),
            'reference': extract_with_css('div.c58 > div.item-info span::text'),
            'image_urls': [urljoin('https://ekt2.com/', extract_with_css('div.c23 img::attr(src)'))],
        }'''	
        yield {
            'name': response.css('div.c58 p::text').get(),
            'reference': response.css('div.c58 > div.item-info span::text').get(),
            'image_urls': [urljoin('https://ekt2.com', url) for url in response.css('div.c23 img::attr(src)').getall()]
,
        }

#response.css('img.zoom-tiny-image::attr(src)')[0].get() image detail getter
#http://ekt2.com/Sitefinity/WebsiteTemplates/WebGreen/App_Themes/WebGreen/Images/Products/35000/25 BATTERY ACID CAR 12V  40AH VARTA.jpg //full image link
#response.css('span#ContentPlaceHolderMain_C001_EKTProductsDetails1_lblRetailPrice::text').get() //price getter
# start scrape / scrapy crawl detail -o batt_deatil.json

#follow link old ver 'div.right-details > a::attr(href)'

#base_url = 'https://ekt2.com/'