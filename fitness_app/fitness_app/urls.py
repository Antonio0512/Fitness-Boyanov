from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("fitness_app.base.urls")),
    path("enrollment/", include("fitness_app.enrollment.urls"))
]
