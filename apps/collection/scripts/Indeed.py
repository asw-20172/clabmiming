# coding: utf-8
import sys

import mechanize
# from IPython.core.display import HTML
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_referer(False)
    browser.set_handle_refresh(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    browser.open("https://www.indeed.com.pe/")
    browser.select_form(nr=0)
    # ===============================================
    browser.form['q'] = "Ingeniero de sistemas"
    browser.form['l'] = "Lima"
    # ===============================================
    browser.submit()
    print browser.geturl()
    # search_url = browser.geturl()
    jobLinks = get_links_pages(browser)
    print "=================="
    print "Links:", len(jobLinks)
    data = get_data(browser, jobLinks)
    print "Datos:", len(data)
    print "=================="


def get_links_pages(browser):
    jobLinks = [
        jobLink
        for jobLink in browser.links()
        if jobLink.url.startswith("/company/")  # or
        # jobLink.url.startswith("/rc/")
    ]
    for link in browser.links():
        if link.text.isdigit():
            browser.follow_link(link)
            jobLinks += [
                jobLink for jobLink in browser.links()
                if jobLink.url.startswith("/company/")  # or
                # jobLink.url.startswith("/rc/")
            ]
    jobLinks = jobLinks + get_links_sig(browser)
    return jobLinks


def get_links_sig(browser):
    jobLinks = []
    link_sig = [l for l in browser.links() if l.text == u'Siguiente\xa0\xbb']
    for link in link_sig:
        browser.follow_link(link)
        jobLinks += [
            jobLink for jobLink in browser.links()
            if jobLink.url.startswith("/company/")  # or
            # jobLink.url.startswith("/rc/")
        ]
    if link_sig:
        jobLinks += get_links_sig(browser)
    return jobLinks


def get_data(browser, jobLinks):
    data = []
    for jobLink in jobLinks:
        print jobLink.url
        browser.follow_link(jobLink)
        if browser.geturl().startswith("https://www.indeed.com.pe"):
            soup = BeautifulSoup(browser.response().read(), "html.parser")
            div_header = soup.select('div[data-tn-component=jobHeader]')[0]
            data.append(
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
    return data


if __name__ == "__main__":
    main()
