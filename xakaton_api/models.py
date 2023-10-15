from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.IntegerField(default=0)
    language = models.CharField(max_length=2, default='uz')
    username = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"name: {self.name}"

    @staticmethod
    def get_by_user_id(user_id: int):
        user = UserModel.objects.filter(user_id=user_id).first()
        return user


class EmergenciesPostModel(models.Model):
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    video = models.FileField(upload_to="video/", null=True, blank=True)
    category = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category


class DiseaseStateCategoryModel(models.Model):
    name_disease = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_disease

    @staticmethod
    def get_by_name_disease(name_disease: str):
        obj_uz = DiseaseStateCategoryModel.objects.filter(name_disease_uz=name_disease).first()
        obj_ru = DiseaseStateCategoryModel.objects.filter(name_disease_ru=name_disease).first()
        if obj_uz:
            return obj_uz
        elif obj_ru:
            return obj_ru


class Specialist(models.Model):
    user = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    tag = models.ManyToManyField(DiseaseStateCategoryModel)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Complain(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(DiseaseStateCategoryModel, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    analizlar = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"user: {self.user.user_id}"


class EmergenciesHistory(models.Model):
    user = models.IntegerField(default=0)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=150, null=True, blank=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


class Chat(models.Model):
    doctor_id = models.IntegerField(default=0)
    patient_id = models.IntegerField(default=0)
    complain = models.OneToOneField(Complain, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_by_complain(complain_id: int):
        obj = Chat.objects.filter(complain=complain_id).first()
        return obj

    def __str__(self):
        return f"Chat_id: {self.id}"


class MessagesModel(models.Model):
    author = models.IntegerField(default=0)
    text = models.TextField(null=True, blank=True)
    files = models.FileField(upload_to='chat/', null=True, blank=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"author: {self.author}"
