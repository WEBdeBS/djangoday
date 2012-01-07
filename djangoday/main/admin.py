from django.contrib.admin.options import ModelAdmin

from main.models import CallForPaper

__author__ = 'sam'
from django.contrib.admin import site

class CFPAdmin(ModelAdmin):
    list_display = ['nome','cognome','titolo']

site.register(CallForPaper,CFPAdmin)
