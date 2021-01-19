from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Playlist
from .serializers import UserSerializer, PlaylistSerializer
from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        query_set = User.objects.filter(userid=data.get('userid'))
        serializer = UserSerializer(data=data)
        if len(query_set) <= 0:
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            if serializer.is_valid():
                return JsonResponse(serializer.data, status=404)


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        query_set = User.objects.filter(userid=data.get('userid'))
        if serializer.is_valid():
            if len(query_set) <= 0:
                return JsonResponse(serializer.data, status=400)
            else:
                if query_set[0].password != data.get('password'):
                    return JsonResponse(serializer.data, status=401)
                else:
                    return JsonResponse(serializer.data, status=201)


@csrf_exempt
def send(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlaylistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
def receive(request):
    if request.method == 'GET':
        query_set = Playlist.objects.all()
        serializer = PlaylistSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False, status=201)


@csrf_exempt
def delete(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        query_set = Playlist.objects.filter(userid=data.get('userid'))
        if serializer.is_valid:
            if len(query_set) > 0:
                obj = query_set[0]
                obj.delete()
                return JsonResponse(serializer.data, status=200)


@csrf_exempt
def users(request):
    if request.method == 'GET':
        query_set = User.objects.all()
        serializer = UserSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'DELETE':
        query_set = User.objects.all()
        query_set.delete()
        return HttpResponse(status=200)


@csrf_exempt
def user(request, pk):
    obj = User.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = UserSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serializer = UserSerializer(obj)
        obj.delete()
        return HttpResponse(status=204)


@csrf_exempt
def playlists(request):
    if request.method == 'GET':
        query_set = Playlist.objects.all()
        serializer = PlaylistSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlaylistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        query_set = Playlist.objects.all()
        query_set.delete()
        return HttpResponse(status=200)


@csrf_exempt
def playlist(request, pk):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PlaylistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'GET':
        query_set = Playlist.objects.all()
        serializer = PlaylistSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)