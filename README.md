# DreamWhammer
Easily create RESTful APIs for any website.

DreamWhammer combines requests, BeautifulSoup and DjangoRestFramework to create RESTful APIs for websites that don't have them (even ones created in Dream Weaver).

For example, the following is all that is required to create an api endpoint for crazysales.com.au:

```
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
```
