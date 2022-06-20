from django.shortcuts import render
from .serializers import SongSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Song

# Create your views here.

class SongList(APIView):

    def get(self,request):
        song = Song.objects.all()
        serializer = SongSerializers(song, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SongSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

