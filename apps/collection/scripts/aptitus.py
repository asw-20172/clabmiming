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


class Aptitus(object):

    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.browser.set_handle_referer(False)
        self.browser.set_handle_refresh(False)
        self.browser.addheaders = [('User-agent', 'Firefox')]

    def search(self, key_word):
        self.browser.open(
            "https://aptitus.com/buscar-trabajo-en-peru?q=" +
            key_word.replace(' ', '-')
        )
        print "=================="
        print self.browser.geturl()
        print "=================="
        self.__get_links_pages()
        print "Links len: ", len(self.jobLinks)
        self.__get_data()
        print "Data len: ", len(self.data)
        print "=================="
        # https://aptitus.com/buscar-trabajo-en-peru/de-tecnologia-sistemas-y-telecomunicaciones

    def export_to_csv(self, filename):
        with open(filename, 'w') as fout:
            json.dump(self.data, fout)

    def __get_links_pages(self):
        self.jobLinks = []
        latest_pagination = [
            l for l in self.browser.links()
            if l.text.isdigit()
        ][-1]
        for d in self.browser.links():
            if d.text.isdigit():
                self.browser.follow_link(d)
                self.jobLinks += [
                    l for l in self.browser.links()
                    if l.url.startswith(
                        "https://aptitus.com/ofertas-de-trabajo/"
                    )
                ]
        self.jobLinks = self.jobLinks + \
            self.__get_links_sig(latest_pagination)

    def __get_links_sig(self, latest_pagination):
        jobLinks_temp = []
        temp = [l for l in self.browser.links() if l.text.isdigit()]
        if temp:
            links = [i for i in temp if int(
                i.text) > int(latest_pagination.text)]
            latest_pagination = temp[-1]
            for link in links:
                self.browser.follow_link(link)
                jobLinks_temp += [
                    l for l in self.browser.links()
                    if l.url.startswith(
                        "https://aptitus.com/ofertas-de-trabajo/"
                    )
                ]
            if links:
                jobLinks_temp += self.__get_links_sig(latest_pagination)
            return jobLinks_temp

    def __get_data(self):
        self.data = []
        for j in self.jobLinks:
            self.browser.follow_link(j)
            print j.url
            soup = BeautifulSoup(
                self.browser.response().read(), "html.parser")
            if not soup.body.find(
                text='Este aviso ha finalizado, puedes ver otros avisos similares'
            ):
                self.data.append(
                    dict(
                        url=j.url,
                        company=soup.select(
                            'a.b-job-detail_subtitle')[0].string,
                        title=soup.select(
                            'h1.b-job-detail_title')[0].string,
                        location=soup.body.find(
                            text='Ubicación').parent.next_sibling.string,
                        description=soup.select(
                            '.b-job-info')[0].get_text(),
                        html=str(soup.select('.b-job-info')[0]),
                        date=soup.body.find(
                            text='Publicado').parent.next_sibling.string,
                        area=soup.body.find(
                            text='Área').parent.next_sibling.string
                    )
                )


if __name__ == "__main__":
    aptituss = Aptitus()
    aptituss.search("Ingeniero de sistemas")
    aptituss.export_to_csv("datasets/aptitusde")
