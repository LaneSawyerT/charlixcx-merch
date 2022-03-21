from . import views
from django.urls import path

urlpatterns = [
    path("", views.NewsPostList.as_view(), name="news"),
]