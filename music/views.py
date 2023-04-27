from django.shortcuts import render, redirect

from music.models import Music
from music.forms import MusicForm

def home(request):
    return render(request, 'music/home.html')

def create_musics(request):
    form = MusicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_musics')

    return render(request, 'music/music_form.html', {'form': form})


def update_music(request, id):
    music = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, instance=music)

    if form.is_valid():
        form.save()
        return redirect('list_musics')

    return render(request, 'music/music_form.html', {'form': form, 'music': music})


def delete_music(request, id):
    music = Music.objects.get(id=id)

    if request.method == 'POST':
        music.delete()
        return redirect('list_members')

    return render(request, 'music/music_delete_confirm.html', {'musics': music})
