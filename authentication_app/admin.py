from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models , forms


class AuthUserAdmin(UserAdmin):
    
    add_form        = forms.AdminPanelUserCreationForm
    form            = forms.AdminPanelUserChangeForm
    model           = models.AuthUser
    list_display    = ['pk','username','date_joined','is_staff']
    
    fieldsets = (
        (None, {'fields': ("username", "password")}),
        ('Personal info', {'fields': ("first_name", "last_name", "email")}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('profile_photo','age','bio','phone_number',)}),
    )


admin.site.register(models.AuthUser, AuthUserAdmin)