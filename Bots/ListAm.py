from Scrapers.downloader import Downloader


class ListAmBot:
    __LOGIN_EMAIL = 'firstbot1990@gmail.com'
    __LOGIN_PASSWORD = 'firstbot1990'
    __LOGIN_URL = 'https://www.list.am/login'

    def add_flat_announcement(self):
        data_dict = {'your_email': self.__LOGIN_EMAIL, 'password': self.__LOGIN_PASSWORD}
        proxy = '61.5.207.102:80'
        opener = Downloader.login_cookies(self.__LOGIN_URL, data_dict, proxy)
        add_page_html = opener.open('https://www.list.am/add/58').read()
        form = Downloader.parse_form(add_page_html)
        for k in form:
            print(k, ' : ', form[k])


if __name__ == "__main__":
    from Helpers.proxy_manager import ProxyManager
    from DB.mongo_cache import MongoCache
    from datetime import timedelta
    proxyCache = MongoCache(collection='proxy', client=None,expires=timedelta(minutes=50))
    mgr = ProxyManager(cache=proxyCache)
    proxies = mgr.get_checked_proxy_list(timeout=5)
    print(proxies)
    print('total count',len(proxies))
