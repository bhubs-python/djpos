from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.logout_request, name='logout'),
]
