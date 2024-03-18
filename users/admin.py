from django.contrib import admin
from .models import BlogUser


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BlogUser._meta.fields]
    search_fields = ('name', )


admin.site.register(BlogUser, UserAdmin)
