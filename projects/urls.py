from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView, ProjectUpdateView,
    ProjectDeleteView,
    ProjectCreateView,
    SearchResultsListView,
)

# app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),

    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('new/', ProjectCreateView.as_view(), name='project_new'),
]
