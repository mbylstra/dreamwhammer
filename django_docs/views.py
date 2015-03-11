from dreamwhammer.views import DreamWhammerListView

settings_spec = {
    'url': 'https://docs.djangoproject.com/en/1.7/ref/settings/',
    'object_selector': '.section',
    'fields': {
        'variable': 'h3',
        'default': '.literal',
    },
}

class SettingsApiView(DreamWhammerListView):
    spec = settings_spec

