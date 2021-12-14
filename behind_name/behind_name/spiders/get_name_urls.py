"""

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
