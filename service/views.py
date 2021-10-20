from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import UserModels, RepoModels
from .serializers import UserSerialezr, RepoSerializer
from django.views import View
import json
from .utils import get_data_from_api


class RepoViews(ModelViewSet):
    model = UserModels
    queryset = UserModels.objects.all()
    serializer_class = UserSerialezr


class AddRepo(APIView):

    def get(self, request, format=None):

        res = get_data_from_api(json.loads(request.body).get('name', None))
        if res:
            serializer = UserSerialezr(data=res)
            print()
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        form = request.Post
        if form.is_valid():
            print(form)
