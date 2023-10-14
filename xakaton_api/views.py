from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from .models import UserModel, EmergenciesPostModel, DiseaseStateCategoryModel, Chat, MessagesModel, Specialist
from .serializers import UserModelSerializer, EmergenciesPostModelSerializer, \
    DiseaseStateCategoryModelSerializer, ComplainSerializer, EmergenciesPostDetailSerializer, HistorySerializers, \
    ChatSerializers, MessagesModelSerializers
import json


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
            return Response({"result": True, "user": UserModelSerializer(user).data})

        return Response({"result": False, "user": None})

    @swagger_auto_schema(
        operation_description="Update a User instance by user_id",
        request_body=UserModelSerializer,
        responses={200: UserModelSerializer()},
    )
    def update(self, request, pk=None):
        try:
            user = UserModel.objects.get(user_id=pk)
        except UserModel.DoesNotExist:
            return Response({"result": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserModelSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            # Check if any fields have changed
            if any(getattr(user, field) != serializer.validated_data.get(field) for field in
                   serializer.validated_data.keys()):
                serializer.save()
                return Response({"result": True, "user": UserModelSerializer(user).data}, status=status.HTTP_200_OK)
            else:
                return Response({"result": True, "message": "No fields have changed. User not updated."})
        else:
            return Response({"result": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EmergenciesViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="List of Emergencies instances",
        responses={200: EmergenciesPostModelSerializer(many=True)},
    )
    def list(self, request):
        post = EmergenciesPostModel.objects.all()
        return Response(EmergenciesPostModelSerializer(post, many=True).data, status=status.HTTP_200_OK)


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
        user_id = request.data.get("user")
        user = UserModel.get_by_user_id(user_id=user_id)
        request.data["user"] = user.id
        serializer = ComplainSerializer(data=data)

        spec = Specialist.objects.filter(tag__specialist__in=request.data.get("category")).first()
        obj = Chat.objects.create(spec.user, user_id)
        obj.save()
        request.data["category"] = DiseaseStateCategoryModel.get_by_name_disease(request.data.get("category")).id
        request.data["specialist"] = spec.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_by_list(request, name: str):
    post = EmergenciesPostModel.objects.filter(category=name).first()
    post_uz = EmergenciesPostModel.objects.filter(category_uz=name).first()
    post_ru = EmergenciesPostModel.objects.filter(category_ru=name).first()
    if post:
        return Response(EmergenciesPostDetailSerializer(post).data, status=status.HTTP_200_OK)
    elif post_uz:
        return Response(EmergenciesPostDetailSerializer(post_uz).data, status=status.HTTP_200_OK)
    elif post_ru:
        return Response(EmergenciesPostDetailSerializer(post_ru).data, status=status.HTTP_200_OK)
    else:
        return Response({"error": f"{name} category not found"}, status=status.HTTP_404_NOT_FOUND)


class EmergenciesHistoryViewSet(ViewSet):

    @swagger_auto_schema(
        operation_description="Create a new EmergenciesHistory instance",
        request_body=HistorySerializers,
        responses={201: HistorySerializers()},
    )
    def create(self, request):
        data = request.data
        serializer = HistorySerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Create a new MessagesModel instance",
        request_body=MessagesModelSerializers,
        responses={201: MessagesModelSerializers()},
    )
    def create(self, request):
        data = request.data
        serializer = ChatSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="List by cat_id MessagesModel instances",
        responses={200: MessagesModelSerializers(many=True)},
    )
    def retrieve(self, request, pk=None):
        messages = MessagesModel.objects.filter(chat=pk).order_by("-created_at")
        return Response(MessagesModelSerializers(messages, many=True).data, status=status.HTTP_200_OK)


def chat_view(request):
    return render(request, "chat.html")


@api_view(["POST"])
def voice_or_text(request):
    import openai
    # OPEN_AI_API_KEY = "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"
    OPEN_AI_API_KEY = "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"
    openai.api_key = OPEN_AI_API_KEY

    print(request.body)

    data = request.body
    data = json.loads(data)
    print(data)
    # voice_url = data.get("voice")

    # if voice_url:
    #
    #     import speech_recognition as sr
    #
    #     recognizer = sr.Recognizer()
    #
    #     with sr.AudioFile('audio.ogg') as source:
    #         audio = recognizer.record(source)
    #
    #     try:
    #         text = recognizer.recognize_google(audio)
    #         # update.message.reply_text(f"Transcription: {text}")
    #     except sr.UnknownValueError:
    #         pass
    #         # update.message.reply_text("Sorry, I couldn't understand the audio.")
    #     except sr.RequestError:
    #         pass
    #         # update.message.reply_text("I'm having trouble connecting to the speech recognition service.")
    #
    # else:
    #     text = data.get("text")

    # here we detect
    user_id = data.get("user_id")
    text = data.get("text")

    user_obj = UserModel.objects.filter(user_id=user_id).first()
    if user_obj.language == 'uz':
        categories = [name.name_disease_uz for name in DiseaseStateCategoryModel.objects.all()]
    else:
        categories = [name.name_disease_ru for name in DiseaseStateCategoryModel.objects.all()]

    categories_str = ','.join(categories)
    chat_completion = openai.Completion.create(model="text-davinci-003",
                                               prompt=f"I have these categories: [{categories_str}] and "
                                                      f"my patient sends this text as complaint: {text}. "
                                                      f"Based on the patient's text, determine which "
                                                      f"category it should fit more closely. and return "
                                                      f"me that category name",
                                               temperature=0.6,
                                               max_tokens=1024
                                               )
    print(chat_completion)
    return Response({"status": "ok"})
