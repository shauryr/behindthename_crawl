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


class ProquestSpider(scrapy.Spider):
    name = "get_names"

    def start_requests(self):
        """
        create start urls using each year till 2021
        :return:
        """
        file1 = open("letter_pages_links.txt", "r")
        Lines = file1.readlines()

        count = 0
        # Strips the newline character
        for line in Lines:
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
        list_pages = response.selector.xpath(
            '//*[@id="body-inner"]/div[5]//a/@href'
        ).getall()

        list_page_num = []
        for page in list_pages:
            list_page_num.append("https://www.behindthename.com" + page)
        with open("name_urls.txt", "a+") as filehandle:
            for listitem in list_page_num:
                filehandle.write("%s\n" % listitem)
