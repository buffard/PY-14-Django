from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Artists


def index(request):
  latest_artist = Artists.objects.order_by('name')
  context = {
    'latest_artist': latest_artist,
  }
  return render(request, 'artists/index.html', context)

# Define a view to return a template that displays the details of a 
# specific artist, and list all of the songs related to that artist.

def detail(request, artistid_id):
    artist = get_object_or_404(Artists, pk=artistid_id)
    
    return render(request, 'artists/detail.html', {'artist': artist})
