from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Atom)
class AtomAdmin(admin.ModelAdmin):
    list_display=['title','author']
    list_display_links=['title','author']
    search_fields=['title']



    class Meta:
        model=Atom
