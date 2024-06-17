from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, UpdateView
from .models import User



# Create your views here.
class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'profile/profile.html'
    def get_queryset(self):
        return User.objects.for_user(self.request.user)

    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    client = Client.objects.for_user(self.request.user).get(pk=13)
    #    context['client'] = client
    #    print(client)
    #    return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'profile/profile_form.html'
    fields = ['first_name', 'last_name', 'email']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование информации профиля"
        context['client'] = self.object.pk
        return context

    def get_success_url(self):
        return reverse('profile')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form