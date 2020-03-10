import scrapy
from urllib.parse import urljoin

class ImageSpider(scrapy.Spider):
    name = "image"
    start_urls = [
        'https://3v3.com.ua/category_7329_show_all.html',
    ]
    

    def parse(self, response):
    	##follow link to event page
    	for info in response.css('div.hd1 td.bf a::attr(href)'):
    		yield response.follow(info, self.parse_detail)



            #response.follow(href, self.parse_detail)
    	

    def parse_detail(self, response):

        '''def extract_with_css(query):

            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('div.c58 p::text'),
            'reference': extract_with_css('div.c58 > div.item-info span::text'),
            'image_urls': [urljoin('https://ekt2.com/', extract_with_css('div.c23 img::attr(src)'))],
        }'''	
        yield {
            'name': response.css('td.hd2::text').get(),
            #'original_number': response.css('div.c58 > div.item-info span::text')[3].get(),
            'reference': response.css('td.buyButton table tr td b::text')[2].get(),
            #'product_information': response.css('div.c58 > div.item-info p::text')[6].get(),
            'price': response.css('td.price span.fromPrice2 b::text').get(),
            'image_urls': [urljoin('https://3v3.com.ua', response.css('td.imboxl a::attr(href)').get())],
            #'image_urls': [urljoin('https://www.ekt2.com', url) for url in response.css('div.c23 img::attr(src)').getall()],
        }

#response.css('img.zoom-tiny-image::attr(src)')[0].get() image detail getter
#http://ekt2.com/Sitefinity/WebsiteTemplates/WebGreen/App_Themes/WebGreen/Images/Products/35000/25 BATTERY ACID CAR 12V  40AH VARTA.jpg //full image link
#response.css('span#ContentPlaceHolderMain_C001_EKTProductsDetails1_lblRetailPrice::text').get() //price getter
# start scrape / scrapy crawl detail -o batt_deatil.json

#follow link old ver 'div.right-details > a::attr(href)'

#base_url = 'https://ekt2.com/'