from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from beat_gigs.views import GigsApiView, GigsPhotosApiView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/gigs-simple/', GigsApiView.as_view()),
    url(r'^api/gigs/(?P<date>[\d\-]+)/$', GigsPhotosApiView.as_view()),
    url(r'^gigs/', TemplateView.as_view(template_name='gigs.html')),
    url(r'^django-docs/', include('django_docs.urls')),
    url(r'^crazy-sales/', include('crazy_sales.urls')),
)
