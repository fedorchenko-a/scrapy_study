import scrapy


class BiletSpider(scrapy.Spider):
    name = "bilet"
    start_urls = [
        'https://kharkov.internet-bilet.ua/#all-events',
    ]

    def parse(self, response):
        for test in response.css('div.event-title'):
            yield {
                'event_name': test.css('a::attr(title)').get()
                
            }

        '''next_page = response.css('li.next a::attr(href)').get()
        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)'''