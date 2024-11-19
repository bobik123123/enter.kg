from django.contrib import admin
from .models import *

@admin.register(PageName)
class PageName(admin.ModelAdmin):
    pass

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    pass



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Static)
class StaticAdmin(admin.ModelAdmin):
    pass