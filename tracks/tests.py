from django.test import TestCase

# Create your tests here.

from .models import Track
from albums.models import Album
from artists.models import Artist

class TestTrack(TestCase):

	def setUp(self):
		self.artist = Artist.objects.create(first_name='akil', last_name='ammar')
		self.album = Album.objects.create(title='heroes', artist=self.artist)
		self.track = Track.objects.create(title='la vida es', artist=self.artist, album=self.album, order=1, track_file='media/sa')

	def test_usuario_logueado(self):
		res = self.client.get('/tracks/%s' % self.track.title)
		self.assertEqual(res.status_code, 302)