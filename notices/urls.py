from django.urls import path
from . import views

app_name = "notice"

urlpatterns = [
    path("search/", views.search, name="search"),
  
]