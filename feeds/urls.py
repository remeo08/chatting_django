from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllFeed.as_view())
]