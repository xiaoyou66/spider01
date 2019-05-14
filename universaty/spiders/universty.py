import scrapy
from universaty.items import UniversatyItem

class universty(scrapy.Spider):
    name="school"
    start_urls=['https://www.phb123.com/jiaoyu/gx/21950.html']

    def parse(self, response):
        schoolss=[]
        schools=response.xpath('//tbody/tr')
        for sch in schools:
            school=UniversatyItem()
            school['grade']=sch.xpath('./td[1]/text()').extract()
            school['school'] = sch.xpath('./td[2]/text()').extract()
            school['top'] = sch.xpath('./td[3]/text()').extract()
            school['start'] = sch.xpath('./td[4]/text()').extract()
            school['layout'] = sch.xpath('./td[5]/text()').extract()
            # school['score'] = sch.xpath('./td[6]/text()').extract()
            schoolss.append(school)
        return schoolss