from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from blockchain import views
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from schema import schema

router = routers.DefaultRouter()
router.register(r'audiofiles', views.AudioFileViewSet)
router.register(r'stations', views.StationViewSet)
router.register(r'tracks', views.TrackViewSet)

urlpatterns = [
    url(r'^blockchain/', include('blockchain.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api/tracks/stations/(?P<stations>.+)/$', views.TrackList.as_view()),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^graphiql', GraphQLView.as_view(graphiql=True, schema=schema)),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view( schema=schema))),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
