from rest_framework import serializers
from .models import UserModel, EmergenciesPostModel, DiseaseStateCategoryModel, Complain, Specialist


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "name", "username", "user_id", "phone_number"]


class EmergenciesPostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergenciesPostModel
        fields = ["id", "category"]


class EmergenciesPostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergenciesPostModel
        fields = ["image", "video", ]


class DiseaseStateCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseStateCategoryModel
        fields = ["id", "name_disease"]


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = ["id", "user", "category", "specialist"]


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ["id", "user", "name", "phone_number", "is_active"]
