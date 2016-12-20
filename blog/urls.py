from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$',show_bloog),
    url(r'^(?P<bloog_id>[0-9]+)',get_bloog

        )
]