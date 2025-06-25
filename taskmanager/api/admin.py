from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Task  # Your custom models

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Optional: customize what shows in the list view
    list_display = ['username', 'email', 'role', 'is_active', 'is_staff']
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'deadline', 'status']
