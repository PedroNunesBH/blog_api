from django.contrib import admin
from .models import Post, PostLikeAndDislike


class AdminPost(admin.ModelAdmin):
    list_display = [field.name for field in Post._meta.fields]
    search_fields = ('title', )


class AdminPostLikeAndDislike(admin.ModelAdmin):
    list_display = [field.name for field in PostLikeAndDislike._meta.fields]
    search_fields = ("post", )


admin.site.register(Post, AdminPost)
admin.site.register(PostLikeAndDislike, AdminPostLikeAndDislike)
