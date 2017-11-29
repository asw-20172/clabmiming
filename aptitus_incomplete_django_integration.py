# coding: utf-8
import mechanize
# from IPython.core.display import HTML
import sys
from bs4 import BeautifulSoup
import os
import logging
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

from apps.collection.models.palabra_clave import Palabra_clave
from apps.collection.models.data_red_social import Data_red_social
from apps.collection.models.consulta import Consulta
from apps.collection.models.carrera import Carrera
from apps.collection.models.red_social import Red_social
reload(sys)
sys.setdefaultencoding('utf-8')
logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)


def main():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_handle_referer(False)
    browser.set_handle_refresh(False)
    browser.addheaders = [('User-agent', 'Firefox')]
    # =============================================
    carrera = Carrera.objects.all().first()
    palabras_clave = Palabra_clave.objects.filter(carrera=carrera)

    # https://aptitus.com/buscar-trabajo-en-peru/de-tecnologia-sistemas-y-telecomunicaciones
# coding: utf-8

    # print "##################"
    # for p in palabras_clave:
    #     # =============================================
    #     browser.open(
    #         "https://aptitus.com/buscar-trabajo-en-peru?q=" +
    #         p.nombre.replace(' ', '-')
    #     )
    #     jobLinks = get_links_pages(browser)
    #     print "=================="
    #     print "Links:", len(jobLinks)
    #     data = get_data(browser, jobLinks)
    #     Data_red_social.bulk_create(data)
    #     print "Datos:", len(data)
    #     print "=================="
    # red_social = Red_social.get(nombre="Aptitus")
    # Consulta.create(descripcion="Primera Consulta", red_social=red_social)


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
                Data_red_social(
                    url=j.url,
                    titulo=soup.select('h1.b-job-detail_title')[0].string,
                    institucion=soup.select(
                        'a.b-job-detail_subtitle')[0].string,
                    lugar=soup.body.find(
                        text='Ubicación').parent.next_sibling.string,
                    descripcion_empleo=soup.select(
                        '.b-job-info')[0].get_text(),
                    descripcion_empleo_html=str(soup.select('.b-job-info')[0]),
                    fecha=soup.body.find(
                        text='Publicado').parent.next_sibling.string,
                    sector=soup.body.find(
                        text='Área').parent.next_sibling.string
                )
            )
    return data
if __name__ == "__main__":
    main()
