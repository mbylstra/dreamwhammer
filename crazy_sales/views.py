from dreamwhammer.views import DreamWhammerListView

class HotDealsApiView(DreamWhammerListView):
    spec = {
        'url': 'http://www.crazysales.com.au/hottest-deals',
        'object_selector': '.border',
        'fields': {
            'name': 'h5 a',
            'price': '.newprice',
            'saving': '.saveicon',
        },
    }
