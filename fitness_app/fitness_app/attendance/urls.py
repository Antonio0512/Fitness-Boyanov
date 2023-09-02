from django.urls import path
from .views import AttendanceListView, AttendanceAddView

urlpatterns = [
    path("", AttendanceListView.as_view(), name="attendance-list"),
    path("add/", AttendanceAddView.as_view(), name="attendance-add")
]
