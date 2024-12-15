from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from api.views import *

from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = routers.SimpleRouter()

router.register('users', UsersViewSet)
router.register('anime', AnimeViewSet)
router.register('anime-viewing-status', AnimeviewingstatusViewSet)
router.register('comment', CommentViewSet)
router.register('director-anime', DirectoranimeViewSet)
router.register('genre-anime', GenreanimeViewSet)
router.register('list-anime-genre', ListanimegenreViewSet)
router.register('list-anime-studios', ListanimestudiosViewSet)
router.register('list-anime-subtitles', ListanimesubtitlesViewSet)
router.register('status-anime', StatusanimeViewSet)
router.register('studio-anime', StudioanimeViewSet)
router.register('type-anime', TypeanimeSerializer)
router.register('update-anime', UpdateanimeViewSet)
router.register('viewing-status', ViewingstatusViewSet)
router.register('voice-acting-anime', VoiceactinganimeViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
