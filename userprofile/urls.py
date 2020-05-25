from django.urls import path
from . import views

from .views import *

urlpatterns = [
    path('userprofile/<int:user_id>/', profile_detail, name='profile_detail_url'),
    path('profile_list', prof_list, name='profile_list_url'),
    path('groups/', group_list, name='groups_list_url'),
    path('group/<int:id_group>/', group_detail, name='group_detail_url'),
    path('compclass/', compclass_list, name='compclass_list_url'),
    path('places/', places_list, name='places_list_url'),
    path('registration/', registration, name='user_registration'),
    path('teacherprofile/', teach_list, name='teachers_list_url'),
    path('teacher/<int:id_teacher>/', teach_detail, name='teacher_detail_url'),
    path('lessons/', lessons_list, name='lessons_detail_url'),
    path('pay_statement/', statement_pay, name='statement_detail_url'),
    path('', inform, name='info_url'),
    path('login/', views.user_login, name='login'),
    path('logout/', logout_user, name='logout'),
]
