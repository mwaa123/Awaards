from django.conf.urls import url
from . import views
from .views import ProjectListView,ProjectDetailView,ProjectCreateView,ProjectDeleteView,ProjectUpdateView
from django.urls import path
urlpatterns=[
    url('^$',ProjectListView.as_view(), name= 'welcome'),
    path('project/<int:pk>/',ProjectDetailView.as_view(),name='detail'),
    url('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('search/',views.search_results, name = 'search_results'),
    path('project/<int:pk>/vote',VoteCreateView.as_view(), name = 'project-vote'), 

]