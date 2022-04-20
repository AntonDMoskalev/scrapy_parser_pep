import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """
    The spider parses the PEP list,
    takes the data about the PEP number,
    goes to the PEP page and takes the status data and the name.
    """
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        all_pep = response.css('tbody')
        for pep in all_pep.css('a[href^="pep"]'):
            number = pep.css('a::text').get()
            yield response.follow(pep, callback=self.parse_pep,
                                  cb_kwargs=dict(number=number))

    def parse_pep(self, response, number):
        data = {
            'number': number,
            'name': response.css(
                'h1.page-title::text').get().split('– ')[-1],
            'status': response.css(
                'dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)
