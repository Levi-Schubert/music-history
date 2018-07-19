from django.shortcuts import render, get_object_or_404

from .models import Artist, Details

# Create your views here.
def index(request):
	all_artists = Artist.objects.all()
	context = {"all_artists" : all_artists}
	return render(request, "history/index.html", context)


def details(request, artist_id):
	artist = get_object_or_404(Artist, pk=artist_id)
	return render(request, "history/details.html", {"artist" : artist})