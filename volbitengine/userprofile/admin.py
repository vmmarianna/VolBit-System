from django.contrib import admin

# Define the admin class
from .models import *


# Register your models here.
# admin.site.register(models.Login)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'surname', 'name', 'patronymic', 'date_of_birth', 'ph_number', 'email')


# Register the admin class with the associated model
admin.site.register(UserProfile, ProfileAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id_group', 'name_group')


# Register the admin class with the associated model
admin.site.register(Group, GroupAdmin)


class CompClassAdmin(admin.ModelAdmin):
    list_display = ('id_comp', 'price', 'beg_hours', 'end_hours')


# Register the admin class with the associated model
admin.site.register(CompClass, CompClassAdmin)
