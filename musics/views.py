from django.shortcuts import render, redirect, get_object_or_404
from .models import Music

# Create your views here.
    
def main(request):
    musics = Music.objects.all()
    return render(request, 'musics/main.html', {'musics':musics})
   

def show(request, music_id):
    music = get_object_or_404(Music, id=music_id) 
    return render(request, 'musics/show.html', {'music':music})

def new(request):
    return render(request, 'musics/new.html')

def create(request):
    user = request.user
    if request.method =="POST":
        music = Music()
        music.writer = user
        music.title = request.POST.get('title')
        music.singer = request.POST.get('singer')
        music.genre = request.POST.get('genre')
        music.lyrics = request.POST.get('lyrics')
        music.link = request.POST.get('link')
        music.save()

    return redirect('musics:main')


def update(request, music_id):
    if request.method == "POST":
        music = get_object_or_404(Music, pk=music_id)
        music.title = request.POST.get('title')
        music.singer = request.POST.get('singer')
        music.lyrics = request.POST.get('lyrics')
        music.genre = request.POST.get('genre')
        music.link = request.POST.get('link')
        music.save()

    return redirect('musics:show', music_id)


def delete(request, music_id):
    get_object_or_404(Music, pk=music_id).delete()
    return redirect('musics:main')

def edit(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    return render(request, 'musics/edit.html', {'music':music})

def search(request):
    search = request.GET.get('search')
    search_result = Music.objects.filter(title__contains=search)
    return render(request,'musics/search.html', {'search_result':search_result})