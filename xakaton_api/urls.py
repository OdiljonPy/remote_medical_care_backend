from django.urls import path
from rest_framework import routers
from .views import CreateUser, EmergenciesViewSet, DiseaseStateViewSet, ComplainViewSet, get_by_list, EmergenciesHistoryViewSet

router = routers.DefaultRouter()
router.register('user', CreateUser, "user")
router.register('ttb', EmergenciesViewSet, " ttb")
router.register('disease', DiseaseStateViewSet, "disease")
router.register('complain', ComplainViewSet, "complain")
router.register('history', EmergenciesHistoryViewSet, "history")


urlpatterns = [
    path("ttb/<str:name>/", get_by_list)
]

urlpatterns += router.urls
