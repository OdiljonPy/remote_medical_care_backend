from django.contrib import admin
from .models import UserModel, DiseaseStateCategoryModel, EmergenciesPostModel, Specialist, Complain, \
    EmergenciesHistory, Chat, MessagesModel


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


@admin.register(EmergenciesHistory)
class EmergenciesHistoryAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "phone_number", "age", "category", "latitude", "longitude"]


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ["id", "doctor_id", "patient_id", "is_active"]


@admin.register(MessagesModel)
class MessagesModelAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "text", "files", "chat", "created_at"]
