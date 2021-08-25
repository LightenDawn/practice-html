from django.shortcuts import render, get_object_or_404
from .models import videos
from django.conf import settings
from django.http import HttpResponse


def index(request):
    movie = videos.objects.all()
    return render(request, "movie_html/video.html",{
        "url": movie,
    })