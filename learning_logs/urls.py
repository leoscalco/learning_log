# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Exibir todos os tópicos.
    url(r'^topics/$', views.topics, name='topics'),
     # Detail page for a single topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Página apra adicionar um novo tópico
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Página para adicionar nova entrada
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Página para editar entrada
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]