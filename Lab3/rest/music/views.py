from django.shortcuts import render
from .models import Music
from .serializers import MusicSerializer, MusicListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MusicListView(APIView):
    
    def get(self, request, format=None):
        snippets = Music.objects.all()
        serializer = MusicListSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicByIdView(APIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    def get_object(self, pk):
        try:
            return Music.objects.get(id=int(pk))
        except Music.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MusicListSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = MusicSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    