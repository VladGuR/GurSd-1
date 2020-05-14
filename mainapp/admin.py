from django.contrib import admin
from mainapp.models import Game, Genre, GameComment, UserGame

admin.site.register(Game)
admin.site.register(GameComment)
admin.site.register(Genre)
admin.site.register(UserGame)

