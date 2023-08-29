from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Member
from .forms import SignUpForm, SignInForm


class SignUpView(CreateView):
    model = Member
    template_name = "sign-up/sign-up.html"
    form_class = SignUpForm

    def get_success_url(self):
        return reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = self.form_class
        return context

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"Error: {error}")
        return super().form_invalid(form)


class SignInView(LoginView):
    template_name = "sign-in/sign-in.html"
    form_class = SignInForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, "The Username and Password do not match!")
        return super().form_invalid(form)
