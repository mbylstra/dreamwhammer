from django.core.exceptions import ObjectDoesNotExist
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from dreamwhammer.scraper import scrape_list_view
from dreamwhammer.views import DreamWhammerListView

from wham.apis.lastfm.models import LastFmArtist

gigs_list_spec = {
    'url': 'http://www.beat.com.au/gig-guide/',
    'object_selector': '#block-system-main .text',
    'fields': {
        'name': '.gig-title a',
        'venue': '.icon a',
        'date': '.date-display-single',
        'price': '.price',
    },
    'next_page_selector': '.date-prev a'
}

def get_gigs_n_photos(date):

    gigs = scrape_list_view(gigs_list_spec, page=date)
    for gig in gigs:
        try:
            lastfm_artist = LastFmArtist.objects.wham_get(pk=gig['name'])
            gig['image_url'] = lastfm_artist.mega_image_url
            gig['num_listeners'] = lastfm_artist.num_listeners
        except ObjectDoesNotExist:
            gig['image_url'] = None
            gig['num_listeners'] = 0
        except ValueError:
            gig['image_url'] = None
            gig['num_listeners'] = 0

    gigs = sorted(gigs, key=(lambda gig: int(gig['num_listeners'])), reverse=True)
    return gigs

class GigsApiView(DreamWhammerListView):
    spec = gigs_list_spec

class GigsPhotosApiView(APIView):

    renderer_classes = (JSONRenderer,)

    def get(self, _request, date):
        return Response(get_gigs_n_photos(date=date))
