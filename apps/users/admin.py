from django.contrib import admin

# Register your models here.

from users import models

# admin.site.register(models.UserProfile)


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.UserProfile, UserProfileAdmin)