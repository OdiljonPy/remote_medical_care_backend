from rest_framework import serializers
from .models import UserModel, EmergenciesCategoryModel, EmergenciesPostModel, DiseaseStateCategoryModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "name", "username", "user_id", "phone_number"]


class EmergenciesCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergenciesCategoryModel
        fields = ["id", "category_name"]


class EmergenciesPostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergenciesPostModel
        fields = ["id", "image", "video"]


class DiseaseStateCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseStateCategoryModel
        fields = ["id", "name_disease"]
