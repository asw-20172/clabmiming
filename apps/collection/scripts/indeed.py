# coding: utf-8

import mechanize
from bs4 import BeautifulSoup
import json

# import sys
# import logging
# from IPython.core.display import HTML
# reload(sys)
# sys.setdefaultencoding('utf-8')
# logger = logging.getLogger("mechanize")
# logger.addHandler(logging.StreamHandler(sys.stdout))
# logger.setLevel(logging.DEBUG)


class Indeed(object):

    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.browser.set_handle_referer(False)
        self.browser.set_handle_refresh(False)
        self.browser.addheaders = [('User-agent', 'Firefox')]

    def search(self, key_word, location):
        self.browser.open("https://www.indeed.com.pe/")
        self.browser.select_form(nr=0)
        self.browser.form['q'] = key_word
        self.browser.form['l'] = location
        self.browser.submit()
        print "=================="
        print self.browser.geturl()
        print "=================="
        self.__get_links_pages()
        print "Links: ", len(self.jobLinks)
        self.__get_data()
        print "Datos: ", len(self.data)
        print "=================="

    def export_to_csv(self, filename):
        with open(filename, 'w') as fout:
            json.dump(self.data, fout)

    def __get_links_pages(self):
        self.jobLinks = [
            jobLink
            for jobLink in self.browser.links()
            if jobLink.url.startswith("/company/")  # or
            # jobLink.url.startswith("/rc/")
        ]
        for link in self.browser.links():
            if link.text.isdigit():
                self.browser.follow_link(link)
                self.jobLinks += [
                    jobLink for jobLink in self.browser.links()
                    if jobLink.url.startswith("/company/")  # or
                    # jobLink.url.startswith("/rc/")
                ]
        self.jobLinks = self.jobLinks + self.__get_links_sig()

    def __get_links_sig(self):
        jobLinksTemp = []
        link_sig = [l for l in self.browser.links() if l.text ==
                    u'Siguiente\xa0\xbb']
        for link in link_sig:
            self.browser.follow_link(link)
            jobLinksTemp += [
                jobLink for jobLink in self.browser.links()
                if jobLink.url.startswith("/company/")  # or
                # jobLink.url.startswith("/rc/")
            ]
        if link_sig:
            jobLinksTemp += self.__get_links_sig()
        return jobLinksTemp

    def __get_data(self):
        self.data = []
        for jobLink in self.jobLinks:
            print jobLink.url
            self.browser.follow_link(jobLink)
            if self.browser.geturl().startswith("https://www.indeed.com.pe"):
                soup = BeautifulSoup(
                    self.browser.response().read(), "html.parser")
                div_header = soup.select('div[data-tn-component=jobHeader]')[0]
                self.data.append(
                    dict(
                        url=jobLink.url,
                        company=div_header.select('.company')[0].string,
                        title=div_header.select('.jobtitle')[0].string,
                        location=div_header.select('.location')[0].string,
                        description=soup.find(id='job_summary').get_text(),
                        html=str(soup.find(id='job_summary')),
                        date=soup.select('.result-link-bar .date')[0].string
                    )
                )


if __name__ == "__main__":
    indeedd = Indeed()
    indeedd.search("Ingeniero de sistemas", "Lima")
    indeedd.export_to_csv("datasets/indeedd")
