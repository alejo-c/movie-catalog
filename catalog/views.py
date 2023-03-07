from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Movie
from .forms import MovieForm


def index(req):
    return render(req, "movies/index.html")


def catalog(req):
    movies = Movie.objects.all()
    return render(req, "movies/catalog.html", {"movies": movies})


def view(req, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(req, "movies/movie.html", {"movie": movie})


@login_required
def add(req):
    form = MovieForm(req.POST or None, req.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("catalog")
    return render(req, "movies/add.html", {"form": form})


@login_required
def edit(req, movie_id):
    movie = Movie.objects.get(id=movie_id)
    form = MovieForm(req.POST or None, req.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("catalog")
    return render(req, "movies/edit.html", {"form": form})


@login_required
def remove(req, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect("catalog")


@login_required
def logout_view(req):
    logout(req)
    return render(req, "auth/logout.html")
