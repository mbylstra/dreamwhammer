import os
import sys
import django

project_dir = os.path.realpath(__file__)
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dreamwhammer.settings'
django.setup()
from django.conf import settings

######################################

from beat_gigs.views import get_gigs_n_photos
from wham.apis.lastfm.models import LastFmArtist

# from bs4 import BeautifulSoup
# import requests
#
#
# NUM_PAGES = 5
#
# next_page_selector = '.date-prev a'
#
#
# class DreamWhammerSpec:
#     pass
#
# class GigDM(DreamWhammerSpec):
#
#     pass
#
# gig_dm = {
#     'url': 'http://www.beat.com.au/gig-guide/',
#     'object_selector': '#block-system-main .text',
#     'fields': {
#         'name': '.gig-title a',
#         'venue': '.icon a',
#         'date': '.date-display-single',
#         'price': '.price',
#     },
#     'next_page_selector': '.date-prev a'
# }
#
#
# def scrape(spec, num_pages=5):
#     curr_page = spec['url']
#     data = []
#     for x in range(num_pages):
#         soup = BeautifulSoup(requests.get(curr_page).content)
#         object_soups = soup.select(spec['object_selector'])
#         for object_soup in object_soups:
#             curr_object = {}
#             for field_name, selector in spec['fields'].iteritems():
#                 curr_object[field_name] = object_soup.select(selector)[0].text
#             data.append(curr_object)
#         curr_page = soup.select(spec['next_page_selector'])[0]['href']
#     return data
#
# data = scrape(gig_dm)
# print data


# artist = LastFmArtist.objects.wham_get(pk='jonny telafone', wham_use_cache)
# print artist

# get_gigs_n_photos('2015-03-01')

# for artist in LastFmArtist.objects.all():
#     print '----------------------'
#     print artist
#     print artist.mega_image_url
#     print artist.num_listeners


import hashlib
from django.core.cache import caches
web_request_cache = caches['wham_web_request']
web_request_cache.set('test1_key', 'test1 value', None)

print web_request_cache.get('test1_key')

# def make_web_request(url):
#     cache_key = hashlib.md5(url).hexdigest()
#     response = web_request_cache.get(cache_key)
#     if not response:
#         web_request_cache.set(cache_key, response)
#     return response
