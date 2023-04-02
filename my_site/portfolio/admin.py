from django.contrib import admin
from .models import Post, Achievement

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


class AchievementAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Post, PostAdmin)
admin.site.register(Achievement, AchievementAdmin)
