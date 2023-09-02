from django.views.generic import ListView
from .models import Photo


class GalleryListView(ListView):
    model = Photo
    template_name = "gallery/gallery-list.html"
    context_object_name = "images"
