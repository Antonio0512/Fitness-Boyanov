from django.views.generic import ListView, DetailView

from .models import MembershipPlan


class MembershipListView(ListView):
    model = MembershipPlan
    template_name = "membership-plans/membership-plans.html"
    context_object_name = "membership_plans"


class MembershipDetailsView(DetailView):
    model = MembershipPlan
    template_name = "membership-plans/membership-details.html"
    context_object_name = "membership_plan"