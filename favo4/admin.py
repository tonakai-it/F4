from django.contrib import admin

from .models import Content, Chara, PostTwi, Favorite4, Subclass
# Register your models here.

admin.site.register((Content, Chara, PostTwi, Favorite4, Subclass))
