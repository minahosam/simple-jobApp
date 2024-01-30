from django.contrib import admin
from .models import *

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title','salary','type')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(job,JobAdmin)