from django.contrib import admin

# Define the admin class
from .models import *


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id_profile', 'surname', 'name', 'patronymic', 'sex', 'date_of_birth', 'ph_number', 'user',)


# Register the admin class with the associated model
admin.site.register(UserProfile, ProfileAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id_group', 'name_group')


# Register the admin class with the associated model
admin.site.register(Group, GroupAdmin)


class CompClassAdmin(admin.ModelAdmin):
    list_display = ('id_comp', 'price', 'long', 'weekday', 'beg_hours', 'end_hours')


# Register the admin class with the associated model
admin.site.register(CompClass, CompClassAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id_place', 'name_place', 'address', 'floor', 'office')
    # Register the admin class with the associated model


admin.site.register(Place, PlaceAdmin)


class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('id_teacher', 'surname', 'name', 'patronymic', 'sex', 'date_of_birth', 'ph_number')
    # Register the admin class with the associated model


admin.site.register(TeacherProfile, TeacherProfileAdmin)


class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id_lesson', 'pay', 'date_start ', 'date_end', 'data_statement', 'pay_statement')
    # Register the admin class with the associated model


admin.site.register(Lesson)


class StatementAdmin(admin.ModelAdmin):
    list_display = ('id_statement', 'pay_statement', 'data_statement')


admin.site.register(Statement)
