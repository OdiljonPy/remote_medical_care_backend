from django.contrib import admin
from .models import UserModel, DiseaseStateCategoryModel, EmergenciesPostModel, Specialist, Complain


# Register your models here.


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "username", "user_id", "phone_number"]


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "phone_number", "is_active"]


@admin.register(EmergenciesPostModel)
class EmergenciesPostModelAdmin(admin.ModelAdmin):
    list_display = ["category"]


@admin.register(DiseaseStateCategoryModel)
class DiseaseStateCategoryModelAdmin(admin.ModelAdmin):
    list_display = ["name_disease"]


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ["user", "category", "specialist"]
