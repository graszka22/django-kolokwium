from django.conf.urls import url

from . import views

app_name = 'kolokwium'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<kolokwium_id>[0-9]+)/$', views.kolokwium, name='kolokwium'),
    url(r'^(?P<kolokwium_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^(?P<kolokwium_id>[0-9]+)/(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
]
