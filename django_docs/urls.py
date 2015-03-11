from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django_docs.views import SettingsApiView

urlpatterns = patterns('',
    url(r'^api/settings/$', SettingsApiView.as_view()),
    url(r'^settings$', TemplateView.as_view(template_name='django_settings.html')),
)
