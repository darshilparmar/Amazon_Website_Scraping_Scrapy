
import scrapy
from amazon.items import AmazonItem
import pandas as pd
from scrapy.utils.markup import remove_tags
import re
class AmazonbotSpider(scrapy.Spider):
    name = 'amazonbot'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/Apple-iPhone-X-Silver-256GB/product-reviews/B071P37652/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber={}'.format(i) for i in range(1,30)]
    


    

    def parse(self, response):
    	
    	title = response.xpath('//a[contains(@data-hook, "review-title")]/text()').extract()
    	ratings = response.xpath('//a[contains(@class, "a-link-normal")]/i[contains(@data-hook, "review-star-rating")]/span/text()').extract()
    	reviews = response.xpath('//div[contains(@class, "a-section review")]/div[contains(@class, "a-section celwidget")]/div[contains(@class, "a-row a-spacing-medium review-data")]/span[contains(@class, "a-size-base review-text")]').extract()
    	


    	for titl,rating,review in zip(title,ratings,reviews):
    		yield {'title': re.sub(r'[^a-zA-Z0-9]', '', titl.strip()), 'ratings': re.sub(r'[^a-zA-Z0-9]', '', rating.strip()), 'reviews': re.sub(r'[^a-zA-Z0-9]', '', remove_tags(review))}
    	
    		