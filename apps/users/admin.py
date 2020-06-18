from django.contrib import admin
from .models import Users


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "account", "user_type", "password", "gender", "email", "portrait",
                    "permission"]
    list_editable = ["name", "account", "password", "gender", "email", "permission"]


admin.site.register(Users, UserAdmin)
