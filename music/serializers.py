from rest_framework import serializers 
from .models import Song

class SongSerializers(serializers.ModelSerializers):
    class Meta:
        model = Song
        fields = ['id', 'title', 'album', 'genre', 'release_date']

        