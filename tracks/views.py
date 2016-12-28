import json
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from .models import Track

def track_view(request, title):
	"""try:
		track = Track.objects.get(title=title)
	except
		raise Http404
	"""
	track = get_object_or_404(Track, title=title)

	#Respuesta JSON
	data = {
		'title': track.title,
		'order': track.order,
		'album': track.album,
		'artist': {
			'name': track.artist.first_name,
			'biography': track.artist.biography,
		}
	}
	# import ipdb; ipdb.set_trace()
	# De JSON a cadena
	# json_data = json.dumps(data)

	# De cadena a JSON
	# json.loads(string_json)

	# Hay que indicar al response que es un JSON, indicar tipo de peticion
	# application/json para saber que envian o reciben un JSON
	# return HttpResponse(json_data, content_type='application/json')

	return render(request, 'track.html', {'track': track})