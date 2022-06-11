from django.contrib import admin
from .models import Country, Image, Greetings

class PostAdmin1(admin.ModelAdmin):
    list_display = (
        'nickname',
        'country', 
        )
    search_fields = ('nickname',)

class PostAdmin2(admin.ModelAdmin):
    list_display = (
        'nickname',
        'image', 
        )
    search_fields = ('nickname',)

class PostAdmin3(admin.ModelAdmin):
    list_display = (
        'nickname',
        'greetings', 
        )
    search_fields = ('nickname',)



admin.site.register(Country, PostAdmin1)
admin.site.register(Image, PostAdmin2)
admin.site.register(Greetings, PostAdmin3)

