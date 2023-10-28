from django.contrib import admin
from .models import Character, Race, CharacterClass

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'character_class', 'level')
admin.site.register(Character, CharacterAdmin)
admin.site.register(Race)
admin.site.register(CharacterClass)





# Register your models here.
