from django.shortcuts import render
from poll.models import Films, Users, Genres, Cartoons, Poll


def sign(request):
    film = Films.objects.all()
    return render(request, 'sign.html', {'film': film})


def project(request):
    genres = Genres.objects.all()
    return render(request, 'project.html', {'genre': genres})


def koru(request):
    users = Users.objects.all()
    return render(request, 'koru.html', {'user': users})

def cartoons(request):
    film = Cartoons.objects.all()[1]
    return render(request, 'cartoons.html',{'film':film})

def top_films(request):
    return render(request, 'top_films.html')

def contacts(request):
    return render(request, 'contacts.html')





