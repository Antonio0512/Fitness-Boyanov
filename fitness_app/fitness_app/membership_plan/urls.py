from django.urls import path
from .views import MembershipListView, MembershipDetailsView

urlpatterns = [
    path("", MembershipListView.as_view(), name="membership-plans"),
    path("<int:pk>/details/", MembershipDetailsView.as_view(), name="membership-plan-details")
]
