from django.contrib import admin
from .models import Person,Cars,Man,Business,Profile,Accoutn
# Register your models here.
admin.site.register(Cars)
admin.site.register(Man)
admin.site.register(Business)
admin.site.register(Profile)
admin.site.register(Accoutn)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','hobby']
    search_fields = ['name']
    list_per_page = 2 # сторінки
    list_display_links = ['age', 'hobby'] # кликабельность
    ordering = ['age'] # сортування від < do > 
    readonly_fields = ['name'] # заглушка для редагування 
    