from django.contrib import admin

from .models import *


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Users._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.username

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Anime._meta.fields]
    ordering = ['id']
    search_fields = ['name']
    
    def __str__(self):
        return self.name
    
@admin.register(Animeviewingstatus)
class AnimeviewingstatusAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Animeviewingstatus._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Comment._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Directoranime)
class DirectoranimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Directoranime._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Genreanime)
class GenreanimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Genreanime._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Listanimegenre)
class ListanimegenreAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Listanimegenre._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Listanimestudios)
class ListanimestudiosAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Listanimestudios._meta.fields]
    ordering = ['id_anime']
    
    def __str__(self):
        return self.name

@admin.register(Listanimesubtitles)
class ListanimesubtitlesAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Listanimesubtitles._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Statusanime)
class StatusanimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Statusanime._meta.fields]    
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Studioanime)
class StudioanimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Studioanime._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Typeanime)
class TypeanimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Typeanime._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Updateanime)
class UpdateanimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Updateanime._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Viewingstatus)
class ViewingstatusAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Viewingstatus._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

@admin.register(Voiceactinganime)
class VoiceactinganimeAdmin(admin.ModelAdmin):
    list_display = [fields.name for fields in Voiceactinganime._meta.fields]
    ordering = ['id']
    
    def __str__(self):
        return self.name

