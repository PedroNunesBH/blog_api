from django.contrib import admin
from .models import Comment


class AdminComment(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    search_fields = ("title", )


admin.site.register(Comment, AdminComment)
