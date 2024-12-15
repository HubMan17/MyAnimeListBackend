from rest_framework import serializers

from .models import *


class UsersSerializer(serializers.ModelSerializer):
    
    
    def create(self, validated_data):
        return Users.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
    
    class Meta:
        model = Users
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'
        
        
class AnimeviewingstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animeviewingstatus
        fields = '__all__'
        

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
    
class DirectoranimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directoranime
        fields = '__all__'
        
        
class GenreanimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genreanime
        fields = '__all__'
        
        
class ListanimegenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listanimegenre
        fields = '__all__'
        
        
class ListanimestudiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listanimestudios
        fields = '__all__'
        
        
class ListanimesubtitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listanimesubtitles
        fields = '__all__'
        

class StatusanimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statusanime
        fields = '__all__'
        
        
class StudioanimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studioanime
        fields = '__all__'

        
class TypeAnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeanime
        fields = '__all__'
        
        
class UpdateanimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Updateanime
        fields = '__all__'
        
        
class ViewingstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewingstatus
        fields = '__all__'
        
        
class VoiceactinganimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiceactinganime
        fields = '__all__'
