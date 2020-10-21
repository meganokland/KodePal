from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Profile


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'profiles/profile_list.html'
    login_url = 'profile_login'


class ProfileDetailView(LoginRequiredMixin,
                        PermissionRequiredMixin,
                        DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'
    login_url = 'profile_login'
    permission_required = 'profiles.special_status'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = {'first_name', 'description'}
    template_name = 'profiles/profile_edit.html'
    success_msg = 'Profile Updated'


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profiles/profile_delete.html'
    success_url = reverse_lazy('profile_list')


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profiles/profile_new.html'
    fields = ('first_name', 'location', 'description')


class ProfileResultsListView(ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'profiles/profile_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Profile.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
