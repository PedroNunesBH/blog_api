from django.contrib import admin
from .models import Post


class AdminPost(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    search_fields = ('title', )


admin.site.register(Post, AdminPost)
