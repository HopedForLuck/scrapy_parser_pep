import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css('a[href^="pep-"]')
        for pep_link in all_pep:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number_name = response.css('h1.page-title::text').get().split()
        data = {
            'number': int(number_name[1]),
            'name': number_name[3:],
            'status': response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get(),
        }
        yield PepParseItem(data)
