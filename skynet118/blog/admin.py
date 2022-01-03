from django.contrib import admin
from .models import (
        UserProfile,
        Portfolio,
        Comment
        )

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)

