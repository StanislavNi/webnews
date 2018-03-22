from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
