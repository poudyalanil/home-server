from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="music_home")]
