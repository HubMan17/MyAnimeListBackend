from django.db import models


class Users(models.Model):
    username = models.CharField(db_column='userName', max_length=255)  # Field name made lowercase.
    password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    telegramuserid = models.CharField(db_column='telegramUserId', max_length=255)  # Field name made lowercase.
    bindingtelegram = models.BooleanField(db_column='bindingTelegram')  # Field name made lowercase.
    bindingemail = models.BooleanField(db_column='bindingEmail')  # Field name made lowercase.
    registration = models.DateField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'


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

    class Meta:
        managed = False
        db_table = 'anime'


class Animeviewingstatus(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='user')
    anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='anime')
    status = models.ForeignKey('Viewingstatus', models.DO_NOTHING, db_column='status')

    class Meta:
        managed = False
        db_table = 'animeViewingStatus'


class Comment(models.Model):
    users = models.ForeignKey(Users, models.DO_NOTHING)
    anime = models.ForeignKey(Anime, models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comment'


class Directoranime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'directorAnime'
        verbose_name = 'Режиссеры'
        verbose_name_plural = 'Режиссеры'


class Genreanime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'genreAnime'


class Listanimegenre(models.Model):
    id_anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='id_anime')
    id_genre = models.ForeignKey(Genreanime, models.DO_NOTHING, db_column='id_genre')

    class Meta:
        managed = False
        db_table = 'listAnimeGenre'
        unique_together = (('id_anime', 'id_genre'),)


class Listanimestudios(models.Model):
    id_anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='id_anime')
    id_studio = models.ForeignKey('Studioanime', models.DO_NOTHING, db_column='id_studio')

    class Meta:
        managed = False
        db_table = 'listAnimeStudios'
        unique_together = (('id_anime', 'id_studio'),)


class Listanimesubtitles(models.Model):
    id_anime = models.ForeignKey(Anime, models.DO_NOTHING, db_column='id_anime')
    id_subtitles = models.ForeignKey('Voiceactinganime', models.DO_NOTHING, db_column='id_subtitles')

    class Meta:
        managed = False
        db_table = 'listAnimeSubtitles'
        unique_together = (('id_anime', 'id_subtitles'),)


class Statusanime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'statusAnime'


class Studioanime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'studioAnime'


class Typeanime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'typeAnime'


class Updateanime(models.Model):
    anime = models.ForeignKey(Anime, models.DO_NOTHING)
    series = models.BigIntegerField(blank=True, null=True)
    status = models.ForeignKey(Statusanime, models.DO_NOTHING, db_column='status', blank=True, null=True)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'updateanime'


class Viewingstatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'viewingStatus'


class Voiceactinganime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'voiceActingAnime'
