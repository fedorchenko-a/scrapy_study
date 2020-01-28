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
            'name': extract_with_css('div.p-prod-r > div.title > span::text'),
            'price': extract_with_css('span#ContentPlaceHolderMain_C001_EKTProductsDetails1_lblRetailPrice::text'),
            'image_link': extract_with_css('img.zoom-tiny-image::attr(src)'),
        }	


#response.css('img.zoom-tiny-image::attr(src)')[0].get() image detail getter
#http://ekt2.com/Sitefinity/WebsiteTemplates/WebGreen/App_Themes/WebGreen/Images/Products/35000/25 BATTERY ACID CAR 12V  40AH VARTA.jpg //full image link
#response.css('span#ContentPlaceHolderMain_C001_EKTProductsDetails1_lblRetailPrice::text').get() //price getter
# start scrape / scrapy crawl detail -o batt_deatil.json