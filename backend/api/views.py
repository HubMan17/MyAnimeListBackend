from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins

from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *
from .permissions import *


class UsersViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    """Make custome permissions"""
    queryset = Users.objects.filter(is_superuser=False, is_staff=False)
    serializer_class = UsersSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    # authentication_classes = [JWTAuthentication, ]
    

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class AnimeviewingstatusViewSet(viewsets.ModelViewSet):
    """Make custome permissions"""
    queryset = Animeviewingstatus.objects.all()
    serializer_class = AnimeviewingstatusSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class DirectoranimeViewSet(viewsets.ModelViewSet):
    queryset = Directoranime.objects.all()
    serializer_class = DirectoranimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class GenreanimeViewSet(viewsets.ModelViewSet):
    queryset = Genreanime.objects.all()
    serializer_class = GenreanimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class ListanimegenreViewSet(viewsets.ModelViewSet):
    queryset = Listanimegenre.objects.all()
    serializer_class = ListanimegenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class ListanimestudiosViewSet(viewsets.ModelViewSet):
    queryset = Listanimestudios.objects.all()
    serializer_class = ListanimestudiosSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class ListanimesubtitlesViewSet(viewsets.ModelViewSet):
    queryset = Listanimesubtitles.objects.all()
    serializer_class = ListanimesubtitlesSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class StatusanimeViewSet(viewsets.ModelViewSet):
    queryset = Statusanime.objects.all()
    serializer_class = StatusanimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class StudioanimeViewSet(viewsets.ModelViewSet):
    queryset = Studioanime.objects.all()
    serializer_class = StudioanimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class TypeanimeSerializer(viewsets.ModelViewSet):
    queryset = Typeanime.objects.all()
    serializer_class = TypeAnimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class UpdateanimeViewSet(viewsets.ModelViewSet):
    queryset = Updateanime.objects.all()
    serializer_class = UpdateanimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class ViewingstatusViewSet(viewsets.ModelViewSet):
    queryset = Viewingstatus.objects.all()
    serializer_class = ViewingstatusSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    
    
class VoiceactinganimeViewSet(viewsets.ModelViewSet):
    queryset = Voiceactinganime.objects.all()
    serializer_class = VoiceactinganimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
