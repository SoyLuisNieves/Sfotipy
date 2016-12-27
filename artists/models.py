from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank=True)
	biography = models.TextField()
	favorite_songs = models.ManyToManyField('tracks.Track', blank=True, related_name='is_favorite')

	def __unicode__(self):
		return self.first_name