from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profolio/", views.userpage, name= "profolio"),
    path("logout/", views.logout, name="logout"),
]