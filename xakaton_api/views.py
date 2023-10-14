from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema
from .models import UserModel, EmergenciesPostModel, DiseaseStateCategoryModel
from .serializers import UserModelSerializer, EmergenciesPostModelSerializer, \
    DiseaseStateCategoryModelSerializer, ComplainSerializer, EmergenciesPostDetailSerializer


class CreateUser(ViewSet):

    @swagger_auto_schema(
        operation_description="Create a new User instance",
        request_body=UserModelSerializer,
        responses={201: UserModelSerializer()},
    )
    def create(self, request):
        data = request.data
        serializer = UserModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = UserModel.get_by_user_id(pk)
        if user:
            return Response({"result": True})

        return Response({"result": False})


class EmergenciesViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="List of Emergencies instances",
        responses={200: EmergenciesPostModelSerializer(many=True)},
    )
    def list(self, request):
        post = EmergenciesPostModel.objects.all()
        return Response(EmergenciesPostModelSerializer(post, many=True).data, status=status.HTTP_200_OK)

    def get_by_list(self, request, name: str):
        post = EmergenciesPostModel.objects.filter(category=name)
        return Response(EmergenciesPostDetailSerializer(post, many=True).data, status=status.HTTP_200_OK)


class DiseaseStateViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="List of DiseaseState instances",
        responses={200: DiseaseStateCategoryModelSerializer(many=True)},
    )
    def list(self, request):
        post = DiseaseStateCategoryModel.objects.all()
        return Response(DiseaseStateCategoryModelSerializer(post, many=True).data, status=status.HTTP_200_OK)


class ComplainViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="Create a new Complain instance",
        request_body=ComplainSerializer,
        responses={201: ComplainSerializer()},
    )
    def create(self, request):
        data = request.data
        serializer = ComplainSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def chat_view(request):
    return render(request, "chat.html")
