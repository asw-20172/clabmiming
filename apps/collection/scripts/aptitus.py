# coding: utf-8
import mechanize
# from IPython.core.display import HTML
import sys
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_referer(False)
    browser.set_handle_refresh(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    # =============================================
    key = "Ingeniero de sistemas"
    # =============================================
    browser.open(
        "https://aptitus.com/buscar-trabajo-en-peru?q=" + key.replace(' ', '-')
    )
    # https://aptitus.com/buscar-trabajo-en-peru/de-tecnologia-sistemas-y-telecomunicaciones

    jobLinks = get_links_pages(browser)
    print "=================="
    print "Links:", len(jobLinks)
    data = get_data(browser, jobLinks)
    print "Datos:", len(data)
    print "=================="


def get_links_pages(browser):
    jobLinks = []
    latest_pagination = [
        l for l in browser.links()
        if l.text.isdigit()
    ][-1]
    for d in browser.links():
        if d.text.isdigit():
            browser.follow_link(d)
            jobLinks += [
                l for l in browser.links()
                if l.url.startswith("https://aptitus.com/ofertas-de-trabajo/")
            ]
    jobLinks = jobLinks + get_links_sig(browser, latest_pagination)
    return jobLinks


def get_links_sig(browser, latest_pagination):
    jobLinks = []
    temp = [l for l in browser.links() if l.text.isdigit()]
    if temp:
        links = [i for i in temp if int(i.text) > int(latest_pagination.text)]
        latest_pagination = temp[-1]
        for link in links:
            browser.follow_link(link)
            jobLinks += [
                l for l in browser.links()
                if l.url.startswith("https://aptitus.com/ofertas-de-trabajo/")
            ]
        if links:
            jobLinks += get_links_sig(browser, latest_pagination)
        return jobLinks


def get_data(browser, jobLinks):
    data = []
    for j in jobLinks:
        browser.follow_link(j)
        print j.url
        soup = BeautifulSoup(browser.response().read(), "html.parser")
        if not soup.body.find(
            text='Este aviso ha finalizado, puedes ver otros avisos similares'
        ):
            data.append(
                dict(
                    url=j.url,
                    company=soup.select('a.b-job-detail_subtitle')[0].string,
                    title=soup.select('h1.b-job-detail_title')[0].string,
                    location=soup.body.find(
                        text='Ubicación').parent.next_sibling.string,
                    description=soup.select('.b-job-info')[0].get_text(),
                    html=str(soup.select('.b-job-info')[0]),
                    date=soup.body.find(
                        text='Publicado').parent.next_sibling.string,
                    area=soup.body.find(text='Área').parent.next_sibling.string
                )
            )
    return data

if __name__ == "__main__":
    main()
