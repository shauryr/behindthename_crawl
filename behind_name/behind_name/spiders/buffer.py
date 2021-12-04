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
    name = "behind_name"

    def start_requests(self):
        """
        create start urls using each year till 2021
        :return:
        """
        for i in [
            "/names/letter/a",
            "/names/letter/b",
            "/names/letter/c",
            "/names/letter/d",
            "/names/letter/e",
            "/names/letter/f",
            "/names/letter/g",
            "/names/letter/h",
            "/names/letter/i",
            "/names/letter/j",
            "/names/letter/k",
            "/names/letter/l",
            "/names/letter/m",
            "/names/letter/n",
            "/names/letter/o",
            "/names/letter/p",
            "/names/letter/q",
            "/names/letter/r",
            "/names/letter/s",
            "/names/letter/t",
            "/names/letter/u",
            "/names/letter/v",
            "/names/letter/w",
            "/names/letter/x",
            "/names/letter/y",
            "/names/letter/z",
        ]:
            yield scrapy.Request(
                url="https://www.behindthename.com" + i, callback=self.parse
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
            '//*[@id="div_pagination"]/nav/a/@href'
        ).getall()
        list_page_num = []
        if len(list_pages) > 0:
            list_page_num.append(
                "https://www.behindthename.com" + list_pages[0][:-1] + "1"
            )
        else:
            with open("letter_pages_links.txt", "a+") as filehandle:
                filehandle.write("%s\n" % response.url)

        for page in list_pages:
            list_page_num.append("https://www.behindthename.com" + page)
        with open("letter_pages_links.txt", "a+") as filehandle:
            for listitem in list_page_num:
                filehandle.write("%s\n" % listitem)
