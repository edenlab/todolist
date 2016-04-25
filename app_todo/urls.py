from django.conf.urls import patterns, url
from app_todo import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^new$', views.task_create, name='task_new'),
    url(r'^edit/(?P<id>\d+)$', views.task_update, name='task_edit'),
    url(r'^delete/(?P<id>\d+)$', views.task_delete, name='task_delete'),
    url(r'^task-done/(?P<id>\d+)/$', views.mark_as_done, name='task-done')

)
