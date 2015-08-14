from django.conf.urls import url

from . import views

print views.index

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),
	url(r'^(?P<question_id>[0-9]+)/questao/$', views.editar_questao, name="editar_questao"),
	url(r'^questao/$', views.editar_questao, name="nova_questao")
]