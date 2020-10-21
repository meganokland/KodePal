from django.urls import path

from .views import (ProfileDetailView, ProfileUpdateView, ProfileListView,
                    ProfileCreateView, ProfileDeleteView, ProfileResultsListView
                    )

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='profile_list'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('search/', ProfileResultsListView.as_view(), name='search_results'),

    path('edit/<int:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('delete/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
    path('new/', ProfileCreateView.as_view(), name='profile_new'),
]
