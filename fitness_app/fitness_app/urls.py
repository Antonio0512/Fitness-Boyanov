from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("fitness_app.base.urls")),
    path("enrollment/", include("fitness_app.enrollment.urls")),
    path("membership-plans/", include("fitness_app.membership_plan.urls")),
    path("trainers/", include("fitness_app.trainer.urls")),
    path("profile/", include("fitness_app.enrollment.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
