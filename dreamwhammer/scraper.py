import hashlib
from bs4 import BeautifulSoup
import requests
from django.core.cache import caches
web_request_cache = caches['wham_web_request']

def make_web_request(url):
    cache_key = hashlib.md5(url).hexdigest()
    response = web_request_cache.get(cache_key)
    if not response:
        response = requests.get(url).content
        web_request_cache.set(cache_key, response)
    return response


def scrape_list_view(spec, page=None):

    data = []
    url = spec['url']
    if page:
        url += page
    print 'url', url
    content = make_web_request(url)
    soup = BeautifulSoup(content)
    object_soups = soup.select(spec['object_selector'])
    for object_soup in object_soups:
        try:
            curr_object = {}
            for field_name, selector in spec['fields'].iteritems():
                curr_object[field_name] = object_soup.select(selector)[0].text
            data.append(curr_object)
        except IndexError:
            pass #ignore
    return data



