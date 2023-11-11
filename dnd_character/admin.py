from django.contrib import admin
from .models import Character, Race, CharacterClass, Alignment

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'character_class', 'level')
admin.site.register(Character, CharacterAdmin)
admin.site.register(Race)
admin.site.register(CharacterClass)
admin.site.register(Alignment)





# Register your models here.
