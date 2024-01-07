from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomView.as_view(), name="home"),
]
