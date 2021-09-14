from django.contrib import admin

from .models import Categories, Comments, Genre_Title, Genres, Reviews, Titles

# Register your models here.


admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Titles)
admin.site.register(Reviews)
admin.site.register(Comments)
admin.site.register(Genre_Title)