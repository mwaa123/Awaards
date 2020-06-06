from django.conf.urls import url
from . import views
from .views import ProjectListView,ProjectDetailView
from django.urls import path
urlpatterns=[
    url('^$',ProjectListView.as_view(), name= 'welcome'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='detail'),
]