# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Music


class Index(ListView):
    model = Music
    template_name = "musics/index.html"
