from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from crazy_sales.views import HotDealsApiView

urlpatterns = patterns('',
    url(r'^api/hot-deals/$', HotDealsApiView.as_view()),
)
