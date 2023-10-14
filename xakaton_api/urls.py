from django.urls import path
from rest_framework import routers
from .views import CreateUser, EmergenciesViewSet, DiseaseStateViewSet, ComplainViewSet

router = routers.DefaultRouter()
router.register('user', CreateUser, "user")
router.register('ttb', EmergenciesViewSet, " ttb")
router.register('disease', DiseaseStateViewSet, "disease")
router.register('complain', ComplainViewSet, "complain")

urlpatterns = [
]

urlpatterns += router.urls
