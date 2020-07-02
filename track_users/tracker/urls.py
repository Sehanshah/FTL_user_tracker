from django.conf.urls import url
from tracker.views import *

urlpatterns = [
    url(r'^$', home_page, name="tracker.homepage"),
    url(r'users_list/$', users_list, name="tracker.users_list"),
]
