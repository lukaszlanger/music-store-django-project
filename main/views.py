# main/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Album, Sale

@login_required
def home(request):
    albums = Album.objects.all()
    return render(request, 'main/home.html', {'albums': albums})

@login_required
def buy_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'main/finalize_order.html', {'album': album})

@login_required
def finalize_order(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    Sale.objects.create(user=request.user, album=album)
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('login')
