import scrapy
#from scrapy.spiders import Rule
from scrapy.selector import Selector

class MyItem(scrapy.Item):
    title = scrapy.Field()
    desc = scrapy.Field()
    link = scrapy.Field()

class StackOverflowSpider(scrapy.Spider):
    name = 'zPOC'
    allowed_domains = ['cdc.gov']
    start_urls = ['http://www.cdc.gov/outbreaks/index.html']

#    rules = (
#        Rule(LinkExtractor(allow=('/travel/notices/alert/', ), deny=('', )))
#    )

    def parse(self, response):
	#print(response.css('.module-typeD .list-bullet').extract())
	#print(response.css('.module-typeD').extract())

	#titles	= response.xpath('//li[@class="item-title"]/a/text()').extract()
        
        item = scrapy.Item()
        items = []
        divOB = response.xpath('.//div[@id="rss-outbreaksUS"]').extract()
	      for p in divOB:
            liOB = p.xpath('//li').extract()

            for i in liOB:
                link = i.xpath('//a/@href').extract()
                title = i.xpath('//a/text()').extract()
                desc = i.xpath('//text()').re('-\s[^\t]*\\r')
                grp = MyItem(title=title, link=link, desc=desc)
                print title, link, desc
                items.append(grp)

                #yield grp 
                #yield scrapy.Request(full_url, callback=self.parse_question)

        return items

   # def parse_question(self, response):
   #     yield {
   #         'name': response.css('h1 a::text').extract()[0],
   #         'info': response.xPath('//li[@class="item-title"]/a/text()').extract()[0],
   #         'body': response.css('.question .post-text').extract()[0],
   #         'tags': response.css('.question .post-tag::text').extract(),
   #         'link': response.url,
   #     }
