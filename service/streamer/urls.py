from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^read_log/', views.read_log, name='read_log'),
]