from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    user_id = models.IntegerField(default=0)
    username = models.CharField(max_length=150, default=None)
    phone_number = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_by_user_id(user_id: int):
        user = UserModel.objects.filter(user_id=user_id).first()
        return user


class EmergenciesPostModel(models.Model):
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    video = models.FileField(upload_to="video/")
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


class Specialist(models.Model):
    user = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Complain(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    category = models.ForeignKey(DiseaseStateCategoryModel, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user_id
