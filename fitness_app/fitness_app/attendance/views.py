from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import AttendanceAddForm
from .models import Attendance


class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = "attendance/attendance-list.html"
    context_object_name = "attendances"

    def get_queryset(self):
        return Attendance.objects.filter(user=self.request.user)


class AttendanceAddView(LoginRequiredMixin, CreateView):
    model = Attendance
    template_name = "attendance/attendance-add.html"
    form_class = AttendanceAddForm

    def get_success_url(self):
        return reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = self.form_class
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, 'Attendance added successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error adding attendance. Please check your input and try again.')
        return super().form_invalid(form)
