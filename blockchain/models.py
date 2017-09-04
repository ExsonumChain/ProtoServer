from django.db import models


class AudioFile(models.Model):
    file = models.FileField(upload_to='audiofiles/')
    length_seconds = models.PositiveIntegerField(default=0)
    size_bytes = models.PositiveIntegerField(null=True, blank=True)
    format = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.file)


class Station(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='stations/')
    subscription_count = models.PositiveIntegerField(default=0)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Track(models.Model):
    station = models.ForeignKey(Station, related_name='tracks')
    audio_file = models.ForeignKey(AudioFile, related_name='audiofiles')
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=2000)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='tracks/')
    like_count = models.PositiveIntegerField(default=0)
    report_count = models.PositiveIntegerField(default=0)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


