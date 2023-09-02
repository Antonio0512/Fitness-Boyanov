from django.urls import path
from . import views

urlpatterns = [
    path("sign-up/", views.SignUpView.as_view(), name='sign-up'),
    path("sign-in/", views.SignInView.as_view(), name='sign-in'),
    path("logout/", views.LogOutView.as_view(), name="logout"),

    path("<int:pk>/details/", views.ProfileDetailsView.as_view(), name="profile-details"),
    path("<int:pk>/edit/", views.ProfileEditView.as_view(), name="profile-edit")
]
