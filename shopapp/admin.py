from django.contrib import admin
from shopapp.models import categ,products
from .models import *


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display=['name','slug']
admin.site.register(categ, catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    list_display=['name','slug','price','desc','stock','img']
    list_editable=('price','desc','stock','img')
admin.site.register(products,prodadmin)
