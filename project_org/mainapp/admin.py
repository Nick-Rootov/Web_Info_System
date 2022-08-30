from django.contrib import admin
from .models import *

# Register your models here.

class SotrudnikiAdmin (admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'otchestvo','zarplata', 'cat')
    list_display_links = ('id', 'zarplata')
    search_fields = ('last_name', 'cat')
    list_filter = ('cat',)
    list_editable = ('cat',)


admin.site.register(Sotrudniki,SotrudnikiAdmin)


admin.site.register(Category)
admin.site.register(Dogovor)
admin.site.register(Project)
admin.site.register(Otdel)
admin.site.register(Machine)