from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm


class UserRegistrationCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/registration.html'
    title = 'Registration'
    success_message = 'Success registration!'

    def get_success_url(self):
        return reverse_lazy('todos:current')


@login_required
def user_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('todos:current')
