from django.urls import path
from rest_framework import routers
from .views import CreateUser, EmergenciesViewSet, DiseaseStateViewSet, ComplainViewSet, get_by_list, \
    EmergenciesHistoryViewSet, voice_or_text, MessagesViewSet, ChatList

router = routers.DefaultRouter()
router.register('user', CreateUser, "user")
router.register('ttb', EmergenciesViewSet, " ttb")
router.register('disease', DiseaseStateViewSet, "disease")
router.register('complain', ComplainViewSet, "complain")
router.register('history', EmergenciesHistoryViewSet, "history")
router.register('messages', MessagesViewSet, "messages")
router.register('chat', ChatList, "chat")

urlpatterns = [
    path("ttb/<str:name>/", get_by_list),
    path("voice/", voice_or_text)
]

urlpatterns += router.urls
