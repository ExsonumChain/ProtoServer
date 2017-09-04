from .models import *
from rest_framework import viewsets
from .serializer import *
from rest_framework import generics


class AudioFileViewSet(viewsets.ModelViewSet):
    queryset = AudioFile.objects.all()
    serializer_class = AudioFileSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackList(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        stations = self.kwargs['stations'].split(',')
        return Track.objects.filter(station__id__in=stations)
