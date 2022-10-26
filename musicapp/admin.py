from django.contrib import admin
from .models import Song, Artiste, Lyric
# Register your models here.
admin.site.register(Song)
admin.site.register(Lyric)
admin.site.register(Artiste)