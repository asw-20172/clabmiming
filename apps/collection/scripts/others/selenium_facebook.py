from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class Facebook(object):

    def __init__(self, path_to_chromedriver):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.browser = webdriver.Chrome(
            executable_path=path_to_chromedriver,
            chrome_options=chrome_options)

    def login(self, user, password):
        self.browser.get('https://www.facebook.com/login/')
        self.browser.find_element_by_name('email').send_keys(user)
        self.browser.find_element_by_name('pass').send_keys(password)
        self.browser.find_element_by_id('loginbutton').submit()

    def dislake_pages(self, scroll_pause_time=2):
        URL = 'https://www.facebook.com/pages/?category=liked'
        self.browser.get(URL)
        self.browser.maximize_window()
        last_height = self.browser.execute_script(
            "return document.body.scrollHeight")
        while True:
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = self.browser.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        liked_page_urls = [
            elem.get_attribute("href")
            for elem in self.browser.find_elements_by_class_name('_5l2d')
        ]
        for i in liked_page_urls:
            self.browser.get(i)
            try:
                self.browser.find_element_by_class_name('likedButton').click()
                self.browser.execute_script(
                    "document.querySelectorAll('a[data-testid=page_unlike_item_test_id]')[0].click()"
                )
            except Exception, e:
                print e

    def close(self):
        # Logout script
        self.browser.find_element_by_id('pageLoginAnchor').click()
        time.sleep(2)
        self.browser.execute_script(
            'document.querySelector("#BLUE_BAR_ID_DO_NOT_USE > div > div > div.uiScrollableAreaWrap.scrollable > div > div > ul > li._54ni.navSubmenu._6398._64kz.__MenuItem > a").click()'
        )
        # Browser quit
        self.browser.quit()

if __name__ == "__main__":
    path_to_chromedriver = '/home/yuselenin/Projects/clabmining/apps/collection/scripts/others/chromedriver'
    facebook = Facebook(path_to_chromedriver)
    facebook.login('your username', 'your password')
    facebook.dislake_pages()
    facebook.close()
