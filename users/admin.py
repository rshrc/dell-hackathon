from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User, UserProfile, InAppSearchHistory


@admin.register(InAppSearchHistory)
class InAppSearchAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user', 'product')

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'name', 'last_login')
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2')
    }),)

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = (
        'groups',
        'user_permissions',
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'birthday', 'city', 'country', 'gold_member']
    list_filter = ['gold_member']


admin.site.register(User, UserAdmin)
