from django.contrib import admin

from .models import Track

class TrackAdmin(admin.ModelAdmin):
	list_display = ('artist', 'title','order','track_file','album', 'player', 'es_algo')
	list_filter = ('artist','album')
	# Buscar por el first name del artista, para acceder usamos __
	search_fields = ('title','artist__first_name')
	list_editable = ('title', 'album')
	raw_id_fields = ('artist', )

	# return obj.title = 'ckan'
	def es_algo(self, obj):
		return obj.id == 1

	es_algo.boolean = True

admin.site.register(Track, TrackAdmin)

			# Minuto 14