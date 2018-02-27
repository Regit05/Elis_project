from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.second_view, name='second_view'),
]