from django.shortcuts import render
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer
from django.http import HttpResponse,JsonResponse,HttpRequest

# Create your views here.

class ListSongsView(generics.ListAPIView):
    queryset=Songs.objects.all()
    serializer_class=SongsSerializer
    
    
class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Songs.objects.all()
    serializer_class=SongsSerializer
    
def methodinfo(request):
    dicts=request.META
   
    return HttpResponse("Http request is:"+str(request.headers['User-Agent']))