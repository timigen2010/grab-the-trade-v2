from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random


class Spider:

    def __init__(self):
        self.ua = UserAgent()
        self.proxies = []

        self.__fill_proxies__()

    def __fill_proxies__(self):
        if len(self.proxies) < 10:
            proxies_req = Request('https://www.sslproxies.org/')
            proxies_req.add_header('User-Agent', self.ua.random)
            proxies_doc = urlopen(proxies_req).read().decode('utf8')

            soup = BeautifulSoup(proxies_doc, 'html.parser')
            proxies_table = soup.find(id='proxylisttable')

            for row in proxies_table.tbody.find_all('tr'):
                self.proxies.append({
                    'ip': row.find_all('td')[0].string,
                    'port': row.find_all('td')[1].string
                })

    def __get_random_proxy__(self):
        self.__fill_proxies__()
        return random.randint(0, len(self.proxies) - 1)

    def execute_request(self, request):

        proxy_index = self.__get_random_proxy__()
        proxy = self.proxies[proxy_index]

        page = False
        exceptions_count = 0
        while not page or exceptions_count > 25:
            req = Request(request)
            req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
            try:
                page = urlopen(req).read().decode('utf8')
            except:
                del self.proxies[proxy_index]
                proxy_index = self.__get_random_proxy__()
                proxy = self.proxies[proxy_index]

        return page
