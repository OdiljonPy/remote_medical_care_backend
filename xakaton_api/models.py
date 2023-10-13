from django.db import models


# Create your models here.


class UserModel(models.Model):
    name = models.CharField(max_length=150)
    user_id = models.IntegerField()
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


class EmergenciesCategoryModel(models.Model):
    category_name = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class EmergenciesPostModel(models.Model):
    image = models.ImageField(upload_to="image/", null=True, blank=True)
    video = models.FileField(upload_to="video/")
    category = models.ForeignKey(EmergenciesCategoryModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category.category_name

    @staticmethod
    def get_by_category(category_id: int):
        post = EmergenciesPostModel.objects.filter(category=category_id)
        return post


class DiseaseStateCategoryModel(models.Model):
    name_disease = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_disease
