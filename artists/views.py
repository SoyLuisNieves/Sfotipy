from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist
	context_object_name = 'artist'

	def get_template_names(self):
		return 'artist.html'

# Create your views here.

# Vistas con funciones es una funcion que recibe el metodo request y retorna una respuesta

# Vista basada en clase 