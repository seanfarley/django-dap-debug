from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from .models import User


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        """Return all the users sorted by username."""
        return User.objects.order_by('-username')


class InfoView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'users/info.html'
