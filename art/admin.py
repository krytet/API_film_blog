from django.contrib import admin
from .models import Categories, Genres, Titles, Reviws, Comments
# Register your models here.


admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Titles)
admin.site.register(Reviws)
admin.site.register(Comments)