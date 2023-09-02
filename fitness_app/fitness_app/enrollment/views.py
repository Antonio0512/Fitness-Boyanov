from django.contrib import messages
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .models import Member
from .forms import SignUpForm, SignInForm, ProfileUpdateForm

User = get_user_model()


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


class LogOutView(LoginRequiredMixin, LogoutView):
    template_name = "logout/logout.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class ProfileDetailsView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "enroll/profile-details.html"
    context_object_name = "user"


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "enroll/profile-edit.html"
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy("profile-details", kwargs={"pk": self.request.user.pk})

    def form_valid(self, form):
        try:
            instance = form.save(commit=False)
            instance.user = self.request.user
            instance.save()
            form.save_m2m()
        except IntegrityError:
            messages.error(self.request, 'Error updating profile. Please check your input and try again.')
            return redirect('profile-edit', kwargs={"pk": self.request.user.pk})
