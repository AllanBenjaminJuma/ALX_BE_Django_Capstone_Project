from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'full_name', 'role', 'phone_number', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'full_name', 'phone_number')
    list_filter = ('role', 'is_active', 'is_staff', 'is_superuser')