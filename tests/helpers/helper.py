import urlparse

__author__ = 'tan'



class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)



class Component(object):
    def __init__(self, driver):
        self.driver = driver
