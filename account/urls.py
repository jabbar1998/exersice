from django.urls import path
from . import views

urlpatterns = [path("register", views.UserRegisteration.as_view(), name="register")]
