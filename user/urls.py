from django.urls import path
from . import views


urlpatterns = [
    path("", views.userpage, name="userpage"),
    path("logout/", views.logout, name="logout"),

]