from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .scraper import scrape_list_view


class DreamWhammerListView(APIView):

    renderer_classes = (JSONRenderer,)

    def get(self, _request):
        content = scrape_list_view(self.spec)
        return Response(content)