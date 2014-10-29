from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
	fieldsets = (
			('Datos de Usuario', { 'fields' : ('username', 'password')}),
			('Informacion Personal', { 'fields' : ('first_name', 'last_name', 'email', 'avatar')}),
			('Permisos', { 'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		)
admin.site.register(User, UserAdmin)
