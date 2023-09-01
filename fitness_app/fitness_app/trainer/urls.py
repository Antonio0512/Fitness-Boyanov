from django.urls import path
from .views import TrainersListView, TrainerDetailsView

urlpatterns = [
    path("", TrainersListView.as_view(), name='trainers-list'),
    path("<int:pk>/details/", TrainerDetailsView.as_view(), name="trainer-details")
]