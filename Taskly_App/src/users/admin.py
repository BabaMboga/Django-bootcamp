from django.contrib import admin

from .models import Profile

# add an id on the django dashboard
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Profile, ProfileAdmin)
