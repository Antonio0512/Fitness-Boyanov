from django.views.generic import ListView, DetailView
from .models import Trainer

class TrainersListView(ListView):
    model = Trainer
    template_name = "trainers/trainers.html"
    context_object_name = "trainers"


class TrainerDetailsView(DetailView):
    model = Trainer
    template_name = "trainers/trainer-details.html"
    context_object_name = "trainer"