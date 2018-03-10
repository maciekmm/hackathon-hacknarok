from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from core.models import Room, RoomCategory, Profile

admin.site.register(Room)
admin.site.register(RoomCategory)
# admin.site.register(Profile)


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
