from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sfotipy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tracks/(?P<title>[\w\-]+)', 'tracks.views.track_view', name='track_view'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^<signin</signin>/', 'userprofiles.views.signin', name='signin'),
]
