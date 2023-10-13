from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from .models import UserModel, EmergenciesPostModel, EmergenciesCategoryModel, DiseaseStateCategoryModel
from .serializers import UserModelSerializer, EmergenciesCategoryModelSerializer, EmergenciesPostModelSerializer, \
    DiseaseStateCategoryModelSerializer


# Create your views here.


class CreateUser(ViewSet):
    def create(self, request):
        data = request.data
        serializer = UserModelSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = UserModel.get_by_user_id(pk)
        if user:
            return Response({"result":True})
