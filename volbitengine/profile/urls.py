from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import *

urlpatterns = [
    path('', prof_list, name='profile_list_url'),
    path('profile/<int:id_profile>/', profile_detail, name='profile_detail_url'),
    path('groups/', group_list, name='groups_list_url'),
    path('group/<int:id_group>/', group_detail, name='group_detail_url'),
    path('compclass/', compclass_list, name='compclass_list_url'),
    path('compcl/<int:id_comp>/', compclass_detail, name='compclass_detail_url'),
]
