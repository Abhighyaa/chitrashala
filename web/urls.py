from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^phad/$', views.phad, name='phad'),
    url(r'^phad-making/$', views.phadmaking, name='phadmaking'),
    url(r'^phad-perfomance/$', views.phadperfomance, name='phadperfomance'),
    url(r'^contactus/$', views.contact, name='contact'),
    url(r'^awards/$', views.awards, name='awards'),
    url(r'^blog/$', views.blog, name='blog'),
]