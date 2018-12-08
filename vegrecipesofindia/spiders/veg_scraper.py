import os
import re
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from scrapy.linkextractor import LinkExtractor
from vegrecipesofindia.items import Recipe ,Ingredient, RecipeJson
import time
import json


class vegRecipeScraper(CrawlSpider):
    # The name of the spider
    name = "vegRecipe"

    # The domains that are allowed (links to other domains are skipped)
    allowed_domains=["vegrecipesofindia.com"]

    deny_words = ['/recipes/','privacy','terms','media','/recipe/','About','Archives',\
                    'index','comment','email','about']

    # The URLs to start with
    start_urls = ["https://www.vegrecipesofindia.com/recipes-index/"]

    # This spider has one rule: extract all (unique and canonicalized) links, follow them and parse them using the parse_items method
    rules = [
        Rule(
            LinkExtractor(
                canonicalize=True,
                deny = (deny_words),
                unique=True
            ),
            follow=True,
            callback="parse_items"
        )
    ]

    # Method which starts the requests by visiting all URLs specified in start_urls
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_items(self,response):
        time.sleep(2)
        print(response)

        if response.css('span.wprm-recipe-details-icon'):
            all_tags = response.xpath('//script/text()')
            #print(all_tags)
            for x in all_tags:
                if "@type" in x.extract():
                    print(x.extract())
                    yield {
                        "data":x.extract().strip()
                    }