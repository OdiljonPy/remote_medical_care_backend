from rest_framework import serializers
from .models import UserModel, EmergenciesPostModel, DiseaseStateCategoryModel, Complain, Specialist


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "name", "username", "user_id", "phone_number", "language"]


class EmergenciesPostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergenciesPostModel
        fields = ["id", "category", "category_uz", "category_ru"]


class EmergenciesPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergenciesPostModel
        fields = ["image", "video", ]


class DiseaseStateCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseStateCategoryModel
        fields = ["id", "name_disease", "name_disease_uz", "name_disease_ru"]


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ["id", "user", "category", "specialist"]


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ["id", "user", "name", "phone_number", "is_active"]
