"""
This spider gets the URLs for 27k authors from pqdtopen which has been decommissioned for proquest.com
Steps :
Proquest open gives just first 1000 documents
get 1964 to 2000, get 2000 to 2006, get 2006 to 2007
Starting from 2007-08 to 2020-21 bi directional crawl for each year (CHRON and REV_CHRON)
To run this :
`scrapy crawl proquest`
and this will write a list of urls on proquest which appear on the SERP
"""
import scrapy
import jsonlines

class ProquestSpider(scrapy.Spider):
    name = "get_info"

    def start_requests(self):
        """
        create start urls using each year till 2021
        :return:
        """
        file1 = open("uniq.name_urls.txt", "r")
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
            if line.startswith("https://www.behindthename.com/name"):
                count += 1
                print("Line{}: {}".format(count, line.strip()))
                yield scrapy.Request(
                    url=line, callback=self.parse,
                )

    def parse(self, response, **kwargs):
        """
        writes a file with unique links in it, which are later used to crawl the actual data
        :param **kwargs:
        :param response:
        :return:
        """
        # loop from 1 to the size of the table on proquest
        name = response.selector.xpath(
            '//*[@id="body-inner"]/div[1]/div/div/h1/text()'
        ).get()

        list_Diminutives = response.selector.xpath(
            '//*[@id="body-inner"]/div[3]/article/section[2]/div[2]/div[2]/span[2]/a/text()'
        ).getall()

        list_Variant = response.selector.xpath(
            '//*[@id="body-inner"]/div[3]/article/section[2]/div[2]/div[1]/span[2]/a/text()'
        ).getall()

        with jsonlines.open('output.jsonl', mode='a') as writer:
            writer.write({
                "name" : name,
                'Diminutives' : list_Diminutives,
                'Variant' : list_Variant,
                'url' : response.url
            })