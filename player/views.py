from django.shortcuts import  render, redirect
from player.forms import SearchForm
from pyglet import media
from IPython.display import Audio
import pafy


# Create your views here.

def index(request):
    form = SearchForm()
    context = {'form':form}
    return render(request, 'index.html', context=context)

def player(request):
    context = {'title' : None, 'ytUrl' : None}
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            ytLink = form.cleaned_data['searchbBox']
            try:
                audioInfo = pafy.new(ytLink)
                bestAudio = audioInfo.getbestaudio(preftype="webm")
                context['title'] = audioInfo.title
                context['ytUrl'] = bestAudio.url
            except:
                return redirect('/')
        return render(request, 'player.html', context=context)
    return render(request, 'player.html', context=context)
    
