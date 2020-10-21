from django.contrib import admin
from .models import Profile


# class Profile(admin.ModelAdmin):
#     model = Profile


class ProfileAdmin(admin.ModelAdmin):
    fields = ('first_name', 'description', 'location')


admin.site.register(Profile, ProfileAdmin)
