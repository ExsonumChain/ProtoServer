import graphene

from graphene_django.types import DjangoObjectType

from .models import *


class StationType(DjangoObjectType):
    class Meta:
        model = Station

class TrackType(DjangoObjectType):
    class Meta:
        model = Track

class AudioFileType(DjangoObjectType):
    class Meta:
        model = AudioFile

class Query(graphene.AbstractType):
    
    all_stations = graphene.List(StationType)
    all_tracks = graphene.List(TrackType)
    all_audiofiles = graphene.List(AudioFileType)
    
    station = graphene.Field(StationType,
                              id=graphene.Int(),
                              name=graphene.String())
    track = graphene.Field(TrackType,
                                id=graphene.Int(),
                                name=graphene.String())
    audiofile = graphene.Field(AudioFileType,
                                id=graphene.Int(),
                                name=graphene.String())

    def resolve_all_stations(self, args, context, info):
        return Station.objects.all()
    def resolve_all_tracks(self, args, context, info):
        # We can easily optimize query count in the resolve method
        return Track.objects.select_related('station').all()
    def resolve_all_all_audiofiles(self, args, context, info):
        # We can easily optimize query count in the resolve method
        return AudioFile.objects.select_related('track').all()
    def resolve_station(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Station.objects.get(pk=id)

        if name is not None:
            return Station.objects.get(name=name)

        return None

    def resolve_track(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Track.objects.get(pk=id)

        if name is not None:
            return Track.objects.get(name=name)

    def resolve_audiofile(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return AudioFile.objects.get(pk=id)

        if name is not None:
            return AudioFile.objects.get(name=name)

        return None