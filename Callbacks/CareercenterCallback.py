import re, lxml, lxml.html
from DB.mongo import MongoManager
import json

def clear_key(key):
    return key.replace(':', '').replace(' ', '_').replace('/', '').strip()


def clear_text(text):
    clean_text = text.strip()
    # clear usicode spec chars
    return re.sub(r'[^\x00-\x7F]+', '', clean_text)


def get_job_dict_from_html(html):
    h = lxml.html.fromstring(html)
    desc_dict = {}
    for p in h.xpath('//p'):
        try:
            key = clear_key(p.xpath('b/text()')[0])
            desc_dict[key] = clear_text(p.xpath('text()')[0])
        except:
            pass
    return desc_dict


class careeercenterCalback:
    def __init__(self):
        self.__dbMgr = MongoManager()

    def __call__(self, url, html):
        job_dict = get_job_dict_from_html(html)
        self.__dbMgr.Insert('parsed_jobs','career_center',job_dict)
