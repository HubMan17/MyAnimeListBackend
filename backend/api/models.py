from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class Users(AbstractUser):
    telegramuserid = models.CharField(db_column='telegramUserId', max_length=255, null=True)  # Field name made lowercase.
    bindingtelegram = models.BooleanField(db_column='bindingTelegram', default=False)  # Field name made lowercase.
    bindingemail = models.BooleanField(db_column='bindingEmail', default=False)  # Field name made lowercase.
    code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'api_users'
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'


class Anime(models.Model):
    name = models.CharField(max_length=255)
    seriescount = models.CharField(db_column='seriesCount', max_length=255)  # Field name made lowercase.
    status = models.ForeignKey('Statusanime', models.DO_NOTHING, db_column='status')
    type = models.ForeignKey('Typeanime', models.DO_NOTHING, db_column='type')
    releasedate = models.CharField(db_column='releaseDate', max_length=255)  # Field name made lowercase.
    director = models.ForeignKey('Directoranime', models.DO_NOTHING, db_column='director')
    othernames = models.CharField(db_column='otherNames', max_length=255)  # Field name made lowercase.
    idtitle = models.BigIntegerField(db_column='idTitle', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'anime'
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class Animeviewingstatus(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='user')
    anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='anime')
    status = models.ForeignKey('Viewingstatus', models.DO_NOTHING, db_column='status')

    class Meta:
        managed = False
        db_table = 'animeViewingStatus'
        verbose_name = 'Статус просмотра аниме пользователями'
        verbose_name_plural = 'Статус просмотра аниме пользователями'


class Comment(models.Model):
    users = models.ForeignKey(Users, models.DO_NOTHING)
    anime = models.ForeignKey(Anime, models.DO_NOTHING, blank=True, null=False)
    date = models.DateField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comment'
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


class Directoranime(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'directorAnime'
        verbose_name = 'Режиссеры'
        verbose_name_plural = 'Режиссеры'


class Genreanime(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'genreAnime'
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'


class Listanimegenre(models.Model):
    id_anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='id_anime')
    id_genre = models.ForeignKey(Genreanime, models.DO_NOTHING, db_column='id_genre')

    class Meta:
        managed = False
        db_table = 'listAnimeGenre'
        unique_together = (('id_anime', 'id_genre'),)
        verbose_name = 'Жанры аниме'
        verbose_name_plural = 'Жанры аниме'


class Listanimestudios(models.Model):
    id_anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='id_anime')
    id_studio = models.ForeignKey('Studioanime', models.DO_NOTHING, db_column='id_studio')

    class Meta:
        managed = False
        db_table = 'listAnimeStudios'
        unique_together = (('id_anime', 'id_studio'),)
        verbose_name = 'Студии аниме'
        verbose_name_plural = 'Студии аниме'


class Listanimesubtitles(models.Model):
    id_anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='id_anime')
    id_subtitles = models.ForeignKey('Voiceactinganime', models.DO_NOTHING, db_column='id_subtitles')

    class Meta:
        managed = False
        db_table = 'listAnimeSubtitles'
        unique_together = (('id_anime', 'id_subtitles'),)
        verbose_name = 'Озвучки аниме'
        verbose_name_plural = 'Озвучки аниме'


class Statusanime(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

    class Meta:
        managed = False
        db_table = 'statusAnime'
        verbose_name = 'Статус аниме'
        verbose_name_plural = 'Статус аниме'
        
    def __str__(self):
        return self.name


class Studioanime(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'studioAnime'
        verbose_name = 'Студии'
        verbose_name_plural = 'Студии'


class Typeanime(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'typeAnime'
        verbose_name = 'Типы'
        verbose_name_plural = 'Типы'


class Updateanime(models.Model):
    anime = models.ForeignKey(Anime, models.DO_NOTHING)
    series = models.BigIntegerField(blank=True, null=True) # integer or null
    status = models.ForeignKey(Statusanime, models.DO_NOTHING, db_column='status', blank=True, null=True) # integer or null
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'updateanime'
        verbose_name = 'Обновления аниме'
        verbose_name_plural = 'Обновления аниме'


class Viewingstatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'viewingStatus'
        verbose_name = 'Статус просмотра'
        verbose_name_plural = 'Статус просмотра'


class Voiceactinganime(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'voiceActingAnime'
        verbose_name = 'Озвучки'
        verbose_name_plural = 'Озвучки'
